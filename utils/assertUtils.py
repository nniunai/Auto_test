from utils.logUtils import my_log
import json
from common.base import init_db





class AssertUtil:

    def __init__(self):
        self.log = my_log("AssertUtil")


    def assert_code(self,code,expected_code):
        """
        验证返回状态码
        :param code:
        :param expected_code:
        :return:
        """

        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("断言状态码错误，实际值：%s，期望值为：%s" % (code,expected_code))
            raise


    def assert_body(self,body,expected_body):
        """
        断言响应结果相等
        :param body:
        :param expected_body:
        :return:
        """

        try:

            assert body == expected_body
            return True
        except:
            self.log.error("断言响应内容不相同，实际值：%s，期望值为：%s" % (body,expected_body))
            raise


    def assert_in_body(self,body,expected_body):


        try:
            bodys = json.dumps(body)
            assert expected_body in bodys
            return True
        except:
            self.log.error("断言响应内容不包含，实际值：%s，期望值为：%s" % (body, expected_body))
            raise


    def assert_db(self,sql,rp_res,db_name="db_test01"):

        con = init_db(db_name)

        # 数据库查询
        db_res = con.fetchone(sql)

        # 获取数据库结果的key
        verify_list = list(dict(db_res).keys())

        for line in verify_list:
            # 接口返回的数据
            res_line = rp_res[line]
            # 数据库取到的数据
            res_db_lin=dict(db_res)[line]

            # 验证
            self.assert_in_body(res_line,res_db_lin)






