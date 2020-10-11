#! /home/wenyu/anaconda3/bin/python3
# -*- coding: utf-8 -*-


"""
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑       永无BUG 

'''
  

Created on 


@author: wenyu_xu
@mail:wenyu__xu@163.com




"""

import os
import json
import logging
from utils.logger import Logger
from system.default import DEFAULT_SYSTEM_CONFIG
from utils.utils import json_bottom_dict


class system_params:
    """
    系统默认配置
    """
    def __init__(self, file="config.json"):
        self.__logger = Logger('mech.log', logging.DEBUG, logging.DEBUG)

        self._cfg = DEFAULT_SYSTEM_CONFIG
        path = os.getcwd() + "/" + file
        # print(path)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    self._cfg = json.load(f)
                except Exception as e:
                    print(e)
                    self._cfg = DEFAULT_SYSTEM_CONFIG
        except Exception as e:
            print(e)
            self._cfg = DEFAULT_SYSTEM_CONFIG

        self.__logger.info('configuration = {}'.format(self._cfg))

    def get_module_server_info(self):
        """
        获取module server的IP和Port
        :return:
        """
        ip = self._cfg['module_server']['ip']
        port = int(self._cfg['module_server']['port'])
        self.__logger.info('ip = {}'.format(ip))
        self.__logger.info('port = {}'.format(port))

        return ip, port

    def get_module_monitor_name(self):
        """
        获取module server必须的监控模块
        :return:
        """

        json_module = self._cfg['module_monitor']
        self.__logger.info('json_module = {}'.format(json_module))

        """
        if isinstance(json_module, dict):
            for key in json_module:
                if isinstance(json_module[key], dict):
                    pass
                else:
                    module += json_module[key]
        print(module)
        """

        module = []
        dic = {}
        json_bottom_dict(json_module, dic)
        # print(dic)
        for k, v in dic.items():
            module += v
        self.__logger.info('module = {}'.format(module))

        return module

    def get_can_analyzer_info(self):
        usb_id = self._cfg['can_analyzer']
        print(usb_id)
        vendor_id = usb_id['vendor_id']
        product_id = usb_id['product_id']

        print("vendor_id = %#x" % vendor_id)
        print("product_id = %#x" % product_id)
        return vendor_id, product_id


system_config = system_params()

if __name__ == '__main__':
    config = system_params()
    config.get_module_server_info()
    config.get_module_monitor_name()
    config.get_can_analyzer_info()
    pass
