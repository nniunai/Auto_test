from config.conf import   ConfigYaml
from utils.emailUtil import Email
from utils.mysqlUtils import Mysql
import json
import re
import subprocess
from utils.logUtils import my_log


pattern_data = "\${(.*)}\$"


# 初始化数据库
def init_db(db_alias):

    # 初始化配置信息
    db_info = ConfigYaml().get_db_conf_info(db_alias)

    host = db_info["host"]
    user = db_info["user"]
    pwd = db_info["psswrd"]
    database = db_info["database"]
    port = db_info["port"]

    # 初始化mysql对象
    conner = Mysql(host=host,user=user,passwd=pwd,database=database)

    return conner



def json_parse(data):
    """
    格式化字符 转化为json数据
    :param data:
    :return:
    """
    return json.loads(data) if data else data


def res_find(datas,pattern_data=pattern_data):
    """
    查询是否有指定匹配字符
    :param datas:
    :param pattern_data:
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(datas)
    return re_res


def res_sub(datas,replace,pattern_data=pattern_data):
    """

    :param datas: 需要替换的数据
    :param replace: 传入替换的值
    :param pattern_data: 替换规则
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(datas)
    if re_res:
        return re.sub(pattern_data,replace,datas)
    return re_res



def params_find(headers,cookies=None):
    """
    验证请求中是否有需要替换的变量
    :param headers:
    :param cookies:
    :return:
    """

    if "${" in headers:
        head = res_find(headers)
    return head


def allure_report(report_json_path,report_html_json):

    allure_cmd = "allure generate %s -o %s --clean" % (report_json_path,report_html_json)
    try:
        subprocess.call(allure_cmd,shell=True)
        my_log().info("生成测试报告执行命令：%s"%(allure_cmd))
    except :
        my_log().error("执行报告失败")


def send_mail(report_html_path="",content="",title="测试"):
    data = ConfigYaml().get_email_info()
    smtp_addr = data["smtpserver"]
    username = data["username"]
    password = data["password"]
    recv = data["receiver"]
    print(smtp_addr, username, password, recv)

    email = Email(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()


if __name__ == '__main__':
    # db=init_db("db_test01")
    print(res_find('{"Authorization":"Bearer ${token}$"}'))
    s=res_sub('{"Authorization":"Bearer ${token}$"}',"lkdjlkj")
    print(s)

