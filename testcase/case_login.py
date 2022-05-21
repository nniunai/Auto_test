from config.conf import *
import os
from common.caseData import RunData
from common.excelConfig import DataConfig
from utils.logUtils import my_log
from utils.requestUtils import Requsts
import pytest
from common.base import *
from utils.assertUtils import AssertUtil
import allure

# 获取用例文件
case_file = os.path.join(get_case_data_path(),ConfigYaml().get_case_file())
#print(case_file)

# 获取用例工作薄
sheet_name = ConfigYaml().get_case_sheet()
# 获取用例数据
case_data = RunData(case_file,sheet_name)
run_case_data = case_data.get_case_data()

#print(case_data)
# 日志
log = my_log()
# 初始化参数
data_key = DataConfig







class TestExcel:

    def run_api(self,method,url,params=None,head=None,cookie=None):
        """
        执行用例
        :param method:
        :param url:
        :param params:
        :param head:
        :param cookie:
        :return:
        """

        rq = Requsts()
        if len(str(params).strip()) is not 0:
            params = json_parse(params)

        log.info("请求参数：%s" % (params))

        if str(method).lower() == "get":
            res = rq.get(url, json=params, headers=head)
        elif str(method).lower() == "post":
            res = rq.post(url, json=params, headers=head)
        else:
            log.error("错误请求method：%s" % (method))

        return res


    def run_pre(self,pre_case):
        """
        执行前置用例
        :param pre_case:
        :return:
        """
        #初始化数据


        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        # 判断headers是否存在
        head = json_parse(headers)
        res=self.run_api(method,url,params,head)
        print("前置用例执行完毕 返回")
        print(res)
        return res




    @pytest.mark.parametrize("case",run_case_data)
    def test_run(self,case):

        # 初始化请求数据

        url = ConfigYaml().get_conf_url()+case[data_key.url]
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        headers = case[data_key.headers]
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        is_run = case[data_key.is_run]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]

        log.info(url)


        # 验证是否有前置条件
        if pre_exec:
            pre_case_data = case_data.get_case_pre(pre_exec)
            log.info("需要执行前置用例：%s" % (pre_case_data))
            pre_res=self.run_pre(pre_case_data)
            heades=self.get_correlation(headers,pre_res)

        head = json_parse(heades)
        res=self.run_api(method,url,params,head=head)


        #allure报告
        # feature： sheet名称   一级
        allure.dynamic.feature(sheet_name)
        # story：模块    二级
        allure.dynamic.story(case_model)
        # title：用例编号+接口名称
        allure.dynamic.title(case_id+case_name)
        # description：请求的信息 url 类型 描述
        desc = "<font color='red'>请求url:</font> {} <br /> " \
               "<font color='red'>请求类型:</font> {} <br /> " \
               "<font color='red'>预期结果:</font> {}<br /> " \
               "<font color='red'>实际结果:</font> {} ".format(url,method,expect_result,res)
        #allure.dynamic.description(desc)
        allure.dynamic.description_html(desc)



        # 断言
        ast =AssertUtil()
        ast.assert_code(int(res["code"]),code)




    def get_correlation(self,head,pre_res):
        """
        关联替换
        :param head:
        :param pre_res:
        :return:
        """
        # 验证是否有关联,取出关联 key
        para_head=params_find(headers=head)
        if len(para_head) :
            # 接受前置用例返回值去body中提取关联key的值

            # 取值 待优化
            head_data =pre_res["body"]["data"][para_head[0]]
            # 进行替换关联
            headers = res_sub(head,head_data)

        return headers


if __name__ == '__main__':

    report_path = get_report_path()+os.sep+"result"
    html_path = get_report_path()+os.sep+"html"
    pytest.main(["-vs", "case_login.py", "--alluredir",report_path])

    # 生成测试报告
    allure_report(report_path,html_path)

    send_mail(title="接口测试报告测试",content=html_path)
    # str1 = '{"Authorization":"Bearer ${token}$"}'
    #
    # if "${" in str1:
    #     print(str1)
    # pattern = re.compile("\${(.*)}\$")
    # re_res = pattern.findall(str1)
    #
    # token = "123"
    # res = re.sub(pattern,token,str1)
    # print(res)



