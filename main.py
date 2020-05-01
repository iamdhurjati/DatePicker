# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import reources

# ------------class for weekend color and round selected date---------





class Ui_MainWindow(QtWidgets.QCalendarWidget):
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_4.setStyleSheet("\n"
"QDateEdit\n"
"{border-radius: 4px;\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    width:130px;\n"
"    height:23px;\n"
"   \n"
"    color: rgb(127, 127, 127);\n"
"    border-color: rgb(135, 207, 255);\n"
"    spacing: 5px; \n"
"}\n"
"\n"
"QDateEdit::drop-down {  \n"
"image: url(:/newPrefix/calendar.svg);\n"
"    width:25px;\n"
"    height:23px;\n"
"subcontrol-position: right top;\n"
"    subcontrol-origin:margin;\n"
"     background-color:  rgb(135, 207, 255);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
" border-radius: 1px;\n"
"   spacing: 5px; \n"
"\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"background-color:  rgb(135, 207, 255);\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"background-color:  rgb(135, 207, 255);\n"
"color: white;\n"
"icon-size: 20px;\n"
"\n"
"      font-size: 11px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu{\n"
"background-color: rgb(96, 175, 204);\n"
"color: white;\n"
"\n"
"\n"
"}\n"
"\n"
"  /* header row */\n"
" QCalendarWidget QWidget {alternate-background-color: rgb(250, 250, 250);  }\n"
"\n"
"/*normmal days*/\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"    color: rgb(115, 115, 115);\n"
"\n"
"  }\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QCalendarWidget QMenu{\n"
"background-color:  rgb(135, 207, 255);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox{\n"
" background-color:  rgb(135, 207, 255);\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QTableView{\n"
"background-color: rgb(250, 250, 250);\n"
"selection-background-color:  rgb(135, 207, 255);\n"
"\n"
"font-size: 12px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"  \n"
"    icon-size: 15px;\n"
"    qproperty-icon: url(:/newPrefix/left.svg);\n"
"\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    \n"
"    icon-size: 15px;\n"
"    qproperty-icon:   url(:/newPrefix/right.svg);\n"
"}\n"
"")
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_2.addWidget(self.dateEdit_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateEdit_4.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
