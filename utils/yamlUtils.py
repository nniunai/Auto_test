import os
import yaml

class YamlReader:

    def __init__(self,yamlfile):

        if os.path.exists(yamlfile):
            self.yamlfile = yamlfile

        else:
            raise FileNotFoundError("文件不存在")

        self._data=None
        self._data_all=None

    def read(self):

        if not self._data:
            with open(self.yamlfile,"rb") as f:
                self._data = yaml.safe_load(f)
        return self._data


    def read_all(self):

        if not self._data:
            with open(self.yamlfile,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all


if __name__ == '__main__':
    ym = YamlReader("../data/yamldemo.yml")
    d=ym.read()
    print(d)