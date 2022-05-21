import pymysql
from utils.logUtils import my_log


class Mysql:

    def __init__(self,host,user,passwd,database,charset="utf8",port=3306):
        self.log = my_log()
        self.connect = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database,
            charset=charset,
            port=port
        )

        self.cursor = self.connect.cursor(cursor=pymysql.cursors.DictCursor)




    def fetchone(self,sql):
        """
        单行查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        """
        多行查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def exec(self,sql):

        try:
            if self.connect and self.cursor:
                self.cursor.execute(sql)
                self.connect.commit()

        except Exception as ex :
            self.connect.rollback()
            self.log.error("执行失败")
            self.log.error(ex)
            return False
        return True


    def __del__(self):
        # 先关闭光标
        if self.cursor is not None:
            self.cursor.close()
        if self.connect is not None:
            self.connect.close()

if __name__ == '__main__':
    my = Mysql(host="106.14.225.213",user="hduser8000",passwd="hd123456",database="test_16")

    my.exec("update users set password = '123' where username='test00'")
    res=my.fetchall(sql="select * from users")

    print(res)