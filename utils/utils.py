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


def hexStringTobytes(string):
    """
    字符串数据转化为bytes类型数据
    :param string:
    :return:
    """
    string = string.replace(" ", "")
    return bytes.fromhex(string)


def print_hex(data):
    """
    打印byte类型数据
    :param data:
    :return:
    """
    l = [hex(int(i)) for i in data]
    print(" ".join(l))


def crc16(bytes):
    """ crc16的校准 """
    crc = 0xffff
    for byte in bytes:
        crc = ((crc >> 8) | (crc << 8)) & 0xFFFF
        crc ^= byte
        crc ^= ((crc & 0xff) % 256) >> 4
        crc ^= ((crc << 8) << 4) & 0xFFFF
        crc ^= ((crc & 0xff) << 4) << 1
        #print("byte = 0x%x" % byte)
        #print("crc = 0x%x" % crc)

    #print("crc total = 0x%x" % crc)
    return crc


def json_bottom_dict(data, dic):
    """
    获取json数据格式中最底层的key，val组成的字典
    :param data:
    :param dic:
    :return:
    """
    if isinstance(data, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in data:
            if isinstance(data[key], dict):  # 如果dic_json[key]依旧是字典类型
                # print("****key--：%s value--: %s" % (key, data[key]))
                json_bottom_dict(data[key], dic)
                # dic[key] = dic_json[key]
            else:
                # print("****key--：%s value--: %s" % (key, data[key]))
                dic[key] = data[key]


if __name__ == '__main__':
    pass
