from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_MainForm import Ui_Form
from ExcelHandler import ExcelProcess
from Utils import logger
import sys

class MainForm(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)

        self.filePath = None
        self.outputPath = None
        self.colCountStr= None
        self.colCount = None
        self.colToOutputStr = None
        self.colToOutput = None


    def selectModuleFile(self):
        logger.info("selectModuleFile is called!")
        fName = QtWidgets.QFileDialog.getOpenFileName(self, "打开文件", "./", ("ExcelFile *.xls *.xlsx"))
        if fName[0]:
            self.filePath = fName[0]
            mainMenu.lineEdit_ModulePath.setText(self.filePath)

    def selectOutputPath(self):
        logger.info("myCustomEvent is called!")
        self.outputPath = QtWidgets.QFileDialog.getExistingDirectory(self, "选择输出文件目录")
        if len(self.outputPath) > 0:
            mainMenu.lineEdit_outPutPath.setText(self.outputPath)
        else:
            logger.warning("output directory is null ...")
            mainMenu.lineEdit_outPutPath.clear()

    def colCountTextChanged(self):
        self.colCountStr = mainMenu.lineEdit_colCount.text()
        logger.info("colCountTextChanged is called and text:%s", self.colCountStr)

    def colToOutputTextChanged(self):
        self.colToOutputStr = mainMenu.lineEdit_colToOutput.text()
        logger.info("colToOutputTextChanged is called and text:%s", self.colToOutputStr)

    def goToOutput(self):
        logger.info("goToOutput is called!")
        if(self.checkInputVaild()):
            logger.info("所有填写的数据都合法，可以继续执行程序")
            excelProcess = ExcelProcess()
            excelProcess.ReadExcel(self.filePath)
            excelProcess.InitKeyValueData()
            excelProcess.InitKeyContainedLists()
            excelProcess.SearchContent(self.colCount, self.colToOutput, self.outputPath)

    def checkInputVaild(self):

        logger.info("start checkinput ...")

        if not (self.filePath and len(self.filePath) > 0):
            msgBox = QtWidgets.QMessageBox(self)
            msgBox.about(self, "提示", "请选择模板文件")
            return False

        if not (self.outputPath and len(self.outputPath) > 0):
            msgBox = QtWidgets.QMessageBox(self)
            msgBox.about(self, "提示", "请选择输出文件的目录")
            return False

        if self.colCountStr and self.colCountStr.isdigit():
            self.colCount = int(self.colCountStr)
        else:
            msgBox = QtWidgets.QMessageBox(self)
            msgBox.about(self, "提示", "请输入正确的列数")
            return False

        if self.colToOutputStr and self.colToOutputStr.isdigit():
            self.colToOutput = int(self.colToOutputStr)
        else:
            msgBox = QtWidgets.QMessageBox(self)
            msgBox.about(self, "提示", "请输入正确的列号")
            return False

        return True


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainMenu=MainForm()
    mainMenu.show()

    # logging.basicConfig(filename="Log.txt", filemode="w", level=logging.DEBUG, format="%(asctime)s[%(thread)d] %(levelname)s %(pathname)s[:%(lineno)d] %(message)s")

    logger.info("显示处理窗口")

    #选择模板文件按钮
    mainMenu.pushButton_SelectModule.clicked.connect(mainMenu.selectModuleFile)

    #选择目标文件按钮
    mainMenu.pushButton_selectOutput.clicked.connect(mainMenu.selectOutputPath)

    #填写需要遍历的列的数目
    mainMenu.lineEdit_colCount.textChanged.connect(mainMenu.colCountTextChanged)

    #填写需要生成的列的数值
    mainMenu.lineEdit_colToOutput.textChanged.connect(mainMenu.colToOutputTextChanged)

    # 执行按钮
    mainMenu.go.clicked.connect(mainMenu.goToOutput)
    sys.exit(app.exec_())