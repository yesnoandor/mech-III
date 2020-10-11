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


import json
import struct
import datetime
import logging
from utils.logger import Logger
from utils.utils import *
from utils import const

from pubsub import pub


const.MAGIC_NUMBER = 0x7e
const.ESCAPE_NUMBER = 0x7d
const.ESCAPE_ESCAPE_NUMBER = 0x01
const.ESCAPE_MAGIC_NUMBER = 0x02

const.GWM_VENDOR_ID = 0x20
const.L2_DEVICE_ID = 0x01
const.L3_DEVICE_ID = 0x02
const.L4_DEVICE_ID = 0x03

const.HEART_BEAT_UPLOAD = 0x0001
const.MODULE_EVENT_UPLOAD = 0x0002
const.SYSTEM_INFO_UPLOAD = 0x0100

const.SETTING_DOWNLOAD = 0x8004


class MechProtocol:
    """ 解析协议 """

    def __init__(self):  #
        """
        构造方法, 初始化变量
        """

        # 初始化日志类
        self.__logger = Logger('mech.log', logging.DEBUG, logging.DEBUG)

        #self.msg_id = 0
        #self.msg_len = 0
        #self.serial_number = 0
        self.vendor_id = const.GWM_VENDOR_ID
        self.product_id = const.L2_DEVICE_ID
        self.serial_id = bytearray([0, 0, 0, 0, 0, 0])
        self._serial_number = 0                 # 发送序列号，依次递增

        pass

    @staticmethod
    def escape(data):
        """
        转义处理
        :param data: 原始的bytearray
        :return:
        """
        escape_bin = bytearray()
        # print(type(data))
        for byte in data:         # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
            if byte == 0x7d:
                escape_bin.append(0x7d)
                escape_bin.append(0x01)
                pass
            elif byte == 0x7e:
                escape_bin.append(0x7d)
                escape_bin.append(0x02)
                pass
            else:
                escape_bin.append(byte)
                pass

        return escape_bin

    @staticmethod
    def unescape(data):
        """
        反转义处理
        :param data:
        :return:
        """
        unescape_bin = bytearray()

        flag = False
        for byte in data:
            if flag:
                if byte == 0x01:
                    unescape_bin.append(0x7d)
                else:
                    unescape_bin.append(0x7e)
                flag = False

            elif byte == 0x7d:
                flag = True
            else:
                unescape_bin.append(byte)

        return unescape_bin

    @staticmethod
    def build_inquiry_body():
        """
        构建查询指令
        :return:
        """
        cmd = {"system": ["version", "temperature", "cpu", "memory"]}
        print(cmd)
        jsoninfo = json.dumps(cmd)
        print(type(jsoninfo))
        print(jsoninfo)
        body = jsoninfo.encode("utf-8")
        print(type(body))
        print_hex(body)
        return body

    @staticmethod
    def build_rtc_sync_body():
        now = datetime.datetime.now()
        cmd = {
            "Setting":
                {"MOD_RTC":
                    {
                        "year": now.year,
                        "month": now.month,
                        "day": now.day,
                        "hour": now.hour,
                        "min": now.hour,
                        "sec": now.second
                    }
                }
        }
        jsoninfo = json.dumps(cmd)
        print(type(jsoninfo))
        print(jsoninfo)
        body = jsoninfo.encode("utf-8")
        print(type(body))
        print_hex(body)
        return body

    def build_header(self, msg_id, msg_len, vendor_id, product_id, serial_id):
        """
        构建header的bin数据
        """
        header = struct.pack('<HHBBBBBBBBI', msg_id, msg_len, vendor_id, product_id, serial_id[0], serial_id[1], serial_id[2], serial_id[3], serial_id[4], serial_id[5], self._serial_number)
        print_hex(header)

        self._serial_number += 1
        return header

    @staticmethod
    def build_crc(data):
        """
        计算crc的值
        :param data: 需要计算crc的bytearray
        :return: byte类型的crc输出
        """
        print_hex(data)
        check = crc16(data)
        crc = struct.pack('<H', check)
        print_hex(crc)
        return crc

    def build_inquiry_bin(self):
        """
        构建查询命令的bin格式
        :return:
        """
        body = self.build_inquiry_body()
        header = self.build_header(0x8100, len(body))
        inquiry_bin = self.build_bin(header + body)
        return inquiry_bin

    def build_rtc_sync(self):
        body = self.build_rtc_sync_body()
        header = self.build_header(0x8104, len(body))
        rtc_sync_bin = self.build_bin(header + body)
        return rtc_sync_bin

    def build_bin(self, header, body):
        crc = self.build_crc(header + body)
        data = header + body + crc
        data = self.escape(data)
        data = const.MAGIC_NUMBER + data + const.MAGIC_NUMBER
        print_hex(header)
        print_hex(body)
        print_hex(crc)
        print_hex(data)
        return data

    @staticmethod
    def parse_header(header):
        """
        解析头数据
        :param header:
        :return:
        """
        tmp = header[:2]
        msg_id = int.from_bytes(tmp, byteorder='little', signed=False)

        tmp = header[2:4]
        msg_len = int.from_bytes(tmp, byteorder='little', signed=False)

        vendor_id = header[4]
        product_id = header[5]
        serial_id = header[6:12]

        tmp = header[13:]
        serial_number = int.from_bytes(tmp, byteorder='little', signed=False)

        return msg_id, msg_len, vendor_id, product_id, serial_id, serial_number

    @staticmethod
    def parse_body(body):
        print(body)
        pass

    def parse_body_heart_beat(self):
        # print("parse_body_heart_beat::++++++++++++++++++++")
        # print("parse_body_heart_beat::--------------------")
        pass

    def parse_body_event(self, body):
        # print("parse_body_event::++++++++++++++++++++")
        # print(body)
        # print_hex(body)

        #body_json = json.dumps(body.decode("utf-8"))
        #print(type(body_json))
        #print(body_json)
        #body_dic = json.loads(body_json)
        body_dic = json.loads(body.decode("utf-8"))

        # print(type(body_dic))
        # print(body_dic["event"])
        if isinstance(body_dic["event"], dict):
            for k, v in body_dic["event"].items():
                # print(k)
                # print(v)
                if k == "mod":
                    name = v
                if k in ["warning", "error", "info"]:
                    status = k
                    log = v
            # print("type name =", type(name))
            # print("name = ", name)
            # print("log = ", log)
            # print("status = ", status)

            self.logger.info("name = ", name)
            self.logger.info("log = ", log)
            self.logger.info("status = ", status)

            pub.sendMessage('recv_module_event', name=name, log=log, status=status)

        elif isinstance(body_dic["event"], list):
            names = []
            states = []
            logs = []
            for event in  body_dic["event"]:
                # print(event["mod"])
                for k, v in event.items():
                    # print("k =", k)
                    # print("v =", v)
                    if k == "mod":
                        names.append(v)
                    if k in ["warning", "error", "info"]:
                        states.append(k)
                        logs.append(v)

            # print("names = ", names)
            # print("logs = ", logs)
            # print("states = ", states)

            for i in range(len(names)):
                name = names[i]
                log = logs[i]
                state = states[i]

                # print("type name =", type(name))
                # print("name = ", name)
                # print("log = ", log)
                # print("state = ", state)

                pub.sendMessage('recv_module_event', name=name, log=log, status=state)
        else:
            print("error event!!!")

        print("parse_body_event::--------------------")

        pass

    @staticmethod
    def parse_crc(crc_bin):
        """
        将两字节的byte类型数据转化为int类型的crc
        :param crc_bin: byte类型的crc
        :return: int类型的crc
        """
        crc = int.from_bytes(crc_bin, byteorder='little', signed=False)
        return crc

    def parse_data(self, data):
        """
        解析一帧完整bin数据
        :param data:
        :return:
        """
        print("parse_data++++++++")
        print(data)
        print_hex(data)
        data = self.unescape(data[1:-1])
        print(data)
        print_hex(data)

        header_bin = data[:16]
        print_hex(header_bin)
        msg_id, msg_len, vendor_id, product_id, serial_id, serial_number = self.parse_header(header_bin)
        # print("msg_id = ", msg_id)
        # print("msg_len = ", msg_len)
        # print("vendor_id = ", vendor_id)
        # print("product_id = ", product_id)
        # print("serial_id = ")
        # print_hex(serial_id)
        # print("serial_number = ", serial_number)

        if msg_len:
            body_bin = data[16:(16+msg_len)]
            self.parse_body(body_bin)

        begin = 16 + msg_len
        print("begin = ", begin)
        print_hex(data)
        print(len(data))
        crc_bin = data[begin:]
        print_hex(crc_bin)
        crc = self.parse_crc(crc_bin)
        print("-----------------")

        #
        print_hex(data[:-2])
        print("-----------------")
        check = crc16(data[:-2])
        print("check = 0x%x" % check)
        print("crc = 0x%x" % crc)
        if check != crc:
            print("crc error")
            return
        else:
            print("crc ok")
            if msg_id == const.HEART_BEAT_UPLOAD:
                self.parse_body_heart_beat()
            elif msg_id == const.MODULE_EVENT_UPLOAD:
                self.parse_body_event(data[16:-2])


        pass


