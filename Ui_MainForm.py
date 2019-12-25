# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Work\Python\XlsKeySearch\MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 361)
        self.pushButton_SelectModule = QtWidgets.QPushButton(Form)
        self.pushButton_SelectModule.setGeometry(QtCore.QRect(70, 60, 111, 23))
        self.pushButton_SelectModule.setObjectName("pushButton_SelectModule")
        self.pushButton_selectOutput = QtWidgets.QPushButton(Form)
        self.pushButton_selectOutput.setGeometry(QtCore.QRect(70, 110, 131, 23))
        self.pushButton_selectOutput.setObjectName("pushButton_selectOutput")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 170, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 111, 16))
        self.label_2.setObjectName("label_2")
        self.go = QtWidgets.QPushButton(Form)
        self.go.setGeometry(QtCore.QRect(280, 290, 75, 51))
        self.go.setObjectName("go")
        self.lineEdit_colCount = QtWidgets.QLineEdit(Form)
        self.lineEdit_colCount.setGeometry(QtCore.QRect(230, 170, 113, 20))
        self.lineEdit_colCount.setObjectName("lineEdit_colCount")
        self.lineEdit_ModulePath = QtWidgets.QLineEdit(Form)
        self.lineEdit_ModulePath.setGeometry(QtCore.QRect(230, 60, 331, 20))
        self.lineEdit_ModulePath.setObjectName("lineEdit_ModulePath")
        self.lineEdit_outPutPath = QtWidgets.QLineEdit(Form)
        self.lineEdit_outPutPath.setGeometry(QtCore.QRect(230, 110, 331, 20))
        self.lineEdit_outPutPath.setObjectName("lineEdit_outPutPath")
        self.lineEdit_colToOutput = QtWidgets.QLineEdit(Form)
        self.lineEdit_colToOutput.setGeometry(QtCore.QRect(230, 230, 113, 20))
        self.lineEdit_colToOutput.setObjectName("lineEdit_colToOutput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "XlsKeySearchTool"))
        self.pushButton_SelectModule.setText(_translate("Form", "选择模板文件路径"))
        self.pushButton_selectOutput.setText(_translate("Form", "选择要输出的文件路径"))
        self.label.setText(_translate("Form", "输入需要查找的列数"))
        self.label_2.setText(_translate("Form", "输入要生成的序列号"))
        self.go.setText(_translate("Form", "Go"))
