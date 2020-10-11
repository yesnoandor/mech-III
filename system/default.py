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


DEFAULT_SYSTEM_CONFIG = {
    "module_server": {
        "ip": "192.168.1.105",
        "port": 9988
    },

    "module_monitor": {
        "MODULE_CAN": [
            "EMC_MODULE_CAN0",
            "EMC_MODULE_CAN1",
            "EMC_MODULE_CAN2",
            "EMC_MODULE_CAN3",
            "EMC_MODULE_CAN4",
            "EMC_MODULE_CAN5",
            "EMC_MODULE_CAN6",
        ],
        "MODULE_ADC": [
            "EMC_MODULE_ADC0",
            "EMC_MODULE_ADC1",
            "EMC_MODULE_ADC2",
            "EMC_MODULE_ADC3",
            "EMC_MODULE_ADC4",
            "EMC_MODULE_ADC5",
            "EMC_MODULE_ADC6",
            "EMC_MODULE_ADC7"
        ],
        "MODULE_SENSOR": [
            "EMC_MODULE_SENSOR_INA",
            "EMC_MODULE_SENSOR_TMP0",
            "EMC_MODULE_SENSOR_TMP1",
            "EMC_MODULE_SENSOR_TMP2",
            "EMC_MODULE_SENSOR_TMP3"
        ]
    },

    "can_analyzer": {
        "vendor_id": 0x04cc,
        "product_id": 0x1240
    },
}

"""
DEFAULT_EVENT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "date": {"type": "string"},
        "mod": {"type": "string"},
        "error": {"type": "string"},
        "warning": {"type": "string"},
        "normal": {"type": "string"}
    },
    "required": ["id", "date", "mod"],
    "dependencies": {
        "oneOf": {
            "mod": [
                "error"
            ],
            "mod": [
                "warning"
            ],
            "mod": [
                "info"
            ]
        }
    }
}
"""

if __name__ == '__main__':
    pass
