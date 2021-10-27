import sys

from numpy.core.shape_base import block
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from Ui_frame import Ui_MainWindow
#from settings import setting
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QFileDialog
import pyqtgraph as pg
from pyqtgraph import exporters
import numpy as np
from skimage.measure import block_reduce
from client import receiver
from threading import Thread
import time
from scipy import signal

from brush import CurveWidget,ScatterWidget

def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()

class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style,"r") as f:
            return f.read()


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.collection_settings_save.clicked.connect(self.collections_setting_func)
        #self.graph = pg.PlotWidget(self)
        self.divided_graph_curve = CurveWidget(parent=None)
        self.divided_graph_scatter = ScatterWidget(parent=None)
        self.gridLayout.addWidget(self.divided_graph_curve)
        self.rawdata = []
        #self.binned = np.zeros(1024)
        self.buffer = []
        #self.original = np.histogram(np.random.normal(size=40960),bins=4096)[0]
        self.original = []
        self.binned = self.original.copy()
        
        self.start_button.clicked.connect(self.start_collection)
        self.pause_button.clicked.connect(self.pause_collection)
        self.end_button.clicked.connect(self.end_collection)
        self.on_collection = False
        self.status = "End"
        self.end_option = "Time"
        self.full_time = 0
        self.full_count = 0
        
        self.disp = QtWidgets.QLabel()
        self.collection_setting_display.addWidget(self.disp)
        self.connection_disp = QtWidgets.QLabel()
        self.connection_icon_layout.addWidget(self.connection_disp)
        self.link_source.clicked.connect(self.link)
        self.cut_source.clicked.connect(self.cut)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.timeout.connect(self.update_plot)
        #self.timer.start(1000)

        self.global_time = 0
        self.start_time = 0
        self.end_time = 0

        self.plot_option = self.plot_method.currentText()
        self.expand_option = "Original"
        self.display_setting_save.clicked.connect(self.display_setting_func)

        self.source = "Simulation"
        #self.receiver_agent = receiver("127.0.0.1",6688,1024)

        self.export_spectrum.clicked.connect(self.export_image)
        self.set_path.clicked.connect(self.new_path)

        qssStyle = CommonHelper.readQss("qss/MacOS.qss")
        self.setStyleSheet(qssStyle)
        

    def display_setting_func(self):
        self.plot_option = self.plot_method.currentText()
        self.expand_option = self.curve_expansion.currentText()
        if self.plot_option == "Line":
            clearLayout(self.gridLayout)
            self.divided_graph_curve = CurveWidget(parent=None)
            self.gridLayout.addWidget(self.divided_graph_curve)
            print("Line show")
        
        elif self.plot_option == "Scatter":
            clearLayout(self.gridLayout)
            self.divided_graph_scatter = ScatterWidget(parent=None)
            self.gridLayout.addWidget(self.divided_graph_scatter)
            print("Scatter show")



    def collections_setting_func(self):
        print(self.collection_source.currentText())
        
        self.source = self.collection_source.currentText()
        if self.count_time_option.isChecked():
            self.end_option = "Time"
            self.full_time = float(self.count_time_setting.text())
            print("Expected time: {}".format(self.full_time))
        elif self.total_count_option.isChecked():
            self.end_option = "Count"
            self.full_count = float(self.tota_count_setting.text())
            print("Expected count: {}".format(self.full_count))
        
        #调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        Icon = QtGui.QPixmap(sys.path[0]+'/templates/'+self.source+".jpeg")
        # 在disp里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.disp.setPixmap(Icon)
        self.disp.setScaledContents(True)
        print("Collection settings saved")
        pass
    
    def link(self):
        # Collection type: simulation
        if self.source == "Simulation":
            Icon = QtGui.QPixmap(sys.path[0]+"/templates/connected.jpeg")
            self.connection_disp.setPixmap(Icon)
            self.connection_disp.setScaledContents(True)
            self.original = np.histogram(np.random.normal(size=40960),bins=4096)[0]
            return
        ip = self.ip_addr_input.text()
        port = int(self.port_input.text())
        print(ip)
        print(port)
        self.receiver_agent = receiver(ip,port,1024)
        self.receiver_agent.connect()
        
        if not self.receiver_agent.connected:
            Icon = QtGui.QPixmap(sys.path[0]+"/templates/disconnected.jpeg")
            self.connection_disp.setPixmap(Icon)
            self.connection_disp.setScaledContents(True)
            return
        elif self.receiver_agent.connected:
            Icon = QtGui.QPixmap(sys.path[0]+"/templates/connected.jpeg")
            self.connection_disp.setPixmap(Icon)
            self.connection_disp.setScaledContents(True)
            
            #连接成功之后，开启一个可以不断读取数据的子线程
            print("Start receiver thread")
            self.recv_thread = Thread(target=self.fetch_data,args=(self.receiver_agent,))
            self.recv_thread.setDaemon(True)
            self.recv_thread.start()

    def cut(self):
        self.receiver_agent.disconnect()
        Icon = QtGui.QPixmap(sys.path[0]+"/templates/disconnected.jpeg")
        self.connection_disp.setPixmap(Icon)
        self.connection_disp.setScaledContents(True)

    def fetch_data(self,agent):
        #在子线程里面用死循环，一旦agent不再连接，子线程就会结束，等待下一次线程开启
        while True:
            if not agent.connected:
                print("Collection Ended")
                break
            data = agent.regular_receive()
            self.buffer = data
            #print("Fetched {}".format(str(max(data))))
            time.sleep(1)
            #print(self.buffer)
            #np.savetxt('log.txt',np.array(self.buffer),delimiter=',')
            #print("Got "+str(data))
        

    def update_data(self):
        self.global_time = time.time() - self.start_time
        
        if self.end_option == "Time" and self.global_time > self.full_time:
            print("Reached full time")
            self.pause_collection()
            return
        elif self.end_option == "Count" and sum(self.original) > self.full_count:
            print("Reached full count")
            self.pause_collection()
        
        if self.end_option == "Time":
            self.finished_percentage.setValue(int(self.global_time/self.full_time*100))
        elif self.end_option == "Count":
            self.finished_percentage.setValue(int(sum(self.original)/self.full_count*100))
        
        if self.on_collection == False:
            return 
        
        self.count_rate.display(sum(self.original)/self.global_time)
        self.calculate_integral()
        self.calculate_peak_area()
        self.calculate_half_wave()
        
        if self.source == "Simulation":
            self.original = self.original*1.005
            self.time_elapsed.display(self.global_time)
            self.total_count.display(sum(self.original))
            return
        self.time_elapsed.display(self.global_time)
        self.total_count.display(sum(self.buffer))
        print(max(self.buffer))
        """
        new_income = np.random.randn()
        self.rawdata.append(new_income)
        self.binned = np.histogram(np.array(self.rawdata),bins=1024)[0]
        """
        #self.original = np.histogram(np.array(self.buffer),bins=4096)[0]
        self.original = list(self.buffer)
        #self.original = self.original*1.005

    def update_plot(self):
        if self.on_collection == False:
            return
        
        rate = int(len(self.original)/1024)
        if self.expand_option == "Original":
            self.binned = self.original
            pass
        if self.expand_option == "Interval":
            length = len(self.original)
            self.binned = self.original[0:length:rate]
        elif self.expand_option == "Max":
            self.binned = block_reduce(self.original,(rate,),np.max)
            pass
        elif self.expand_option == "Mean":
            self.binned = block_reduce(self.original,(rate,),np.mean)
        

        if self.plot_option == "Line":
            #self.graph.clear()
            #self.curve1 = self.graph.plot(self.binned)
            #self.divided_graph = CurveWidget(parent=None)
            #print("Line show")
            self.divided_graph_curve.display_data_curve(self.binned)
        
        elif self.plot_option == "Scatter":
            y = self.binned
            x = np.array(range(0,len(self.binned)))
            #self.divided_graph = ScatterWidget(parent=None)
            #self.graph.clear()
            #self.curve2 = self.graph.plot(y,x,pen=None,symbol="o")
            #print("Scatter show")
            self.divided_graph_scatter.display_data_scatter(x,y)

    def calculate_peak_area(self):
        min_x,max_x = self.divided_graph_curve.region.getRegion()
        area = sum(self.binned[int(min_x):int(max_x)] - min(self.binned[int(min_x):int(max_x)]))
        self.peak_area.display(area)

    def calculate_integral(self):
        min_x,max_x = self.divided_graph_curve.region.getRegion()
        area = sum(self.binned[int(min_x):int(max_x)])
        self.integral.display(area)
    
    def calculate_half_wave(self):
        min_x,max_x = self.divided_graph_curve.region.getRegion()
        portion = self.binned[int(min_x):int(max_x)]
        width = signal.peak_widths(self.binned,peaks=[np.argmax(portion)],rel_height=0.6)
        print(width)
        self.half_wave.display(width[2][0])

    def start_collection(self):
        print("Started")
        if self.on_collection:
            return 
        self.on_collection = True
        if self.status == "Pause":
            #self.start_time = time.time()
            print("Resume previous round")
            pass
        elif self.status == "End":
            print("New round")
            self.start_time = time.time()
        self.status = "Start"
        self.timer.start(500)
    
    def pause_collection(self):
        print("Paused")
        self.on_collection = False
        self.end_time = time.time()
        self.status = "Pause"
        self.timer.stop()
    
    def end_collection(self):
        print("Ended")
        self.end_time = 0
        self.start_time = 0
        self.status = "End"
        self.on_collection = False
        self.rawdata = []
        self.original = np.histogram(np.random.normal(size=40960),bins=4096)[0]
        self.timer.stop()
    
    def export_image(self):
        self.pause_collection()
        print("Save picture")
        save_path = self.cur_path_display.text()
        exporter = exporters.ImageExporter(self.divided_graph_curve.main_plotter)

        filename = time.asctime(time.localtime(time.time())).replace(" ","_").replace(":","_")
        #filename = "default"
        exporter.parameters()['width'] = 1000
        exporter.parameters()['height'] = 500
        print("Save to "+save_path + filename + '.png')
        exporter.export(save_path + filename + '.png')

    def new_path(self):
        save_path = QFileDialog.getExistingDirectory(None,"Select your path",self.cur_path_display.text())  
        self.cur_path_display.setText(save_path+"/")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MainWindow()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())