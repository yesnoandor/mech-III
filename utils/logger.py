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


import sys
import time
import os.path
import logging
from colorama import Fore, Style


class Logger:
    def __init__(self, logger, clevel=logging.DEBUG, flevel=logging.DEBUG):
        self.logger = logging.getLogger(name=logger)
        self.logger.setLevel(logging.DEBUG)
        # fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fmt = logging.Formatter("[%(asctime)s] - [%(filename)s] - [line:%(lineno)d] - %(name)s - %(message)s", '%Y-%m-%d %H:%M:%S')

        if not self.logger.handlers:
            # 设置CMD日志
            sh = logging.StreamHandler(sys.stdout)
            sh.setFormatter(fmt)
            sh.setLevel(clevel)

            # 设置文件日志
            fh = logging.FileHandler(logger)
            fh.setFormatter(fmt)
            fh.setLevel(flevel)

            # 给logger添加handler
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(Fore.WHITE + "DEBUG - " + str(message) + Style.RESET_ALL)

    def info(self, message):
        self.logger.info(Fore.BLUE + "INFO - " + str(message) + Style.RESET_ALL)

    def war(self, message):
        self.logger.warning(Fore.YELLOW + "WARNING - " + str(message) + Style.RESET_ALL)

    def error(self, message):
        self.logger.error(Fore.RED + "WARNING - " + str(message) + Style.RESET_ALL)

    def cri(self, message):
        self.logger.critical(Fore.RED + "WARNING - " + str(message) + Style.RESET_ALL)


logger_mech = Logger('mech.log', logging.DEBUG, logging.DEBUG)

if __name__ == '__main__':
    logyyx = Logger('yyx.log', logging.DEBUG, logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')

    service_name = "hese"
    logyyx.error('%s service is %s!' % (service_name, 'down'))
    logyyx.error('{} service is {}'.format(service_name, 'down'))

    aaa = 43
    logyyx.war('%d service is %s!' % (aaa, 'down'))
    pass
