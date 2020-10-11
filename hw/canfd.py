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

import wx
import time
import usb
import logging
from utils.logger import Logger
from ctypes import CDLL, sizeof
from hw.ZLG_Struct import *
from copy import deepcopy
from pyudev.wx import MonitorObserver, EVT_DEVICE_EVENT
from pyudev import Context, Monitor
import threading


class CanAnalyze:
    def __init__(self, vendor_id, product_id):
        # 初始化日志类
        self._logger = Logger('mech.log', logging.DEBUG, logging.DEBUG)

        self._vendor_id = vendor_id
        self._product_id = product_id
        self._canfd_devices = []        #

        self.scan_devices(vendor_id, product_id)
        pass

    def get_info(self):
        pass

    def send(self, data):
        pass

    def recv(self, len=64):
        data = []
        return data

    def scan_devices(self, vendor_id, product_id):
        """
        扫描并获取所有指定USB id的CAN分析仪设备
        :param vendor_id:
        :param product_id:
        :return: 设备类的列表
        """
        devices = usb.core.find(find_all=True)
        if devices is None:
            raise ValueError('CAN Device not found')

        # print(type(devices))
        # print(devices)
        for device in devices:
            if (device.idVendor == vendor_id) & (device.idProduct == product_id):
                self._canfd_devices.append(device)
            # print(type(device))
            # print(device)

        # print("device number = ", len(self._canfd_devices))
        # print(self._canfd_devices[0].idVendor)
        # print(type(self._canfd_devices))
        # print(self._canfd_devices[0].get_active_configuration())

        return self._canfd_devices


