import os
from utils.yamlUtils import YamlReader



# 获取到项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
#print(BASE_DIR)

# cinfig 路径
_congfig_path = BASE_DIR+os.sep+"config"
# config.yaml 文件路径
_config_yaml_path = _congfig_path+os.sep+"config.yml"
# log文件路径
_log_path = BASE_DIR+os.sep+"logs"
# db_conf.yml 文件路径
_config_dbconf_path = _congfig_path+os.sep+"db_conf.yml"

# 用例数据路径
_case_data_path= BASE_DIR+os.sep+"data"

# 报告存放路径
_report_path = BASE_DIR+os.sep+"report"


def get_report_path():
    return _report_path



def get_config_path():
    return _congfig_path

def get_config_file():
    return _config_yaml_path

def get_log_path():
    return _log_path

def get_dbconf_path():
    return _config_dbconf_path

def get_case_data_path():
    return _case_data_path





class ConfigYaml:

    def __init__(self):
        self.config = YamlReader(get_config_file()).read()
        self.db_conf = YamlReader(get_dbconf_path()).read()


    def get_conf_url(self):
        return self.config["base"]["test"]["url"]

    def get_conf_loglevel(self):
        return self.config["base"]["log_level"]

    def get_conf_log_extension(self):
        return self.config["base"]["log_extension"]


    def get_db_conf_info(self,db_alias):
        """
        根据不同环境 获取不同数据库
        :param db_alias:
        :return:
        """
        return self.db_conf[db_alias]

    def get_case_file(self):
        return self.config["base"]["test"]["case_file"]

    def get_case_sheet(self):
        return self.config["base"]["test"]["case_sheet"]

    def get_email_info(self):

        return self.config["email"]




if __name__ == '__main__':
    cy = ConfigYaml()
    print(cy.get_conf_url())
    print(cy.get_conf_log_extension())
    print(cy.get_conf_loglevel())
    print(cy.get_db_conf_info("db_test01"))
    print(cy.get_case_file())
    print(cy.get_case_sheet())
    print(cy.get_email_info())