import openpyxl
import os



class Excel:

    def __init__(self,file):
        if os.path.exists(file):
            self.excel = openpyxl.load_workbook(file)
        else:
            raise FileNotFoundError("文件不存在")

        self._datalist=[]


    def read(self,sheetname=None):
        """

        :param sheetname:
        :return:
        """
        if not self._datalist:

            if sheetname is None:
                for sheet in self.excel:

                    for value in sheet.values:
                        print(value)
            else:
                self.sheet = self.excel[sheetname]
                title = self.read_row(sheetname,0)

                for value in self.sheet.values:
                    if "编号" in value[0]:
                        continue
                    self._datalist.append(dict(zip(title,value)))

        return self._datalist


    def read_row(self,sheetname,number=0):
        """
        读取指定行的值
        :param sheetname:
        :param number:
        :return:
        """

        sheet = self.excel[sheetname]
        list=[]
        for value in sheet.values:
            list.append(value)
        return list[number]




if __name__ == '__main__':
    ex = Excel("../data/case_api.xlsx")
    data=ex.read("Sheet1")
    print(data)