class CanAnalyze_ZLG(CanAnalyze):
    def __init__(self, vendor_id, product_id):
        super().__init__(vendor_id, product_id)

        self._canfd_so = "./libusbcanfd.so"         # CANFD动态库名称
        self._canfd = CDLL(self._canfd_so)          # 获取CANFD的句柄
        self._device_type = 33                      # 设备类型 （USBCANFD-200U）
        self._can_err_msg = ZCAN_ERR_MSG()          #
        self._can_stat = ZCAN_STAT()

        # CAN分析仪的初始化参数配置
        can_clk = 60000000,
        can_mod = 0
        aset = ASET(
            tseg1=6,
            tseg2=1,
            sjw=1,
            smp=0,
            brp=5
        )
        dset = DSET(
            tseg1=6,
            tseg2=1,
            sjw=1,
            smp=0,
            brp=2,
        )
        self._init_info = ZCAN_INIT(
            clk=can_clk,
            mode=can_mod,
            aset=aset,
            dset=dset
        )

        # 获取CAN分析仪的设备信息,保存到私有变量self._canfd_devices_info中
        # self._canfd_devices_info = dict()
        self._canfd_devices_info = self.GetCANFDDevicesInfo()
        self._logger.info("canfd devices info = {}".format(self._canfd_devices_info))

    def GetDevicesInfo(self):
        """
        获取CAN分析仪的设备信息
        :return:
        """
        # self.scan_devices(0x04cc, 0x1240)
        canfd_devices_info = dict()

        self._OpenDevice(0)
        info = self._ReadDeviceInfo(0)

        """
        print(type(info))
        print("board_info = ", info)
        print("hardware version = 0x%x " % info.hmv)
        print("firmware version = 0x%x" % info.fwv)
        print("driver version = 0x%x" % info.drv)
        print("api version = 0x%x" % info.api)
        print("irq = ", info.irq)
        print("channels = ", info.chn)
        print(type(info.sn))
        print("sn = ", info.sn)
        print(type(info.id))
        print("id = ", info.id)
        print(info.sn[0])
        """

        """
        sn = str()
        for ch in info.sn:
            sn += chr(ch)
        """
        sn = "".join(list(map(str, info.sn)))
        self._logger.info("sn = {}".format(sn))

        canfd_devices_info[sn] = {
            "index": 0,
            "hmv": hex(info.hmv),
            "fwv": hex(info.fwv),
            "drv": hex(info.drv),
            "api": hex(info.api),
            "irq": hex(info.irq),
            "chn": hex(info.chn),   # 转化为16进制字符串
            "channel": {}
        }

        for inc in range(int(canfd_devices_info[sn]["chn"], 16)):
            canfd_devices_info[sn]["channel"][inc] = dict(init=False, receive=False)

        # print(canfd_devices_info)
        # print(type(canfd_devices_info[sn]['hmv']))
        # print(canfd_devices_info[sn]['hmv'])

        return canfd_devices_info

        """
        for num in range(0, can_num):
            opened = False
            for sn, can_info in self._canfd_devices_info.iteritems():
                if can_info['device_index'] == num:
                    opened = True
                    break
            if not opened:
                self._OpenDevice(num, 0)
            board_info = self._ReadBoardInfo(num)
            sn = str()
            for ch in board_info.sn:
                sn += chr(ch)

            canfd_devices_info[sn] = {
                "device_index": num,
                "hmv": hex(board_info.hmv),
                "fwv": hex(board_info.fwv),
                "drv": hex(board_info.drv),
                "api": hex(board_info.api),
                "irq": hex(board_info.irq),
                "chn": hex(board_info.chn),
                "channel": {}
            }

            for inc in range(int(canfd_devices_info[sn]["chn"], 16)):
                canfd_devices_info[sn]["channel"][inc] = dict(init=False, receive=False)
        """

    def ResetCAN(self):
        """
        复位当前所有CAN分析仪的所有通道
        :return:
        """
        for sn, device in self._canfd_devices_info.items():
            for chn in device["channel"]:
                self._ResetCAN(device["device_index"], chn)

    def GetDevInfoFromSN(self, sn):
        """
        根据设备SN号，得到设备索引号
        :param sn:
        :return:
        """
        if sn in self._canfd_devices_info.keys():
            return self._canfd_devices_info[sn]
        else:
            raise ValueError("No device has SN: {}".format(sn))

    def GetDevIDFromSN(self, sn):
        dev_info = self.GetDevInfoFromSN(sn)

        return dev_info["device_index"]

    def GetInitInfo(self):
        """
        返回初始化配置参数
        :return:
        """
        return self._init_info

    def Start(self, index, chn):
        init_info = self.GetInitInfo()

        self._InitCAN(index, chn, init_info)
        self._SetReference(index, chn, 0x18, c_int(1))      # 设置CANFD的波特率为
        self._StartCAN(index, chn)
        # self._ClearBuffer(card_index, chn)
        # self._canfd_devices_info[sn]["channel"][chn]['init'] = True

    def Send(self, index, channel, msg_id, dat):
        # card_index = self.GetDevIDFromSN(sn)

        msg_inf = ZCAN_MSG_INF(
            fmt=1,
            brs=1,
            txm=0,
            sdf=0,
            sef=0
        )

        long_msg_hdr = ZCAN_MSG_HDR(
            inf=msg_inf,
            len=64,
            chn=0,
            id=msg_id
        )

        msg = CANFDMSG(
            hdr=long_msg_hdr,
            dat=(U8 * 64)(0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x27,
                          0x7, 0x8, 0x9, 0x10, 0x11, 0x12, 0x13, 0x14,
                          0x15, 0x16, 0x17, 0x18, 0x19, 0x20, 0x21, 0x22,
                          0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x30,
                          0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38,
                          0x39, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46,
                          0x47, 0x48, 0x49, 0x50, 0x51, 0x52, 0x53, 0x54,
                          0x55, 0x56, 0x57, 0x58, 0x59, 0x60, 0x61, 0x62)
        )

        self._TransmitFD(self, index, channel, msg)

    def _OpenDevice(self, card_index):
        """
        打开CAN分析仪
        :param card_index:
        :return:
        """
        if self._canfd.VCI_OpenDevice(self._device_type, card_index, 0) != 1:
            raise Exception("Open device id {} failed!".format(str(card_index)))

    def _CloseDevice(self, card_index):
        """
        关闭CAN分析仪
        :param card_index:  设备索引号
        :return:
        """
        if self._canfd.VCI_CloseDevice(self._device_type, card_index) != 1:
            raise Exception("Cloase device id {} failed!".format(str(card_index)))

    def _InitCAN(self, card_index, channel, init_info):
        """
        初始化CAN分析仪的某一路
        :param card_index: 设备索引号
        :param channel: 设备通道号
        :param init_info: 初始化配置参数
        :return:
        """
        if self._canfd.VCI_InitCAN(self._device_type, card_index, channel, byref(init_info)) != 1:
            raise Exception("Init device id {} channel {} failed!".format(str(card_index),
                                                                          str(channel)))

    def _ReadDeviceInfo(self, card_index):
        """
        获取CAN分析仪的设备信息
        :param card_index: 设备索引号
        :return:
        """
        device_info = ZCAN_DEV_INF()
        if self._canfd.VCI_ReadBoardInfo(self._device_type, card_index, byref(device_info)) != 1:
            raise Exception("Can't get device info from {}".format(str(card_index)))
        else:
            return device_info

    def _ReadDeviceErrInfo(self, card_index, channel):
        """
        获取CAN分析仪某一路的最近一次错误信息
        :param card_index: 设备索引号
        :param channel: 设备通道号
        :return:
        """
        error_info = ZCAN_ERR_MSG()

        if self._canfd.VCI_ReadErrInfo(self._device_type, card_index, channel, byref(error_info)) != 1:
            raise Exception("Can't get channel error info from device id {} channel {}".format(str(card_index),
                                                                                               str(channel)))
        else:
            return error_info

    def _ReadCANStatus(self, card_index, channel):
        """
        获取CAN分析仪某一路的状态
        :param card_index: 设备索引号
        :param channel: 设备通道号
        :return:
        """
        can_status = ZCAN_STAT()
        if self._canfd.VCI_ReadCANStatus(self._device_type, card_index, channel, byref(can_status)) != 1:
            raise Exception("Cant't get CAN status from  device id {} channel {} ".format(str(card_index),
                                                                                          str(channel)))
        else:
            return can_status

    def _SetReference(self, card_index, channel, ref, data):
        """
        设置设备的相应参数
        :param card_index: 设备索引号
        :param channel: 设备通道号
        :param ref: 参数类型, =18, 设置波特率
        :param data:
        :return:
        """
        if self._canfd.VCI_SetReference(self._device_type, card_index, channel, ref, byref(data)) != 1:
            raise Exception("Can't Set Reference {} to device id {} channel {}!".format(str(ref),
                                                                                        str(card_index),
                                                                                        str(channel)))

    def _StartCAN(self, card_index, channel):
        """
        启动CAN分析仪的某一路通道
        :param card_index: 设备索引号
        :param channel: 设备通道号
        :return:
        """
        if self._canfd.VCI_StartCAN(self._device_type, card_index, channel) != 1:
            raise Exception("Start CAN device id {} channel {} failed!".format(str(card_index),
                                                                               str(channel)))

    def _ResetCAN(self, card_index, channel):
        """
        复位CAN分析仪的某一路通道
        :param card_index: 设备索引号
        :param channel: 设备通道号
        :return:
        """
        if self._canfd.VCI_ResetCAN(self._device_type, card_index, channel) != 1:
            raise Exception("Reset CAN device id {} channel {} failed!".format(str(card_index),
                                                                               str(channel)))

    def _GetReceiveNum(self, card_index, channel):
        """
        CAN分析仪某一通道数据缓冲区中接收到但尚未被读取的帧数量
        :param card_index:
        :param channel:
        :return: 帧数量
        """
        return self._canfd.VCI_GetReceiveNum(self._device_type, card_index, channel)

    def _ClearBuffer(self, card_index, channel):
        """
        清空指定CAN分析仪某一通道的缓冲区
        :param card_index:
        :param channel:
        :return:
        """
        if self._canfd.VCI_ClearBuffer(self._device_type, card_index, channel) != 1:
            raise Exception("Cant' clear buffer for device id {} channel {}!".format(str(card_index),
                                                                                     str(channel)))

    def _TransmitFD(self, card_index, channel, msg, count=1):
        """
        发送函数CAN-FD数据
        :param card_index:
        :param channel:
        :param msg:
        :param count: 要发送的帧数
        :return: 实际发送成功的帧数
        """
        frame_number = self._canfd.VCI_TransmitFD(self._device_type, card_index, channel, byref(msg), count)
        return frame_number

    def _Receive(self, card_index, channel, msg, timeout=2):
        """
        从指定的设备CAN分析仪某个通道的接收缓冲区中读取数据
        :param card_index:
        :param channel:
        :param msg:
        :param timeout:
        :return: 实际读取到的帧数
        """
        frame_number = self._canfd.VCI_Receive(self._device_type, card_index, channel, msg, 100, timeout)
        return frame_number

    def _ReceiveFD(self, card_index, channel, msg, timeout=2):
        """
        从指定的设备CAN分析仪某个通道的接收缓冲区中读取CAN-FD数据
        :param card_index:
        :param channel:
        :param msg:
        :param timeout:
        :return:
        """
        frame_number = self._canfd.VCI_ReceiveFD(self._device_type, card_index, channel, msg, 1000, timeout)
        return frame_number


if __name__ == "__main__":
    fd = CanAnalyze_ZLG(0x04cc, 0x1240)
    fd.GetDevicesInfo()
    fd.Start(0, 0)
    fd.send(0, 0, "")
    #fd = CanFD()

    """
    {'C8AA17E19B58011900F5': {'device_index': 0, 'hmv': '0x100', 'fwv': '0x107', 'drv': '0x100', 'api': '0x100', 'irq': '0x0', 'chn': '0x2', 'channel': {0: {'init': False, 'receive': False}, 1: {'init': False, 'receive': False}}}}
    """
    pass