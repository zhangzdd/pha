# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ZDD\Desktop\核数据处理\pha\new_design\frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 261, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.collection_source = QtWidgets.QComboBox(self.widget)
        self.collection_source.setGeometry(QtCore.QRect(130, 20, 91, 21))
        self.collection_source.setObjectName("collection_source")
        self.collection_source.addItem("")
        self.collection_source.addItem("")
        self.collection_source.addItem("")
        self.collection_settings_save = QtWidgets.QPushButton(self.widget)
        self.collection_settings_save.setGeometry(QtCore.QRect(90, 470, 75, 23))
        self.collection_settings_save.setObjectName("collection_settings_save")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(53, 20, 61, 21))
        self.label.setObjectName("label")
        self.count_time_option = QtWidgets.QRadioButton(self.widget)
        self.count_time_option.setGeometry(QtCore.QRect(130, 320, 89, 16))
        self.count_time_option.setChecked(True)
        self.count_time_option.setObjectName("count_time_option")
        self.total_count_option = QtWidgets.QRadioButton(self.widget)
        self.total_count_option.setGeometry(QtCore.QRect(130, 360, 89, 16))
        self.total_count_option.setObjectName("total_count_option")
        self.count_time_setting = QtWidgets.QLineEdit(self.widget)
        self.count_time_setting.setGeometry(QtCore.QRect(120, 340, 113, 20))
        self.count_time_setting.setObjectName("count_time_setting")
        self.tota_count_setting = QtWidgets.QLineEdit(self.widget)
        self.tota_count_setting.setGeometry(QtCore.QRect(120, 380, 113, 20))
        self.tota_count_setting.setObjectName("tota_count_setting")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 360, 71, 21))
        self.label_2.setObjectName("label_2")
        self.link_source = QtWidgets.QPushButton(self.widget)
        self.link_source.setGeometry(QtCore.QRect(30, 60, 81, 31))
        self.link_source.setObjectName("link_source")
        self.cut_source = QtWidgets.QPushButton(self.widget)
        self.cut_source.setGeometry(QtCore.QRect(144, 60, 81, 31))
        self.cut_source.setObjectName("cut_source")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 290, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(80, 110, 81, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.connection_icon_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.connection_icon_layout.setContentsMargins(0, 0, 0, 0)
        self.connection_icon_layout.setObjectName("connection_icon_layout")
        self.ip_addr_input = QtWidgets.QLineEdit(self.widget)
        self.ip_addr_input.setGeometry(QtCore.QRect(100, 220, 113, 20))
        self.ip_addr_input.setObjectName("ip_addr_input")
        self.port_input = QtWidgets.QLineEdit(self.widget)
        self.port_input.setGeometry(QtCore.QRect(100, 250, 113, 20))
        self.port_input.setObjectName("port_input")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(30, 220, 61, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(30, 250, 61, 21))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 41, 31))
        self.label_4.setObjectName("label_4")
        self.count_range = QtWidgets.QLineEdit(self.tab_2)
        self.count_range.setGeometry(QtCore.QRect(110, 29, 81, 31))
        self.count_range.setObjectName("count_range")
        self.lower_bound = QtWidgets.QLineEdit(self.tab_2)
        self.lower_bound.setGeometry(QtCore.QRect(60, 80, 81, 31))
        self.lower_bound.setObjectName("lower_bound")
        self.upper_bound = QtWidgets.QLineEdit(self.tab_2)
        self.upper_bound.setGeometry(QtCore.QRect(170, 80, 81, 31))
        self.upper_bound.setObjectName("upper_bound")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 79, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(150, 85, 20, 21))
        self.label_6.setObjectName("label_6")
        self.display_setting_save = QtWidgets.QPushButton(self.tab_2)
        self.display_setting_save.setGeometry(QtCore.QRect(90, 470, 75, 23))
        self.display_setting_save.setObjectName("display_setting_save")
        self.plot_method = QtWidgets.QComboBox(self.tab_2)
        self.plot_method.setGeometry(QtCore.QRect(138, 150, 71, 31))
        self.plot_method.setObjectName("plot_method")
        self.plot_method.addItem("")
        self.plot_method.addItem("")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 150, 91, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 71, 31))
        self.label_10.setObjectName("label_10")
        self.curve_expansion = QtWidgets.QComboBox(self.tab_2)
        self.curve_expansion.setGeometry(QtCore.QRect(140, 200, 71, 31))
        self.curve_expansion.setObjectName("curve_expansion")
        self.curve_expansion.addItem("")
        self.curve_expansion.addItem("")
        self.curve_expansion.addItem("")
        self.curve_expansion.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 250, 91, 31))
        self.label_13.setObjectName("label_13")
        self.curve_color = QtWidgets.QComboBox(self.tab_2)
        self.curve_color.setGeometry(QtCore.QRect(140, 250, 71, 31))
        self.curve_color.setObjectName("curve_color")
        self.curve_color.addItem("")
        self.curve_color.addItem("")
        self.curve_color.addItem("")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 300, 91, 31))
        self.label_15.setObjectName("label_15")
        self.log_count = QtWidgets.QComboBox(self.tab_2)
        self.log_count.setGeometry(QtCore.QRect(140, 300, 71, 31))
        self.log_count.setObjectName("log_count")
        self.log_count.addItem("")
        self.log_count.addItem("")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 360, 91, 31))
        self.label_20.setObjectName("label_20")
        self.set_path = QtWidgets.QPushButton(self.tab_2)
        self.set_path.setGeometry(QtCore.QRect(140, 360, 75, 31))
        self.set_path.setObjectName("set_path")
        self.cur_path_display = QtWidgets.QLineEdit(self.tab_2)
        self.cur_path_display.setGeometry(QtCore.QRect(30, 410, 181, 20))
        self.cur_path_display.setReadOnly(True)
        self.cur_path_display.setObjectName("cur_path_display")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 41, 31))
        self.label_3.setObjectName("label_3")
        self.time_elapsed = QtWidgets.QLCDNumber(self.tab)
        self.time_elapsed.setGeometry(QtCore.QRect(120, 82, 101, 41))
        self.time_elapsed.setObjectName("time_elapsed")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 51, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(40, 160, 54, 12))
        self.label_8.setObjectName("label_8")
        self.total_count = QtWidgets.QLCDNumber(self.tab)
        self.total_count.setGeometry(QtCore.QRect(120, 150, 101, 41))
        self.total_count.setObjectName("total_count")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(120, 10, 71, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.collection_setting_display = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.collection_setting_display.setContentsMargins(0, 0, 0, 0)
        self.collection_setting_display.setObjectName("collection_setting_display")
        self.finished_percentage = QtWidgets.QProgressBar(self.tab)
        self.finished_percentage.setGeometry(QtCore.QRect(120, 210, 118, 23))
        self.finished_percentage.setProperty("value", 24)
        self.finished_percentage.setObjectName("finished_percentage")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 200, 81, 41))
        self.label_14.setObjectName("label_14")
        self.peak_area = QtWidgets.QLCDNumber(self.tab)
        self.peak_area.setGeometry(QtCore.QRect(120, 312, 101, 41))
        self.peak_area.setObjectName("peak_area")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(40, 310, 51, 41))
        self.label_16.setObjectName("label_16")
        self.half_wave = QtWidgets.QLCDNumber(self.tab)
        self.half_wave.setGeometry(QtCore.QRect(120, 362, 101, 41))
        self.half_wave.setObjectName("half_wave")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(40, 360, 51, 41))
        self.label_17.setObjectName("label_17")
        self.integral = QtWidgets.QLCDNumber(self.tab)
        self.integral.setGeometry(QtCore.QRect(120, 412, 101, 41))
        self.integral.setObjectName("integral")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(40, 410, 51, 41))
        self.label_18.setObjectName("label_18")
        self.count_rate = QtWidgets.QLCDNumber(self.tab)
        self.count_rate.setGeometry(QtCore.QRect(120, 252, 101, 41))
        self.count_rate.setObjectName("count_rate")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(30, 250, 61, 41))
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 20, 821, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.start_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(310, 510, 101, 41))
        self.start_button.setObjectName("start_button")
        self.pause_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(500, 510, 101, 41))
        self.pause_button.setObjectName("pause_button")
        self.end_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.end_button.setGeometry(QtCore.QRect(700, 510, 101, 41))
        self.end_button.setObjectName("end_button")
        self.export_spectrum = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.export_spectrum.setGeometry(QtCore.QRect(890, 510, 101, 41))
        self.export_spectrum.setObjectName("export_spectrum")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.collection_source.setItemText(0, _translate("MainWindow", "Simulation"))
        self.collection_source.setItemText(1, _translate("MainWindow", "USB"))
        self.collection_source.setItemText(2, _translate("MainWindow", "Socket"))
        self.collection_settings_save.setText(_translate("MainWindow", "保存设置"))
        self.label.setText(_translate("MainWindow", "采集源"))
        self.count_time_option.setText(_translate("MainWindow", "计数时间"))
        self.total_count_option.setText(_translate("MainWindow", "道计数"))
        self.count_time_setting.setText(_translate("MainWindow", "30"))
        self.tota_count_setting.setText(_translate("MainWindow", "100000000"))
        self.label_2.setText(_translate("MainWindow", "采集终止标准"))
        self.link_source.setText(_translate("MainWindow", "连接采集源"))
        self.cut_source.setText(_translate("MainWindow", "断开采集源"))
        self.ip_addr_input.setText(_translate("MainWindow", "127.0.0.1"))
        self.port_input.setText(_translate("MainWindow", "6688"))
        self.label_11.setText(_translate("MainWindow", "IP地址"))
        self.label_12.setText(_translate("MainWindow", "端口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "采集设置"))
        self.label_4.setText(_translate("MainWindow", "量程"))
        self.count_range.setText(_translate("MainWindow", "1000000"))
        self.lower_bound.setText(_translate("MainWindow", "0"))
        self.upper_bound.setText(_translate("MainWindow", "1024"))
        self.label_5.setText(_translate("MainWindow", "局部谱"))
        self.label_6.setText(_translate("MainWindow", "到"))
        self.display_setting_save.setText(_translate("MainWindow", "提交设置"))
        self.plot_method.setItemText(0, _translate("MainWindow", "Line"))
        self.plot_method.setItemText(1, _translate("MainWindow", "Scatter"))
        self.label_9.setText(_translate("MainWindow", "曲线绘制方式"))
        self.label_10.setText(_translate("MainWindow", "曲线扩展方式"))
        self.curve_expansion.setItemText(0, _translate("MainWindow", "Original"))
        self.curve_expansion.setItemText(1, _translate("MainWindow", "Interval"))
        self.curve_expansion.setItemText(2, _translate("MainWindow", "Max"))
        self.curve_expansion.setItemText(3, _translate("MainWindow", "Mean"))
        self.label_13.setText(_translate("MainWindow", "曲线颜色"))
        self.curve_color.setItemText(0, _translate("MainWindow", "Blue"))
        self.curve_color.setItemText(1, _translate("MainWindow", "Green"))
        self.curve_color.setItemText(2, _translate("MainWindow", "Red"))
        self.label_15.setText(_translate("MainWindow", "是否对数显示"))
        self.log_count.setItemText(0, _translate("MainWindow", "Yes"))
        self.log_count.setItemText(1, _translate("MainWindow", "No"))
        self.label_20.setText(_translate("MainWindow", "存储路径设置"))
        self.set_path.setText(_translate("MainWindow", "设置"))
        self.cur_path_display.setText(_translate("MainWindow", "./output/"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "显示设置"))
        self.label_3.setText(_translate("MainWindow", "采集源"))
        self.label_7.setText(_translate("MainWindow", "采集时间"))
        self.label_8.setText(_translate("MainWindow", "总计数"))
        self.label_14.setText(_translate("MainWindow", "采集完成进度"))
        self.label_16.setText(_translate("MainWindow", "峰面积"))
        self.label_17.setText(_translate("MainWindow", "半高宽"))
        self.label_18.setText(_translate("MainWindow", "积分"))
        self.label_19.setText(_translate("MainWindow", "计数率(/s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "当前信息"))
        self.start_button.setText(_translate("MainWindow", "开始采集"))
        self.pause_button.setText(_translate("MainWindow", "暂停采集"))
        self.end_button.setText(_translate("MainWindow", "结束采集"))
        self.export_spectrum.setText(_translate("MainWindow", "导出能谱"))
