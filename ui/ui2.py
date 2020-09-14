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

"""
import wx
from pubsub import pub
#from wx.lib.pubsub import pub

class MyFrame(wx.Frame):
    def __init__(self,parent=None):
        super(MyFrame, self).__init__(parent,-1,"文本框",size=(300,150))
        panel = wx.Panel(self,-1)
        self.button = wx.Button(panel,-1,"确定",pos=(10,10))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.button.SetDefault()  #将按钮设置为默认按钮，不然会是选中状态，边框不同
        self.inputText = wx.TextCtrl(panel,-1,"",pos=(100,10),size=(150,-1),style=wx.TE_READONLY)
        #订阅主题，接收这个主题的信息
        #pub.subscribe(callable, topic)
        pub.subscribe(self.recive, 'object.added')

    def OnClick(self,event):
        #发布主题，向这个主题发送信息
        pub.sendMessage('object.added', data=42, extra1='hello!')
        pub.sendMessage('object.added', data=23, extra1='hello!', extra2=[2, 3, 5, 7, 11, 13, 17, 19, 23])

    def recive(self, data, extra1, extra2=None):
        print(data)
        print(extra1)
        if extra2:
            print(extra2)
        self.inputText.Value = str(data)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
"""

"""
import wx
from pubsub import pub
from time import sleep
import threading
import sys


# 耗时长的代码
def workproc():
    sum_x = 0
    for i in range(1, 101):
        sum_x = sum_x + i
        sleep(0.1)
        pub.sendMessage("update", mstatus='计算{} , 合计 {}'.format(i, sum_x))
    return sum_x


# 线程调用耗时长代码
class WorkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        pub.sendMessage("update", mstatus='workstart')
        result = workproc()
        sleep(2)
        pub.sendMessage("update", mstatus='计算完成，结果 {}'.format(result))
        pub.sendMessage("update", mstatus='workdone')


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        self.st = wx.StaticText(pnl, label="分析工具 V 2019", pos=(25, 25))
        font = self.st.GetFont()
        font.PointSize += 5
        font = font.Bold()

        self.st.SetFont(font)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("启动完成!")

        pub.subscribe(self.updateDisplay, "update")

    def makeMenuBar(self):

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        # helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
        #         "Help string shown in status bar for this menu item")
        self.startItem = fileMenu.Append(-1, "开始",
                                         "开始计算")
        fileMenu.AppendSeparator()
        self.exitItem = fileMenu.Append(-1, "退出",
                                        "退出")

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(-1, "关于",
                                    "WxPython 界面与线程通讯的例子")

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(fileMenu, "工作")
        self.menuBar.Append(helpMenu, "信息")

        # Give the menu bar to the frame
        self.SetMenuBar(self.menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler functin will be called.
        self.Bind(wx.EVT_MENU, self.OnStart, self.startItem)
        self.Bind(wx.EVT_MENU, self.OnExit, self.exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)
        sys.exit()

    def OnStart(self, event):
        self.work = WorkThread()

    def OnAbout(self, event):
       
        wx.MessageBox("分析工具 v2019",
                      "关于",
                      wx.OK | wx.ICON_INFORMATION)

    def updateDisplay(self, mstatus):
        if mstatus.find("workstart") >= 0:
            self.SetStatusText('开始计算，代码不提供中断线程语句，请等待计算结束！')
            self.startItem.Enable(False)
            self.exitItem.Enable(False)
        if mstatus.find("workdone") >= 0:
            self.SetStatusText('完成！')
            self.startItem.Enable(True)
            self.exitItem.Enable(True)
        else:
            self.st.SetLabel(mstatus)


if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='分析工具')
    frm.Show()
    app.MainLoop()
"""


import wx
#from wx.lib.pubsub import pub
from pubsub import pub


class Student():
    def __init__(self):
        self.__Name = None
        # 注册订阅事件
        pub.subscribe(self.__UpdateName, 'nameEvntTopic')

    def SetName(self, name):
        self.__Name = name

    # 订阅事件
    def __UpdateName(self, data):
        if self.__Name == 'NameA':
            print('You can not give me a new name as my name is ', self.__Name)
            return
        else:
            print('I change name to ', data["name"])
        self.__Name = data["name"]


# 事件没有被注册时候，统一转到该函数处理
def onTopicNeverCreated(eventTopicData):
    print(eventTopicData)


if __name__ == '__main__':
    stuA = Student()
    stuA.SetName('NameA')
    stuB = Student()
    stuB.SetName('NameB')

    # 发布消息

    data = {'name': "David", 'age': 18}
    pub.sendMessage('nameEvntTopic', data=data)

    # 发布一个不存在的事件
    #pub.sendMessage('NoneEvntTopic', ['NewName', 'Age'], onTopicNeverCreated)
    pass
