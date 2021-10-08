import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from Ui_frame import Ui_MainWindow
#from settings import setting
from matplotlib.widgets import Cursor
import sys
import os
import matplotlib
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QFileDialog
import pyqtgraph as pg
import random
import numpy as np
import pandas as pd

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.collection_settings_save.clicked.connect(self.collections_setting_func)
        self.graph = pg.PlotWidget(self)
        self.gridLayout.addWidget(self.graph)
        self.rawdata = []
        #self.binned = np.zeros(1024)
        self.binned = np.histogram(np.random.normal(size=10240),bins=1024)[0]
        
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
        self.timer.start(1000)

        self.plot_option = self.plot_method.currentText()
        self.display_setting_save.clicked.connect(self.display_setting_func)

    def display_setting_func(self):
        self.plot_option = self.plot_method.currentText()


    def collections_setting_func(self):
        print(self.collection_source.currentText())
        print("Collection settings saved")
        self.source = self.collection_source.currentText()
        
        
        #调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        Icon = QtGui.QPixmap('C:/Users/ZDD/Desktop/核数据处理/pha/new_design/templates/'+self.source+".jpeg")
        # 在disp里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.disp.setPixmap(Icon)
        self.disp.setScaledContents(True)
        pass
    
    def link(self):
        print(os.getcwd())
        Icon = QtGui.QPixmap("C:/Users/ZDD/Desktop/核数据处理/pha/new_design/templates/connected.jpeg")
        self.connection_disp.setPixmap(Icon)
        self.connection_disp.setScaledContents(True)

    def cut(self):
        Icon = QtGui.QPixmap("C:/Users/ZDD/Desktop/核数据处理/pha/new_design/templates/disconnected.jpeg")
        self.connection_disp.setPixmap(Icon)
        self.connection_disp.setScaledContents(True)

    def update_data(self):
        if self.on_collection == False:
            return 
        """
        new_income = np.random.randn()
        self.rawdata.append(new_income)
        self.binned = np.histogram(np.array(self.rawdata),bins=1024)[0]
        """
        self.binned = self.binned*1.005

    def update_plot(self):
        if self.on_collection == False:
            return
        if self.plot_option == "Line":
            self.graph.clear()
            self.curve1 = self.graph.plot(self.binned)
        elif self.plot_option == "Scatter":
            x = self.binned
            y = np.array(range(0,1024))

            self.graph.clear()
            self.curve2 = self.graph.plot(y,x,pen=None,symbol="o")


    def start_collection(self):
        print("Started")
        self.on_collection = True

        self.timer.start()
    
    def pause_collection(self):
        print("Paused")
        self.on_collection = False
        self.timer.stop()
    
    def end_collection(self):
        print("Ended")
        self.on_collection = False
        self.rawdata = []
        self.binned = np.zeros(1024)
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