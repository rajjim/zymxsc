import pymssql
from model import zymx
class Mssql_helper:
    def __init__(self,host,user,pwd,db):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db
        self.conn=None
        self.cursor=None

    def __getCursor(self):
        try:
            self.conn=pymssql.connect(self.host,self.user,self.pwd,self.db)
            self.cursor=self.conn.cursor()
        except Exception as e:
            print(str(e))

    def getData(self,sql):
        try:
            self.__getCursor()
            self.cursor.execute(sql)
            zymxlist=[]
            print('执行到了')
            for row in self.cursor:
                print(row)
                zymxlist.append(list(row))
            return zymxlist
        except Exception as e:
            print(e)

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(e)