if __name__ == '__main__':
    """
    heart_beat = "7e 01 00 00 00 20 01 00 00 00 00 00 00 00 00 00 00 c7 74 7e"
    heart_beat_bin = hexStringTobytes(heart_beat)
    print(heart_beat_bin)
    print_hex(heart_beat_bin)
    protocol = MechProtocol()
    protocol.parse_data(heart_beat_bin)
    """

    event = "7e 02 00 45 00 20 01 00 00 00 00 00 00 02 00 00 00 7b 22 65 76 65 6e 74" \
            "22 3a 7b 22 64 61 74 65 22 3a 22 32 30 31 39 30 32 31 36 30 39 32 38 31" \
            "35 22 2c 22 6d 6f 64 22 3a 22 43 43 43 22 2c 22 77 61 72 6e 69 6e 67 22 " \
            "3a 22 49 4d 55 5f 45 52 52 4f 52 22 7d 01 7d 01 34 24 7e "
    event_bin = hexStringTobytes(event)
    print(event_bin)
    print_hex(event_bin)
    protocol = MechProtocol()

    protocol.parse_data(event_bin)


    """
    cmd = {"system": ["version", "temperature", "cpu", "memory"]}
    print(type(cmd))
    print(cmd)
    jsoninfo = json.dumps(cmd)
    print(type(jsoninfo))
    print(jsoninfo)
    print(jsoninfo.encode("utf-8"))
    """
    """
    print("==============================")
    protocol = MechProtocol()
    bin = protocol.build_inquiry_bin()
    print(bin)
    print_hex(bin)
    bbb = protocol.escape(bin)
    print(bbb)
    print_hex(bbb)
    aaa = protocol.unescape(bbb)
    print(aaa)
    print_hex(aaa)
    pass
    """
