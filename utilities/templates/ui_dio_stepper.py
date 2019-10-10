# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dio_stepper.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 326)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setAutoRepeat(True)
        self.pushButton_5.setAutoRepeatInterval(20)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setAutoRepeatInterval(20)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.monitors = QtWidgets.QStackedWidget(Dialog)
        self.monitors.setObjectName("monitors")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gaugeLayout = QtWidgets.QHBoxLayout(self.page_1)
        self.gaugeLayout.setContentsMargins(5, 5, 5, 5)
        self.gaugeLayout.setObjectName("gaugeLayout")
        self.monitors.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graph = PlotWidget(self.page_2)
        self.graph.setObjectName("graph")
        self.horizontalLayout_3.addWidget(self.graph)
        self.monitors.addWidget(self.page_2)
        self.gridLayout.addWidget(self.monitors, 3, 0, 1, 6)
        self.currentPositionBox = QtWidgets.QSpinBox(Dialog)
        self.currentPositionBox.setMinimum(-10000)
        self.currentPositionBox.setMaximum(10000)
        self.currentPositionBox.setObjectName("currentPositionBox")
        self.gridLayout.addWidget(self.currentPositionBox, 0, 4, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/control/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/control/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.gridLayout.addWidget(self.frame, 0, 6, 6, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 4, 3, 1, 1)
        self.pinSet = QtWidgets.QComboBox(Dialog)
        self.pinSet.setFrame(True)
        self.pinSet.setObjectName("pinSet")
        self.pinSet.addItem("")
        self.pinSet.addItem("")
        self.gridLayout.addWidget(self.pinSet, 4, 0, 1, 3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 4, 1, 2)
        self.configLayout = QtWidgets.QHBoxLayout()
        self.configLayout.setObjectName("configLayout")
        self.gridLayout.addLayout(self.configLayout, 2, 0, 1, 6)

        self.retranslateUi(Dialog)
        self.monitors.setCurrentIndex(0)
        self.pushButton_3.clicked.connect(Dialog.add)
        self.pushButton_4.clicked.connect(Dialog.play)
        self.pushButton.clicked.connect(Dialog.initialize)
        self.pushButton_2.clicked.connect(Dialog.stepLeft)
        self.pushButton_5.clicked.connect(Dialog.stepRight)
        self.currentPositionBox.editingFinished.connect(Dialog.stepTo)
        self.pinSet.currentIndexChanged['int'].connect(Dialog.setPins)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_5.setText(_translate("Dialog", ">"))
        self.pushButton_2.setText(_translate("Dialog", "<"))
        self.pushButton.setText(_translate("Dialog", "HOME"))
        self.pinSet.setItemText(0, _translate("Dialog", "A+ : PB0, B + PB1, A- : PB2, B- : PB3"))
        self.pinSet.setItemText(1, _translate("Dialog", "PB4,PB5,PB6,PB7"))
        self.label.setText(_translate("Dialog", "Steps per full revolution"))

from pyqtgraph import PlotWidget
from . import res_rc