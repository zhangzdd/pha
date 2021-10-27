import sys
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.lrg = pg.LinearRegionItem()
        self.graphWidget.addItem(self.lrg)


        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        self.graphWidget.plot(hour, temperature)
        
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.label = pg.TextItem(text="Abscissa: {} \nOrdinate: {}".format(0, 0))
        self.graphWidget.addItem(self.label)
        
        self.setMouseTracking(True)
        self.graphWidget.scene().sigMouseMoved.connect(self.onMouseMoved)
        self.crosshair_v = pg.InfiniteLine(angle=90, movable=False)
        self.crosshair_h = pg.InfiniteLine(angle=0, movable=False)
        self.graphWidget.addItem(self.crosshair_v, ignoreBounds=True)
        self.graphWidget.addItem(self.crosshair_h, ignoreBounds=True)

        self.proxy = pg.SignalProxy(self.graphWidget.scene().sigMouseMoved, rateLimit=60, slot=self.update_crosshair)

    def update_crosshair(self, e):
        pos = e[0]
        if self.graphWidget.sceneBoundingRect().contains(pos):
            mousePoint = self.graphWidget.getPlotItem().vb.mapSceneToView(pos)
            self.crosshair_v.setPos(mousePoint.x())
            self.crosshair_h.setPos(mousePoint.y())

    def onMouseMoved(self, evt):
        if self.graphWidget.plotItem.vb.mapSceneToView(evt):
            point =self.graphWidget.plotItem.vb.mapSceneToView(evt)
            self.label.setHtml(
                "<p style='color:white'>Abscissa： {0} <br> Ordinate: {1}</p>".\
                format(point.x(), point.y()))
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()