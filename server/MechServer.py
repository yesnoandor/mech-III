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

import threading
import logging
from utils.logger import Logger
from queue import Queue
from system.config import system_config
from utils.utils import *
from socketserver import ThreadingTCPServer, TCPServer, BaseRequestHandler
from server.MechProtocol import MechProtocol

g_client_pool = []      # 客户端IP池
g_conn_pool = []        # 连接池
g_protocol_pool = {}    # 协议对象池


class ModuleServerHandler(BaseRequestHandler):
    # 每一个连接初始化
    def setup(self):
        super().setup()

        # 加入连接池
        g_client_pool.append(self.client_address[0])
        g_conn_pool.append(self.request)

        protocol = MechProtocol()
        g_protocol_pool[self.client_address[0]] = protocol

    # 每一个连接清理
    def finish(self):
        super().finish()

        print(self.client_address)

        g_client_pool.remove(self.client_address[0])
        g_conn_pool.remove(self.request)
        del g_protocol_pool[self.client_address[0]]

    # 每一次请求处理
    def handle(self):
        super().handle()

        try:
            while True:
                # 接受数据
                data = self.request.recv(1024)

                # print(type(data))
                # print_hex(data)
                # print(data.decode("utf-8"))

                #msg = '{}{}'.format(self.client_address, data.decode("utf-8")).encode("utf-8")
                #print("msg =", msg)

                g_protocol_pool[self.client_address[0]].parse_data(data)
        except Exception as e:
            print(e)

        finally:
            print('=== end ====')


class ModuleServerThread(threading.Thread):
    def __init__(self, name, data, event):
        super().__init__(name=name)         # 调用父类(超类)的__init__()方法

        # 初始化日志类
        self.__logger = Logger('mech.log', logging.DEBUG, logging.DEBUG)

        # 外部通讯参数
        self.__queue = data                 # 用于向外部传输队列数
        self.__event = event                # 用于触发外部事件
        #self.__exit = exit
        #self.__found = set()
        #self.__found_label = set()
        #self.__fsm = fsm()

        # 控制线程参数初始化
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.clear()                 # 设置为False
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()                # 将running设置为True

    def __del__(self):
        print("__del__")

    def pause(self):
        print("pause module server thread!")
        self.__flag.clear()         # 设置为False, 让线程阻塞

    def resume(self):
        print("resume module server thread!")
        self.__flag.set()           # 设置为True, 让线程停止阻塞

    def stop(self):
        print("stop module server thread!")
        self.__flag.set()           # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()      # 设置为False

    def run(self):
        ip, port = system_config.get_module_server_info()
        server = ThreadingTCPServer((ip, port), ModuleServerHandler)

        self.__logger.logger.error("ip = {}".format(ip))
        self.__logger.logger.error("port = {}".format(port))

        server_thread = threading.Thread(target=server.serve_forever, name='ModuleServer', daemon=True)
        server_thread.start()

        while self.__running.isSet():
            self.__flag.wait()              # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回

            #   self.__exit.wait(0.01)                           # 等待退出事件, 0.01s超时退出
            #   if self.__exit.isSet():
            #       self.__exit.clear()

            #        self.__found.clear()
            #        self.__found_label.clear()

            #        self.pause()                                # 暂停线程

            #else:
            #    break


        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    queue = Queue()
    event = threading.Event()

    thread = ModuleServerThread("ModuleServer", queue, event)
    thread.start()
    pass
