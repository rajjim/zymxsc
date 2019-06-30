from view import ui
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QModelIndex
from PyQt5.QtWidgets import QDialog,QMessageBox,QHeaderView,QMenu
class uison(ui.Ui_Form,QDialog):
    def __init__(self,parent=None):
        super(uison, self).__init__(parent)
        self.setupUi(self)
        self.model=QStandardItemModel(0,5)
        self.model.setHorizontalHeaderLabels(['病历号','项目名称','入账时间','项目数量','项目单价'])
        self.addData()
        #自适应大小
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.model)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.tableView.customContextMenuRequested.connect(self.showContextMenu)
        self.pushButton.clicked.connect(self.getText)

    #测试用，添加数据
    def addData(self):
        for row in range(8):
            for column in range(5):
                item = QStandardItem('r %s ,c %s' % (row, column))
                # 设置每个位置的文本值
                self.model.setItem(row, column, item)

    def showContextMenu(self, pos):  # 创建右键菜单
        self.tableView.contextMenu = QMenu(self)
        self.actionA = self.tableView.contextMenu.addAction('删除选中项目')
        self.tableView.contextMenu.popup(QCursor.pos())
        try:
            self.actionA.triggered.connect(self.actionHandler)
            self.tableView.contextMenu.show()
        except Exception as e:
            print(str(e))

    def  removeSelectedRows(self):
        indexs = self.tableView.selectedIndexes()
        count = 0
        selectedRows = []
        for index in indexs:
            if count % 5 == 0:
                selectedRows.append(index.row())
            count += 1
        # 应该倒序，才能正确删除项目。稍微有点绕脑，需要注意
        selectedRows.sort(reverse=True)
        print(selectedRows)
        count = 0
        for row in selectedRows:
            self.model.removeRow(row)
            count += 1
            print(self.model.rowCount())

    #为什么加入判断就没法更新界面了？其实是行的，就是MessageBox的判断条件没搞明白
    def actionHandler(self):
        isDelete=False
        if QMessageBox.question(self,"提示","是否确定删除选中项?",QMessageBox.Yes,QMessageBox.No)==QMessageBox.Yes:
            self.removeSelectedRows()
            print('执行')

    def getText(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        QMessageBox.about(self, "提示：", "您输入的是：" + a + b)