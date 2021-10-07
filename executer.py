import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from ui import Ui_MainWindow
from settings import setting
from matplotlib.widgets import Cursor
import sys
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QFileDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import random
import numpy as np
import pandas as pd


class MyMplCanvas(FigureCanvas):  # 画布基类
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=50, height=50, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):  # 单个画布

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self,backEnddata,conveySet):
        # 构建4个随机整数，位于闭区间[0, 10]
        #l = [random.randint(0, 10) for i in range(4)]
        set = conveySet
        eRange = set.eRange
        measureRange = set.measureRange
        self.axes.cla()
        self.axes.set_xlim(eRange[0],eRange[1])
        self.axes.set_ylim(0,measureRange)

        self.cursor = Cursor(self.axes, horizOn = False ,useblit=True, color='red', linewidth=1)

        self.binned = np.bincount(backEnddata,minlength=1024)
        #self.axes.hist(backEnddata,bins = 100,rwidth = 0.1)
        #self.axes.bar([i fo i in range(0,1024)],self.binned)
        x = [i for i in range(0,1024)]
        self.axes.plot(x,list(self.binned))
        self.axes.set_xlabel('channel')
        self.axes.set_ylabel('count')
        self.draw()


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.set = setting()
        self.globalClock = 0
        self.OnSim = False
        self.endSignal = False
        self.pushButton_2.clicked.connect(self.show_graph)
        self.backEnddata = []
        self.timer = QtCore.QTimer()#总计时器
        self.countTotal = 0


        #To connect the setiing on the UI with the background settings
        #Pushing of buttons shall trigger a change in the setting
        self.pushButton_7.clicked.connect(self.change_basic)
        self.pushButton.clicked.connect(self.change_channel)
        self.pushButton_8.clicked.connect(self.change_display)
        self.pushButton_3.clicked.connect(self.startSimulation)
        self.pushButton_4.clicked.connect(self.endSimulation)
        #Connect the button with the simulation settings
        self.dc = MyDynamicMplCanvas(width=5, height=4, dpi=100)
        self.gridLayout.addWidget(self.dc)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(self.dc, self))

        self.lcdNumber.display(str(int(self.globalClock)))

        #Connect the button with the clear function
        self.pushButton_5.clicked.connect(self.cla)

        #Connect the button with the search function
        self.pushButton.clicked.connect(self.searchChannel)

        #Connect the button with the show graph function
        self.pushButton_2.clicked.connect(self.show_graph)

        #Connect the file processing button
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFilefiltered)

    def show_graph(self):
        data = self.backEnddata
        self.dc.update_figure(data,self.set)


    def change_basic(self):
        if self.radioButton.isChecked():
            self.set.countTime = int(self.lineEdit.text())
        elif self.radioButton_2.isChecked():
            self.set.countRange = int(self.lineEdit_2.text())
            self.set.channel = int(self.lineEdit_3.text())

    def change_channel(self):
        self.set.searchChannel = int(self.lineEdit_4.text())

    def change_display(self):
        text1 = self.lineEdit_7.text()
        text2 = self.lineEdit_8.text()
        text3 = self.lineEdit_6.text()
        self.set.eRange = [int(text1),int(text2)]
        self.set.measureRange = int(text3)

    def startSimulation(self):
        self.OnSim = True
        self.endSignal = False
        self.timer = QtCore.QTimer()
        if self.radioButton.isChecked():
            conveySet = self.set
            self.timer.start(1000)
            self.timer.timeout.connect(self.backEndUpdate)
            self.timer.timeout.connect(lambda:self.updateFigure("time",conveySet))
        elif self.radioButton_2.isChecked():
            conveySet = self.set
            self.timer.start(1000)
            self.timer.timeout.connect(self.backEndUpdate)
            self.timer.timeout.connect(lambda:self.updateFigure("count",conveySet))
        print(self.timer.isActive())

    def endSimulation(self):
        self.endSignal = True
        self.timer.stop()
        self.OnSim = False
        print(self.timer.isActive())

    def updateFigure(self,simType,coefficient):
        set = coefficient
        if simType == "count":
            requiredChannel = set.channel
            requiredCount = set.countRange
            if len([i for i in self.backEnddata if i < requiredChannel+1 and i>requiredChannel])>requiredCount:
                self.endSimulation()
                return

        if simType == "time":
            requiredTime = self.set.countTime
            if self.globalClock>requiredTime:
                self.endSimulation()
                return

        binned = np.bincount(self.backEnddata,minlength=1024)
        searchChannelcount = binned[self.set.searchChannel]
        self.lineEdit_5.setText(str(searchChannelcount))
        self.dc.update_figure(self.backEnddata,set)
        self.lcdNumber.display(self.globalClock)
        self.globalClock += 1

        pass

    def backEndUpdate(self):
        for i in range(0,10):
            rand = int(random.normalvariate(500,200))
            if rand < 0 or rand>1020:
                rand = 500
            self.backEnddata.append(rand)
        self.countTotal = len(self.backEnddata)
        self.lineEdit_11.setText(str(self.countTotal))
        #print(self.backEnddata)


    def cla(self):
        if self.OnSim:
            self.endSimulation()
        self.OnSim = False
        self.backEnddata = []
        self.globalClock = 0
        self.lcdNumber.display(self.globalClock)
        self.countTotal = 0
        self.lineEdit_11.setText(str(self.countTotal))

    def searchChannel(self):
        self.set.searchChannel = int(self.lineEdit_4.text())

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self,"Select File")
        print(filename)
        if not filename:
            return
        self.lineEdit_9.setText(filename)
        self.set.csvDir = filename
        direc = self.set.csvDir
        csv = pd.read_csv(direc)
        self.backEnddata = csv["energy"]

    def saveFilefiltered(self):
        fileName2, _ = QFileDialog.getSaveFileName(self, "Save File","filtered.csv")
        direc_dict = {"energy": [i for i in range(0,1024)],"count":np.bincount(self.backEnddata,minlength=1024)}
        if fileName2:
            df = pd.DataFrame(direc_dict)
            df.to_csv(fileName2)
        pass

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())