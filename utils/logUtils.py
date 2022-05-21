import logging
from config import conf
import datetime,os

level = {
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR,

}


class Logger():

    def __init__(self,log_file,log_name,log_level):
        self.log_file = log_file
        self.log_name= log_name
        self.log_level = log_level



        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(level[self.log_level])

        if not self.logger.handlers:
            stream = logging.StreamHandler()
            stream.setLevel(level[self.log_level])
            formatter = logging.Formatter("%(asctime)s|%(levelname)8s|%(filename)s[:%(lineno)d]|%(message)s")
            stream.setFormatter(formatter)

            # 写入文件
            fh = logging.FileHandler(self.log_file,encoding="utf-8")
            fh.setLevel(level[self.log_level])
            fh.setFormatter(formatter)

            # 添加处理器
            self.logger.addHandler(stream)
            self.logger.addHandler(fh)




# 初始化
# 获取日志存放的路径
log_path =conf.get_log_path()
# 获取当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# 获取扩展名
log_extension = conf.ConfigYaml().get_conf_log_extension()
#定义log名
logfile = os.path.join(log_path,current_time+log_extension)
#print(logfile)

# 日志级别
loglevel = conf.ConfigYaml().get_conf_loglevel()

def my_log(log_name = __file__):
    return Logger(log_file=logfile,log_name=log_name,log_level=loglevel).logger

if __name__ == '__main__':
    my_log().debug("hahahhah")