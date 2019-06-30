# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(931, 580)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableView, 5, 0, 1, 6)
        self.de_end = QtWidgets.QDateEdit(Form)
        self.de_end.setObjectName("de_end")
        self.gridLayout.addWidget(self.de_end, 1, 4, 1, 1)
        self.de_start = QtWidgets.QDateEdit(Form)
        self.de_start.setObjectName("de_start")
        self.gridLayout.addWidget(self.de_start, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 1, 1, 5)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.le_yzm = QtWidgets.QLineEdit(Form)
        self.le_yzm.setObjectName("le_yzm")
        self.gridLayout.addWidget(self.le_yzm, 0, 4, 1, 1)
        self.le_blh = QtWidgets.QLineEdit(Form)
        self.le_blh.setObjectName("le_blh")
        self.gridLayout.addWidget(self.le_blh, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_blh, self.le_yzm)
        Form.setTabOrder(self.le_yzm, self.tableView)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "住院病人错误项目删除工具"))
        self.label_5.setText(_translate("Form", "    至"))
        self.label.setText(_translate("Form", " 病历号："))
        self.label_2.setText(_translate("Form", " 项目名称："))
        self.label_3.setText(_translate("Form", "  进度："))
        self.label_4.setText(_translate("Form", "入账时间："))
        self.checkBox.setText(_translate("Form", "按日期查"))
        self.pushButton.setText(_translate("Form", "查询"))

