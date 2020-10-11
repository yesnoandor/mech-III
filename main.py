#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
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



@Date: 2020/5/19
@Name: smartbox.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

'''

import wx
import time
import random
import threading
import logging
from utils.logger import Logger
from utils.logger import logger_mech
from pubsub import pub
from queue import Queue
from ui.MechApp import MechApp
from server.MechServer import ModuleServerThread


class MechThread(threading.Thread):
    """  主线程 """
    def __init__(self, name, data, event, app):
        super().__init__(name=name)  # 调用父类(超类)的__init__()方法

        # 初始化日志类
        self.__logger = Logger('mech.log', logging.DEBUG, logging.DEBUG)

        # 同步事件和队列的初始化
        self.__queue = data
        self.__event = event
        self.__app = app

        # Module Server 线程的初始化
        self.__exit = threading.Event()
        self.__module_server_thread = ModuleServerThread("ModuleServer", self.__queue, self.__event)
        self.__module_server_thread.start()
        self.__logger.info("Start ModuleServerThread...")

        """
        # SQLite的初始化
        self.__sql = simpleToolSql("smartbox")

        cmd = '''create table if not exists smartbox(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                object text,
                catalogue text,
                name text,
                timestamp NOT NULL DEFAULT (datetime('now','localtime'))
                )'''
        self.__sql.execute(cmd)
        self.__sql.close()
        """

        # 状态机的初始化
        # fsm.state = 'idle'

    def run(self):
        while True:
            self.__event.wait(300)          # 等待触发事件, 300s超时退出
            if self.__event.isSet():
                print("get a event!")
                self.__logger.logger.info("get a event!")
                data = self.__queue.get()   # 获取数据
            else:
                print("timeout!")
                self.__logger.logger.info("event timeout!")
                data = [0, ]

            # self.dispatchEvent(data)  # 分发事件处理
            # self.__event.clear()  # 清除读事件，以方便下次读取

    def timeout_event_treat(self):
        """
        超时处理
        :return:
        """
        pass

    def module_event_treat(self, data):
        """

        :param code:
        :return:
        """
        self.__logger.info("get a module event: {}".format(data))
        wx.CallAfter(pub.sendMessage, 'recv_module_event', name=data[0], log=data[1], status=data[2])

    def dispatchEvent(self, val):
        """ 事件分发处理 """
        print("system event is {0}".format(val))
        self.__logger.info("system event is {}".format(val))
        event_func = {
            0: lambda: self.timeout_event_treat(),
            1: lambda: self.module_event_treat(val[1])
        }
        func = event_func[val[0]]
        func()
        pass


if __name__ == '__main__':
    logger_mech.info('--主线程开始--')
    queue = Queue()
    event = threading.Event()
    app = MechApp()

    main_thread = MechThread("mech_thread", queue, event, app)
    main_thread.start()

    app.MainLoop()

    main_thread.join()

    logger_mech.info('--主线程结束--')