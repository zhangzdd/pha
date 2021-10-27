"""Add region to the graph and link it with the graph region"""

import dataclasses
from typing import Optional
import sys

import numpy as np
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

SAMPLE_DATA1 = np.random.rand(500) * 10
SAMPLE_DATA2 = 10 + np.random.rand(500) * 10



@dataclasses.dataclass
class CurveWidget(pg.GraphicsLayoutWidget):
    """Main screen
    Attributes #
    ----------
    parent: Optional[QtWidgets.QWidget] default=None
    Parent screen
        main_plotter: pyqtgraph.graphicsItems.PlotItem.PlotItem.PlotItem
    Main graph
        zoom_plotter: pyqtgraph.graphicsItems.PlotItem.PlotItem.PlotItem
        A graph that zooms the main graph in the region
    region: pyqtgraph.graphicsItems.LinearRegionItem.LinearRegionItem
        zoom_region that specifies the x-axis region of the plotter
    """
    parent: Optional[QtWidgets.QWidget] = None

    def __post_init__(self) -> None:
        """Superclass loading and plot,region added"""
        super(CurveWidget, self).__init__(parent=self.parent)
        SAMPLE_DATA3 = 20 + np.random.rand(100) * 10
        self.add_plot()
        self.add_region()
        self.connect_slot()
        self.display_data_curve(SAMPLE_DATA3)

    def add_plot(self) -> None:
        """add plot"""
        self.main_plotter = self.addPlot(row=0, col=0)
        self.main_plotter.showGrid(x=True, y=True, alpha=0.8)
        #main_curve1 = self.main_plotter.plot(pen=pg.mkPen('#f00'))
        #main_curve2 = self.main_plotter.plot(pen=pg.mkPen('#0f0'))
        self.main_curve3 = self.main_plotter.plot(pen=pg.mkPen('#00f'))
        #main_curve1.setData(SAMPLE_DATA1)
        #main_curve2.setData(SAMPLE_DATA2)
        #main_curve3.setData(SAMPLE_DATA3)

        self.zoom_plotter = self.addPlot(row=0, col=1)
        #Adjust the y-axis according to the value
        self.zoom_plotter.setAutoVisible(y=True)
        self.zoom_plotter.showGrid(x=True, y=True, alpha=0.8)
        #zoom_curve1 = self.zoom_plotter.plot(pen=pg.mkPen('#f00'))
        #zoom_curve2 = self.zoom_plotter.plot(pen=pg.mkPen('#0f0'))
        self.zoom_curve3 = self.zoom_plotter.plot(pen=pg.mkPen('#00f'))
        #zoom_curve1.setData(SAMPLE_DATA1)
        #zoom_curve2.setData(SAMPLE_DATA2)
        #zoom_curve3.setData(SAMPLE_DATA3)

        self.zoom_plotter.setXRange(0.0, len(SAMPLE_DATA1) / 8, padding=0)

        self.ci.layout.setColumnStretchFactor(0, 8)
        self.ci.layout.setColumnStretchFactor(1, 5)
        
        self.vLine = pg.InfiniteLine(angle=90, movable=False,pen='#f00')
        #self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.main_plotter.addItem(self.vLine, ignoreBounds=True)
        #self.main_plotter.addItem(self.hLine, ignoreBounds=True)
        self.vb = self.main_plotter.vb
        self.proxy = pg.SignalProxy(self.main_plotter.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        self.label = pg.LabelItem(justify='right', size='20pt',parent=self.main_plotter)
    
    def mouseMoved(self,evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.main_plotter.sceneBoundingRect().contains(pos):
            mousePoint = self.vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            y_data = self.main_curve3.getData()[1]
            x_data = self.main_curve3.getData()[0]
            index = min(len(x_data)-1,index)
            index = max(0,index)
            self.label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (index,y_data[index]))
            
            self.vLine.setPos(index)
            #self.hLine.setPos(mousePoint.y())

        

    def add_region(self) -> None:
        """Add region"""
        self.region = pg.LinearRegionItem()
        #Region height setting. There are multiple regions&If they overlap, the one with the higher Z can be operated.(Since there is only one this time, set it to 10 appropriately)
        self.region.setZValue(10)
        self.main_plotter.addItem(self.region, ignoreBounds=True)
        self.update_region()

    def connect_slot(self) -> None:
        """slot connection"""
        self.region.sigRegionChanged.connect(self.update_zoom_plotter)
        self.zoom_plotter.sigRangeChanged.connect(self.update_region)
    
    def display_data_curve(self,data):
        self.main_curve3.setData(data)
        self.zoom_curve3.setData(data)

    def display_data_scatter(self,x,y):
        self.main_curve3.setData(x,y)
        self.zoom_curve3.setData(x,y)

    @QtCore.pyqtSlot()
    def update_zoom_plotter(self) -> None:
        """self when the region moves.zoom_Change plotter area"""
        self.region.setZValue(10)
        min_x, max_x = self.region.getRegion()
        self.zoom_plotter.setXRange(min_x, max_x, padding=0)

    @QtCore.pyqtSlot()
    def update_region(self) -> None:
        """self.zoom_Change the region of the region when the plotter moves
        viewRange returns the display range of the graph. The type is
        [[Xmin, Xmax], [Ymin, Ymax]]
        """
        rgn = self.zoom_plotter.viewRange()[0]
        self.region.setRegion(rgn)

@dataclasses.dataclass
class ScatterWidget(pg.GraphicsLayoutWidget):
    parent: Optional[QtWidgets.QWidget] = None

    def __post_init__(self) -> None:
        """Superclass loading and plot,region added"""
        super(ScatterWidget, self).__init__(parent=self.parent)
        SAMPLE_DATA3 = 20 + np.random.rand(100) * 10
        self.add_plot()
        self.add_region()
        self.connect_slot()
        self.display_data_scatter(np.array(range(0,len(SAMPLE_DATA3))),SAMPLE_DATA3)

    def add_plot(self) -> None:
        """add plot"""
        self.main_plotter = self.addPlot(row=0, col=0)
        self.main_plotter.showGrid(x=True, y=True, alpha=0.8)
        self.main_curve3 = self.main_plotter.plot(pen=None,symbol = "o")

        self.zoom_plotter = self.addPlot(row=0, col=1)
        #Adjust the y-axis according to the value
        self.zoom_plotter.setAutoVisible(y=True)
        self.zoom_plotter.showGrid(x=True, y=True, alpha=0.8)
        
        self.zoom_curve3 = self.zoom_plotter.plot(pen=None,symbol = "o")

        self.zoom_plotter.setXRange(0.0, len(SAMPLE_DATA1) / 8, padding=0)

        self.ci.layout.setColumnStretchFactor(0, 8)
        self.ci.layout.setColumnStretchFactor(1, 5)
        
        self.vLine = pg.InfiniteLine(angle=90, movable=False,pen='#f00')
        #self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.main_plotter.addItem(self.vLine, ignoreBounds=True)
        #self.main_plotter.addItem(self.hLine, ignoreBounds=True)
        self.vb = self.main_plotter.vb
        self.proxy = pg.SignalProxy(self.main_plotter.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        self.label = pg.LabelItem(justify='right', size='20pt',parent=self.main_plotter)
    
    def mouseMoved(self,evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.main_plotter.sceneBoundingRect().contains(pos):
            mousePoint = self.vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            y_data = self.main_curve3.getData()[1]
            x_data = self.main_curve3.getData()[0]
            index = min(len(x_data)-1,index)
            index = max(0,index)
            self.label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (index,y_data[index]))
            
            self.vLine.setPos(index)
            #self.hLine.setPos(mousePoint.y())
    
    def add_region(self) -> None:
        """Add region"""
        self.region = pg.LinearRegionItem()
        #Region height setting. There are multiple regions&If they overlap, the one with the higher Z can be operated.(Since there is only one this time, set it to 10 appropriately)
        self.region.setZValue(10)
        self.main_plotter.addItem(self.region, ignoreBounds=True)
        self.update_region()

    def connect_slot(self) -> None:
        """slot connection"""
        self.region.sigRegionChanged.connect(self.update_zoom_plotter)
        self.zoom_plotter.sigRangeChanged.connect(self.update_region)
    
    def display_data_curve(self,data):
        self.main_curve3.setData(data)
        self.zoom_curve3.setData(data)

    def display_data_scatter(self,x,y):
        self.main_curve3.setData(x,y)
        self.zoom_curve3.setData(x,y)

    @QtCore.pyqtSlot()
    def update_zoom_plotter(self) -> None:
        """self when the region moves.zoom_Change plotter area"""
        self.region.setZValue(10)
        min_x, max_x = self.region.getRegion()
        self.zoom_plotter.setXRange(min_x, max_x, padding=0)

    @QtCore.pyqtSlot()
    def update_region(self) -> None:
        """self.zoom_Change the region of the region when the plotter moves
        viewRange returns the display range of the graph. The type is
        [[Xmin, Xmax], [Ymin, Ymax]]
        """
        rgn = self.zoom_plotter.viewRange()[0]
        self.region.setRegion(rgn)


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = ScatterWidget(parent=None)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()