# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.setObjectName("editor")
        self.verticalLayout.addWidget(self.editor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(self.menuView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTheme.setIcon(icon)
        self.menuTheme.setObjectName("menuTheme")
        self.menuZoom = QtWidgets.QMenu(self.menuView)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuZoom.setIcon(icon1)
        self.menuZoom.setObjectName("menuZoom")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/collapse-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/Icons/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon5)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/Icons/close-red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/Icons/question-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMore = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/Icons/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMore.setIcon(icon8)
        self.actionMore.setObjectName("actionMore")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/Icons/all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_All.setIcon(icon9)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionDate_And_Time = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icons/Icons/time-clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDate_And_Time.setIcon(icon10)
        self.actionDate_And_Time.setObjectName("actionDate_And_Time")
        self.actionDay = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icons/Icons/calendar-date-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDay.setIcon(icon11)
        self.actionDay.setObjectName("actionDay")
        self.actionInsert_Images = QtWidgets.QAction(MainWindow)
        self.actionInsert_Images.setObjectName("actionInsert_Images")
        self.actionLight_Defualt = QtWidgets.QAction(MainWindow)
        self.actionLight_Defualt.setObjectName("actionLight_Defualt")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionCustom_Theme = QtWidgets.QAction(MainWindow)
        self.actionCustom_Theme.setObjectName("actionCustom_Theme")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionMore)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDay)
        self.menuEdit.addAction(self.actionDate_And_Time)
        self.menuTheme.addAction(self.actionLight_Defualt)
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addSeparator()
        self.menuTheme.addAction(self.actionCustom_Theme)
        self.menuZoom.addAction(self.actionZoom_In)
        self.menuZoom.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuView.addAction(self.menuZoom.menuAction())
        self.menuView.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionMore.setText(_translate("MainWindow", "More"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionDate_And_Time.setText(_translate("MainWindow", "Date/Time"))
        self.actionDay.setText(_translate("MainWindow", "Day"))
        self.actionInsert_Images.setText(_translate("MainWindow", "Insert Images"))
        self.actionLight_Defualt.setText(_translate("MainWindow", "Light (Default)"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionCustom_Theme.setText(_translate("MainWindow", "Custom Theme"))

