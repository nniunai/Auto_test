import pytest
from config.conf import *
from common.base import *



if __name__ == '__main__':

    report_path = get_report_path()+os.sep+"result"
    html_path = get_report_path()+os.sep+"html"

    pytest.main()


    # 生成测试报告
    #allure_report(report_path,html_path)

    #send_mail(title="接口测试报告测试",content=html_path)