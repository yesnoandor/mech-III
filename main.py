import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="菜单", size=(400, 300))
        self.Center()  # 窗口居中
        self.text = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)  # 创建一个多行文本控件
        vbox = wx.BoxSizer(wx.VERTICAL)  # 创建一个垂直布局管理器
        self.SetSizer(vbox)  # 为此窗口添加此布局管理器
        vbox.Add(self.text, 1, flag=wx.EXPAND | wx.ALL, border=1)  # 将文本添加进当前窗口

        menubar = wx.MenuBar()  # 创建一个菜单栏，
        self.SetMenuBar(menubar)  # 给窗口添加此菜单栏
        file_menu = wx.Menu()  # 创建一个菜单
        menubar.Append(file_menu, 'File')  # 在菜单栏上添加此菜单

        file_menu.Append(id=wx.ID_NEW, item='New', helpString='new file')  # 往菜单中添加一个菜单项
        self.Bind(wx.EVT_MENU, self.on_newitem_click, id=wx.ID_NEW)  # 为此菜单项添加事件处理
        file_menu.AppendSeparator()  # 分割线

        edit_menu = wx.Menu()  # 创建一个edit_menu菜单
        file_menu.AppendSubMenu(edit_menu, "Edit")  # file_menu上面添加edit_menu菜单
        copy_item = wx.MenuItem(edit_menu, 100, text="Copy", kind=wx.ITEM_NORMAL)  # 创建copy_item菜单项
        edit_menu.Append(copy_item)  # edit_menu菜单添加copy_item菜单项

        cut_item = wx.MenuItem(edit_menu, 101, text="Cut", kind=wx.ITEM_NORMAL)  # 创建cut_item菜单项
        edit_menu.Append(cut_item)  # edit_menu菜单添加cut_item菜单项

        paste_item = wx.MenuItem(edit_menu, 102, text="Paste", kind=wx.ITEM_NORMAL)  # 创建paste_item菜单项
        edit_menu.Append(paste_item)  # edit_menu菜单添加paste_item菜单项
        self.Bind(wx.EVT_MENU, self.on_editmenu_click, id=100, id2=102)  # 为这3个添加事件处理

    def on_newitem_click(self, event):
        self.text.SetLabel('单击【New】菜单')

    def on_editmenu_click(self, event):
        event_id = event.GetId()
        if event_id == 100:
            self.text.SetLabel('单击【Copy】菜单')
        elif event_id == 101:
            self.text.SetLabel('单击【Cut】菜单')
        else:
            self.text.SetLabel('单击【Paste】菜单')


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("quit")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()