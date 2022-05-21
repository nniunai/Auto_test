from utils.excelUtils import Excel
from common.excelConfig import DataConfig
from config.conf import get_case_data_path
import os


# print(get_case_data_path())



# read = Excel(get_case_data_path()+"case_api.xlsx")


class RunData():

    def __init__(self,file,sheetname):
        self.read = Excel(file)
        self.sheetname= sheetname

    def get_case_data(self):
        """
        获取需要执行的用例
        :return:
        """
        run_list=[]
        for data in self.read.read(self.sheetname):
            if str(data[DataConfig().is_run]).lower() == "y":
                run_list.append(data)
        return run_list

    def get_case_all(self):
        """
        返回所有的测试用例
        :return:
        """
        run_list = [ data for data in self.read.read(self.sheetname)]
        return run_list

    def get_case_pre(self,pre):
        """
        根据前置条件去全部用例筛选出对应的用例
        :param pre:
        :return:
        """
        run_list = self.get_case_all()
        for case in run_list:
            if pre in dict(case).values():
                return case





if __name__ == '__main__':
    run=RunData("../data/case_api.xlsx","Sheet1")
    print(run.get_case_pre("C001"))