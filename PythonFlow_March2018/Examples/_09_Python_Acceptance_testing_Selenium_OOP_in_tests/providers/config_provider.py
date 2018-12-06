import json
import os
from ..utils import find_property

class ConfigProvider(object):
    __configs = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ConfigProvider, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def get_config(self, config_path):
        config = self.__configs.get(config_path, None)
        if not config:
            config = Config(config_path)
            self.__configs[config_path] = config
        return config


class Config(object):
    def __init__(self, config_path):
        with open(config_path) as config:
            conf_str = config.read()
            if os.name == 'nt':
                conf_str = conf_str.replace('\\', '\\\\')
            self.config = json.loads(conf_str)

    def get_param(self, param_name):
        return find_property(self.config, param_name)    

if __name__ == '__main__':
    conf = Config('config.txt')
    print(conf.get_param('app_path'))
