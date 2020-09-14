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
import wx
from wx.lib import newevent

ModuleEvent, EVT_MODULE = newevent.NewEvent()


class ModulePanelBase(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(ModulePanelBase, self).__init__(*args, **kwargs)
        """
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(EVT_MOD, self.OnMod)
        self.Bind(EVT_MOD_CLEAR, self.OnModClear)
        self.Bind(EVT_SSH_CONSOLE_LOG, self.OnSshConsole)
        self.Bind(EVT_CONSOLE_LOG, self.OnConsole)
        self.Bind(EVT_FLEX_DIA, self.OnFlexDia)
        self.Bind(EVT_CAN_MSG, self.OnCanMSG)
        """

    def OnModClear(self, event):
        """
        Need override
        """
        event.Skip()

    def OnMod(self, event):
        """
        Need override
        """
        event.Skip()

    def OnSize(self, event):
        """
        Need override
        """
        event.Skip()

    def OnSshConsole(self, event):
        """
        Need override
        """
        event.Skip()

    def OnConsole(self, event):
        """
        Need override
        """
        event.Skip()

    def OnFlexDia(self, event):
        """
        Need override
        """
        event.Skip()

    def OnCanMSG(self, event):
        """
        Need voerride
        """
        event.Skip()

    def GetOutputPanel(self):
        """
        Need override
        """
        return None


players = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
           ('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
           ('Ganguly', '8000', '50')]


class ModuleListCtrl(wx.ListCtrl):
    def __init__(self, *args, **kwargs):
        super(ModuleListCtrl, self).__init__(*args, **kwargs)

        self.AddColumns()

        for i in players:
            self.AddItem(i)

        # 绑定事件处理
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(EVT_MODULE, self.OnModule)

        # 增加定时器，更新UI状态
        self._update_ui = wx.PyTimer(self.UpdateUI)
        self._update_ui.Start(1000)

    def UpdateUI(self):
        print(self._update_ui)

        data = (1, "hello", 33)
        name = "san"

        evt = ModuleEvent(
            name=name,
            data=data,
        )

        wx.QueueEvent(self, evt)

        pass

    def AddColumns(self):
        """
        增加列格式，包含列标题
        :return: None
        """
        width = self.GetSize().GetWidth()
        self.InsertColumn(0, '', width=width * 0.05)
        self.InsertColumn(1, 'Name', wx.LIST_FORMAT_CENTER, width=width * 0.25)
        self.InsertColumn(2, 'Log', wx.LIST_FORMAT_CENTER, width=width * 0.7)
        print("width = ", self.GetSize().GetWidth())

    def AddItem(self, item):
        """
        增加行记录
        :param item: 一条行记录
        :return: None
        """
        index = self.InsertItem(sys.maxsize, item[0])
        self.SetItem(index, 1, item[1])
        self.SetItem(index, 2, item[2])

    def OnSize(self, event):
        """
        包含多列的组件大小变化的事件触发的处理
        :param event: 大小变化的事件
        :return: None
        """
        print(type(event))
        width = self.GetSize().GetWidth()

        self.SetColumnWidth(0, width * 0.05)
        self.SetColumnWidth(1, width * 0.25)
        self.SetColumnWidth(2, width * (1 - 0.05 - 0.25))

        event.Skip()
        pass

    def OnModule(self, event):
        """
        包含自定义EVT_MODULE的事件触发的处理
        :param event: 自定义的事件
        :return:
        """
        print("OnModule!!!")
        print(type(event))
        print("name = ", event.name)
        print("data = ", event.data)
        pass


class ModulePanel(wx.Panel):
    """
    显示所有模组信息的面板
    """
    def __init__(self, parent):
        super(ModulePanel, self).__init__(parent=parent)

        # 创建一个容器，容器中的控件横向排列
        self.box = wx.BoxSizer(wx.HORIZONTAL)

        # 创建一个包含多列的组件
        self.list = ModuleListCtrl(parent=self, style=wx.LC_REPORT | wx.BORDER_NONE | wx.LC_HRULES | wx.LC_VRULES | wx.LC_SINGLE_SEL)

        # 将多列组件放入容器中
        self.box.Add(self.list, 1, wx.EXPAND)
        # 使布局有效
        self.SetSizer(self.box)

        # 调整窗口大小以适合其最佳大小
        self.Fit()

        # 绑定事件处理
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnClose(self, event):
        event.Skip()
        pass

    """
    def OnSize(self, event):
        event.Skip()
        pass
    """


if __name__ == '__main__':
    pass
