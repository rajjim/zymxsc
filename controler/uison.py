#本类的作用是控制界面

from view import ui
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QModelIndex
from PyQt5.QtWidgets import QDialog,QMessageBox,QHeaderView,QMenu
from controler import readini
from controler import mssql_helper
import re
import datetime
import decimal
class uison(ui.Ui_Form,QDialog):
    def __init__(self,parent=None):
        super(uison, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./image/hos.ico'))  # 设置窗体图标
        self.model=QStandardItemModel(0,5)
        self.model.setHorizontalHeaderLabels(['病历号','医嘱名','日期','总量','零售价'])
        #self.addData()
        #自适应大小
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.model)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.tableView.customContextMenuRequested.connect(self.showContextMenu)
        self.de_start.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.de_start.setDate(datetime.datetime.now() + datetime.timedelta(days=-1))
        self.de_end.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.de_end.setDate(datetime.datetime.now())
        self.pushButton.clicked.connect(self.getText)
        try:
            self.contentlist=readini.getFileContent('./dz.txt')
            self.helper=mssql_helper.Mssql_helper(self.contentlist[0],self.contentlist[1],self.contentlist[2],self.contentlist[3])
        except Exception as e:
            print(e)
    #测试用，添加数据
    def addData(self):
        for row in range(100):
            for column in range(5):
                item = QStandardItem('r %s ,c %s' % (row, column))
                item.setTextAlignment(Qt.AlignCenter)
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
        #填充待删除数据库语句
        sqllist=[]
        sql=''
        for index in indexs:
            content=self.model.data(index)
            content = str(content)
            if count % 5 == 0:
                sql = 'delete from dbo.zy_dxsf where blh=\''+content+'\' '
                #'病历号','医嘱名','日期','总量','零售价'
            if count % 5==1:
                sql=sql+'and yzm like \'%'+content+'%\' '
            if count %5 ==2:
                sql = sql + 'and sfrq = \'' + content[:-3] + '\' '
            if count %5 ==3:
                sql=sql+'and zl = \''+content+'\' '
            if count %5 ==4:
                sql=sql+'and lsj = \''+content+'\' '
                selectedRows.append(index.row())
                sqllist.append(sql)
            count += 1
        # 应该倒序，才能正确删除项目。稍微有点绕脑，需要注意
        if len(selectedRows)==0:
            QMessageBox.information(self,"提示","想干啥啊，啥都没选呐")
            return
        selectedRows.sort(reverse=True)
        #print(selectedRows)
        print(sqllist)
        count = 0
        for row in selectedRows:
            self.model.removeRow(row)
            count += 1
            print(self.model.rowCount())
        for sql in sqllist:
            msg=self.helper.deleteDate(sql)
            print(msg)


    #为什么加入判断就没法更新界面了？其实是行的，就是MessageBox的判断条件没搞明白
    def actionHandler(self):
        messageBox = QMessageBox()
        messageBox.setWindowIcon(QIcon("./image/hos.ico"))
        messageBox.setIconPixmap(QPixmap("./image/warning.png"))
        messageBox.setWindowTitle('警告：')
        messageBox.setText('是否确定删除选中项?一旦删除，只能让科室重新补了。')
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText('是的，我确定')
        buttonN = messageBox.button(QMessageBox.No)
        buttonN.setText('别删除，我害怕')
        messageBox.exec_()
        if messageBox.clickedButton() == buttonY:
            self.removeSelectedRows()
            print('执行')




    def getText(self):
        #无法得到输入内容？是因为在界面设计时指定了清空事件
        try:
            blh = self.le_blh.text()
            yzm = self.le_yzm.text()
            timeStart = self.de_start.dateTime()
            timeEnd=self.de_end.dateTime()
            timeStart=timeStart.toString("yyyy-MM-dd HH:mm:ss")
            timeEnd = timeEnd.toString("yyyy-MM-dd HH:mm:ss")
            print(timeStart)
            print(timeEnd)
            #必须输入病历号
            if blh.strip()=='':
                QMessageBox.information(self, "提示：", "必须输入病历号，别乱来呀！")
                self.le_blh.setFocus()
                return
            #用正则表达式判断病历号是不是合法的
            pattern=r'^[0-9]{7}$'
            match=re.match(pattern,blh,re.I)
            if match==None:
                QMessageBox.information(self, "提示：", "病历号输入有问题，注意检查下！")
                self.le_blh.setFocus()
                return

            #查询条件分为以下几类
            #1.只查病历号
            #2.查病历号+项目名称
            #3.查病历号+项目名称+时间
            #4.查病历号+时间
            isyzm=False  #默认不用
            istime=self.checkBox.isChecked()
            #默认查询条件为1
            sql = 'select blh,yzm,sfrq,zl,lsj from dbo.zy_dxsf where blh=\'' + blh + '\''
            if yzm.strip() not in '':
                isyzm=True
            if isyzm == True and istime==False:
                sql = 'select blh,yzm,sfrq,zl,lsj from dbo.zy_dxsf where blh=\'' + blh + '\' and yzm like \'%'+yzm+'%\''
            if isyzm==True and istime==True:
                sql = 'select blh,yzm,sfrq,zl,lsj from dbo.zy_dxsf where blh=\'' + blh + '\' and yzm like \'%' + yzm + '%\' and sfrq between  \''+timeStart+'\' and  \''+timeEnd+'\' '
            if isyzm == False and istime==True:
                sql = 'select blh,yzm,sfrq,zl,lsj from dbo.zy_dxsf where blh=\'' + blh + '\' and sfrq between  \'' + timeStart + '\' and  \'' + timeEnd + '\' '

            self.model.clear()
            self.model.setHorizontalHeaderLabels(['病历号','医嘱名','日期','总量','零售价'])

            print(sql)
            mxlist=self.helper.getData(sql)
            sum=len(mxlist)
            if sum==0:
                QMessageBox.information(self,"提示：","没有查询到内容啊，是不是输入有问题？")
                return
            self.progressBar.setMaximum(sum)
            i=0 #行
            j=0 #列
            for mx in mxlist:
                for j in range(5):
                    item=QStandardItem(str(mx[j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.model.setItem(i, j, item)
                    value=(i+1)*(j+1)
                    self.progressBar.setValue(value)
                i+=1
                #(self,blh,yzm,sfrq,zl,lsj):
        except Exception as e:
            print("出错了，原因是"+str(e))

