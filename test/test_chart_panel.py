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


class TestPanel0(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        #self.plot()

    def plot(self, y):
        #x = np.linspace(0, 2 * np.pi)  # 创建等差素列, 数据开始点为0, 数据结束点为2Pi，样本数量默认50
        #y = np.sin(x)
        print("test-----------------")
        self.cla()

        x = np.arange(10)
        self.axes.plot(x, y)
        self.UpdatePlot()


class TestPanel1(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建一个画图板和一个画图区
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        self.plot()

    def plot(self, *args, **kwargs):
        # 准备数据
        x = np.arange(10)  # 创建固定步长的列表，起点是0，终点是9，步长为1
        y = np.random.randn(10)  # 返回一组10个服从标准正态分布的随机样本值，作为列表

        # 创建标签
        self.axes.set_title('Scatter Plot')  # 设置标题
        self.axes.set_xlabel('X')  # 设置X轴标签
        self.axes.set_ylabel('Y')  # 设置Y轴标签

        # 显示所有打开的画图板
        self.axes.scatter(x, y, color='red', marker='+')
        self.UpdatePlot()


class TestPanel2(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建画图板和画图区，重新设置了图形的大小
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        #self.plot()

    def plot(self, y):
        self.cla()
        #np.random.seed(1)  # 设置固定随机数生成时所用算法开始的整数值, 导致每次随机数相同
        #x = np.arange(6)  # 创建固定步长的列表，起点是0，终点是4，步长为1
        #y = np.random.randn(6)  # 返回一组5个服从标准正态分布的随机样本值，作为列表

        x = ['cpu0', 'cpu1', 'cpu2', 'cpu3', 'cpu4', 'cpu5']
        self.axes.axhline(0, color='gray', linewidth=2.0)                 # 在水平方向上画线
        self.axes.bar(x, y, color='lightblue', align='center')  # 绘制水平方向上柱状图
        self.UpdatePlot()


class TestPanel3(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建画图板和画图区，重新设置了图形的大小
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        self.plot()

    def plot(self):
        np.random.seed(19680801)                        # 随机数生成时所用算法开始的整数值, 导致每次随机数相同

        n_bins = 10
        x = np.random.randn(1000, 3)

        # 在绘图区1中绘图
        colors = ['red', 'tan', 'lime']
        self.axes.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)   # 绘制直方图 （传统的直方图，多个数据条行图排排列）
        self.axes.legend(prop={'size': 10})                       # 设置图例
        self.axes.set_title('bars with legend')                   # 设置绘图区1标题

        self.UpdatePlot()


class TestPanel4(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建画图板和画图区，重新设置了图形的大小
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        self.plot()

    def plot(self):
        np.random.seed(19680801)  # 随机数生成时所用算法开始的整数值, 导致每次随机数相同

        n_bins = 10
        x = np.random.randn(1000, 3)

        # 在绘图区2中绘图
        self.axes.hist(x, n_bins, density=True, histtype='barstacked')  # 绘制直方图 （多个数据相互堆叠）
        self.axes.set_title('stacked bar')  # 设置绘图区2标题

        self.UpdatePlot()


class TestPanel5(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建画图板和画图区，重新设置了图形的大小
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        #labels = 'Frog', 'Hog', 'Dog', 'Log'
        #sizes = [15, 30, 45, 10]
        #self.plot(labels, sizes)

    def plot(self, labels, sizes):
        self.cla()
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        # 在绘图区1中绘图
        self.axes.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)       # autopct : 显示百分比, labels : 提供标签, shadow : 在饼图下面画阴影
        self.axes.axis('equal')           # 设置等比坐标轴
        # self.axes.legend(labels=labels, loc='upper right')            # 设置图例， 位置偏右偏上

        self.UpdatePlot()


class TestPanel6(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建画图板和画图区，重新设置了图形的大小
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        self.plot()

    def plot(self):
        # 准备数据
        np.random.seed(19680801)                 # 随机数生成时所用算法开始的整数值, 导致每次随机数相同

        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N)) ** 2     # 0 to 15 point radii
        print(x)
        print(y)
        print(colors)
        print(area)

        # 绘制散点图
        self.axes.scatter(x, y, s=area, c=colors, alpha=0.5)
        self.UpdatePlot()


class TestPanel7(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建画图板和画图区，重新设置了图形的大小
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        self.plot()

    def plot(self):
        x = np.arange(-5, 5, 0.1)
        y = np.arange(-5, 5, 0.1)
        xx, yy = np.meshgrid(x, y, sparse=True)
        z = np.sin(xx ** 2 + yy ** 2) / (xx ** 2 + yy ** 2)
        self.axes.contourf(x, y, z)

        self.UpdatePlot()


class ChartPanel(scrolledpanel.ScrolledPanel):
    """
    显示图表信息的面板
    """
    def __init__(self, parent):
        super().__init__(parent=parent)

        # 创建第一行Box
        # wx.ALL : 控件四周都增加宽度为x的空白，x取border参数的值
        # wx.EXPAND : 控件占满可用空间
        # proportion : 代表当容器大小变化时, 控件的大小变化，变化速度为proportion的值， =0为不发生变
        self.BoxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.MPL1_1 = TestPanel0(self)
        self.BoxSizer1.Add(self.MPL1_1, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)
        self.MPL1_2 = TestPanel1(self)
        self.BoxSizer1.Add(self.MPL1_2, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)
        self.MPL1_3 = TestPanel2(self)
        self.BoxSizer1.Add(self.MPL1_3, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)
        self.MPL1_4 = TestPanel3(self)
        self.BoxSizer1.Add(self.MPL1_4, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)

        # 创建第二行Box
        self.BoxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.MPL2_1 = TestPanel4(self)
        self.BoxSizer2.Add(self.MPL2_1, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)
        self.MPL2_2 = TestPanel5(self)
        self.BoxSizer2.Add(self.MPL2_2, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)
        self.MPL2_3 = TestPanel6(self)
        self.BoxSizer2.Add(self.MPL2_3, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)
        self.MPL2_4 = TestPanel7(self)
        self.BoxSizer2.Add(self.MPL2_4, proportion=2, border=5, flag=wx.ALL | wx.EXPAND)

        # 创建纵向容器
        self.BoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.BoxSizer.Add(self.BoxSizer1, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(self.BoxSizer2, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.SetSizer(self.BoxSizer)

        # 绑定事件处理
        self.Bind(EVT_CHART, self.OnChart)

        # 增加定时器，更新UI状态
        self._update_ui = wx.PyTimer(self.UpdateUI)
        self._update_ui.Start(1000)

        self._data_test = list(range(0, 100, 10))

    def UpdateUI(self):
        foo = ['1', '2', '3']
        index = choice(foo)
        print("index = ", index)
        if index == '1':
            val = [15, 30, 45, 10]

            a = np.random.randint(0, 15)
            val[0] -= a
            val[1] += a

            a = np.random.randint(0, 10)
            val[2] -= a
            val[3] += a

            evt = ChartEvent(
                name="DiskInfo",
                type="PieChart",
                sizes=val,
                labels=["Frogs", "Hogs", "Dogs", "Logs"]
            )

            wx.QueueEvent(self, evt)

        elif index == '2':
            val = np.random.randint(0, 100, 6)
            evt = ChartEvent(
                name="CpuInfo",
                type="BarChart",
                data=val,
                labels=["cpu0", "cpu1", "cpu2", "cpu3", "cpu4", "cpu5"]
            )

            wx.QueueEvent(self, evt)

        elif index == '3':

            print("y1 = ", self._data_test)
            a = np.random.randint(0, 100)
            print(a)
            print(self._data_test.pop())
            self._data_test.insert(0, a)
            #np.roll(a, 2)
            #np.left_shift(1, y)
            print("y2 = ", self._data_test)
            #np.append(y, a)

            y = self._data_test
            evt = ChartEvent(
                name="MemInfo",
                type="LineChart",
                data=y
            )

            wx.QueueEvent(self, evt)
        pass

    def OnChart(self, event):
        """
        包含自定义EVT_CHART的事件触发的处理
        :param event: 自定义的事件
        :return:
        """
        print("OnChart!!!")
        print(type(event))

        if event.type == "PieChart":
            print("name = ", event.name)
            print("type = ", event.type)
            print("sizes = ", event.sizes)
            print("labels = ", event.labels)
            self.MPL2_2.plot(event.labels, event.sizes)

        elif event.type == "BarChart":
            print("name = ", event.name)
            print("type = ", event.type)
            print("data = ", event.data)
            print("labels = ", event.labels)
            self.MPL1_3.plot(event.data)

        elif event.type == "LineChart":
            print("name = ", event.name)
            print("type = ", event.type)
            print("data = ", event.data)
            self.MPL1_1.plot(event.data)
        pass


if __name__ == '__main__':
    pass
