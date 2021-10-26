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
import numpy as np
from skimage.measure import block_reduce
from client import receiver
from threading import Thread
import time


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
        self.graph = pg.PlotWidget(self)
        self.gridLayout.addWidget(self.graph)
        self.rawdata = []
        #self.binned = np.zeros(1024)
        self.buffer = []
        self.original = np.histogram(np.random.normal(size=40960),bins=4096)[0]
        self.binned = self.original.copy()
        
        self.start_button.clicked.connect(self.start_collection)
        self.pause_button.clicked.connect(self.pause_collection)
        self.end_button.clicked.connect(self.end_collection)
        self.on_collection = False
        
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

        self.plot_option = self.plot_method.currentText()
        self.expand_option = "Original"
        self.display_setting_save.clicked.connect(self.display_setting_func)

        #self.receiver_agent = receiver("127.0.0.1",6688,1024)

        qssStyle = CommonHelper.readQss("qss/MacOS.qss")
        self.setStyleSheet(qssStyle)
        

    def display_setting_func(self):
        self.plot_option = self.plot_method.currentText()
        self.expand_option = self.curve_expansion.currentText()


    def collections_setting_func(self):
        print(self.collection_source.currentText())
        print("Collection settings saved")
        self.source = self.collection_source.currentText()
        
        
        #调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        Icon = QtGui.QPixmap(sys.path[0]+'/templates/'+self.source+".jpeg")
        # 在disp里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.disp.setPixmap(Icon)
        self.disp.setScaledContents(True)
        pass
    
    def link(self):
        # Collection type: simulation
        if self.source == "Simulation":
            Icon = QtGui.QPixmap(sys.path[0]+"/templates/connected.jpeg")
            self.connection_disp.setPixmap(Icon)
            self.connection_disp.setScaledContents(True)
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
        if self.on_collection == False:
            return 
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
        if self.expand_option == "Original":
            self.binned = self.original
            pass
        if self.expand_option == "Interval":
            length = len(self.original)
            self.binned = self.original[0:length:4]
        elif self.expand_option == "Max":
            self.binned = block_reduce(self.original,(4,),np.max)
            pass
        elif self.expand_option == "Mean":
            self.binned = block_reduce(self.original,(4,),np.mean)
        
        if self.plot_option == "Line":
            self.graph.clear()
            self.curve1 = self.graph.plot(self.binned)
        
        elif self.plot_option == "Scatter":
            x = self.binned
            y = np.array(range(0,len(self.binned)))

            self.graph.clear()
            self.curve2 = self.graph.plot(y,x,pen=None,symbol="o")


    def start_collection(self):
        print("Started")
        self.on_collection = True

        self.timer.start(1000)
    
    def pause_collection(self):
        print("Paused")
        self.on_collection = False
        self.timer.stop()
    
    def end_collection(self):
        print("Ended")
        self.on_collection = False
        self.rawdata = []
        self.original = None
        self.timer.stop()


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MainWindow()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())