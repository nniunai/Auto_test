import pytest
import allure

# allure generate report/result -o report/html
# allure generate report/result -o report/html --clean

"""
feature： sheet名称   一级
story：模块    二级
title：用例编号+接口名称
description：请求的信息 url 类型 描述
"""


@allure.title("测试用例标题1")
@allure.description("执行的描述内容")

@allure.feature("一级模块")
class TestAllure():


    @allure.title("测试用例标题1")
    @allure.description("执行的描述内容")
    @allure.story("这是二级模块")
    def test_01(self):
        print("测试01")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        print("测试02")

    def test_03(self):
        print("测试03")

    @pytest.mark.parametrize("case",["case01","case02","case03"])
    def test_04(self,case):
        print(case)
        allure.dynamic.title(case)


if __name__ == '__main__':
    pytest.main(["allure_demo.py"])