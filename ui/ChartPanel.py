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
from wx.lib import scrolledpanel

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.ticker import MultipleLocator, FuncFormatter
from matplotlib import pyplot
import pylab
import numpy as np

from collections import Iterable



class FigureCanvasBasePanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)

        """
        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        x = np.linspace(0, 2 * np.pi)  # 创建等差素列, 数据开始点为0, 数据结束点为2Pi，样本数量默认50
        y = np.sin(x)
        self.plot(x, y)
        """

    def UpdatePlot(self):
        """
        重新渲染，修改图形的任何属性后都必须重新调用来更新GUI界面
        :return:
        """
        self.FigureCanvas.draw()

    def plot(self, *args, **kwargs):
        """
        绘制画图区
        :param args:
        :param kwargs:
        :return:
        """
        self.axes.plot(*args, **kwargs)
        self.UpdatePlot()

    def scatter(self, *args, **kwargs):
        self.axes.scatter(*args, **kwargs)
        self.UpdatePlot()


    def loglog(self, *args, **kwargs):
        """
        在x和y轴上使用对数缩放比例绘制图
        :param args:
        :param kwargs:
        :return:
        """
        self.axes.loglog(*args, **kwargs)
        self.UpdatePlot()

    def semilogx(self, *args, **kwargs):
        """
        在x轴上使用对数缩放比例绘制图
        :param args:
        :param kwargs:
        :return:
        """
        self.axes.semilogx(*args, **kwargs)
        self.UpdatePlot()

    def semilogy(self, *args, **kwargs):
        """
        在y轴上使用对数缩放比例绘制图
        :param args:
        :param kwargs:
        :return:
        """
        ''''' #对数坐标绘图命令 '''
        self.axes.semilogy(*args, **kwargs)
        self.UpdatePlot()

    def set_title(self, title):
        """
        给图像添加一个标题
        :param title:
        :return:
        """
        self.axes.set_title(title)

    def set_xlabel(self, xlabel="X"):
        """
        设置x轴的标签
        :param xlabel:
        :return:
        """
        self.axes.set_xlabel(xlabel)

    def set_ylabel(self, ylabel="Y"):
        """
        设置y轴的标签
        :param ylabel:
        :return:
        """
        self.axes.set_ylabel(ylabel)

    def legend(self, *args, **kwargs):
        """
        设置图例
        :param args:
        :param kwargs:
        :return:
        """
        self.axes.legend(*args, **kwargs)

    def grid(self, on=True):
        """
        配制网格线，显示网格
        :param on:
        :return:
        """
        self.axes.grid(on)

    def xticker(self, major_ticker=1.0, minor_ticker=0.1):
        """
        设置X轴的刻度大小
        :param major_ticker:
        :param minor_ticker:
        :return:
        """
        self.axes.xaxis.set_major_locator(MultipleLocator(major_ticker))
        self.axes.xaxis.set_minor_locator(MultipleLocator(minor_ticker))

    def yticker(self, major_ticker=1.0, minor_ticker=0.1):
        """
        设置Y轴的刻度大小
        :param major_ticker:
        :param minor_ticker:
        :return:
        """
        self.axes.yaxis.set_major_locator(MultipleLocator(major_ticker))
        self.axes.yaxis.set_minor_locator(MultipleLocator(minor_ticker))

    def xlim(self, x_min, x_max):
        """
        设置X轴的显示范围
        :param x_min:
        :param x_max:
        :return:
        """
        self.axes.set_xlim(x_min, x_max)

    def ylim(self, y_min, y_max):
        """
        设置Y轴的显示范围
        :param y_min:
        :param y_max:
        :return:
        """
        self.axes.set_ylim(y_min, y_max)

    def savefig(self, *args, **kwargs):
        """
        保存图形到文件
        :param args:
        :param kwargs:
        :return:
        """
        self.Figure.savefig(*args, **kwargs)

    def cla(self):
        """
        清空原来的图形,再次画图前,必须调用该命令
        :return:
        """
        self.axes.clear()
        self.figure.set_canvas(self.FigureCanvas)
        self.UpdatePlot()


class TestPanel0(FigureCanvasBasePanel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        fig, ax = pyplot.subplots(figsize=pyplot.figaspect(2.5 / 2))
        self.figure = fig
        self.axes = ax
        self.FigureCanvas = FigureCanvas(self, -1, self.figure)

        x = np.linspace(0, 2 * np.pi)  # 创建等差素列, 数据开始点为0, 数据结束点为2Pi，样本数量默认50
        y = np.sin(x)
        self.plot(x, y)


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

        self.plot()

    def plot(self, *args, **kwargs):
        np.random.seed(1)  # 设置固定随机数生成时所用算法开始的整数值, 导致每次随机数相同
        x = np.arange(5)  # 创建固定步长的列表，起点是0，终点是4，步长为1
        y = np.random.randn(5)  # 返回一组5个服从标准正态分布的随机样本值，作为列表

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

        self.plot()

    def plot(self):
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
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














'''
CHART_LINE_TYPE = 0
CHART_BAR_TYPE = 1
CHART_PIE_TYPE = 2


class ChartPanel(scrolledpanel.ScrolledPanel):
    """
    显示图表信息的面板
    """
    def __init__(self, *args, **kwargs):
        super(ChartPanel, self).__init__(*args, **kwargs)

        self.SetBackgroundColour(wx.WHITE)

        self.sizer = wx.WrapSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        # self.timer = wx.PyTimer(self.PostData)
        # self.timer.Start(1000)

    def OnSize(self, event):
        """
        :type event: wx.SizeEvent
        """
        self.SetVirtualSize((event.GetSize().GetWidth(), self.GetVirtualSize().GetHeight()))
        self.Layout()
        self.Refresh()
        if self.CanScroll(wx.VERTICAL):
            self.SetupScrolling(scroll_x=False, scroll_y=True, scrollToTop=False)
        event.Skip()

    def OnClose(self, event):
        """
        :type event: wx.CloseEvent
        """
        event.Skip()

    def OnChart(self, event):
        """
        ChartEvt handler. event need parameters as follow:
            name, string: the chart name.
            chartType, int:
                0, LineChart
                1, BarChart
                2, PieChart
            xdata: work for BarChart
            ydata: work for LineChart and BarChart, for LineChart is int,
                for BarChart is Iterable int data with int/float/long
            data: work for PieChart, need be Iterable data with int/float/long
            labels: work for PieChart, need be Iterable with String
        :type event: ChartEvt
        """
        child = self.FindWindowByName(event.name)
        if child is None:
            child = self.AddChart(event)
        if child is not None:
            try:
                wx.QueueEvent(child, event.Clone())
                event.Skip()
            except RuntimeError:
                pass
            except Exception as e:
                wx.LogWarning("Chart Panel Get exceptions: {}".format(e))
        else:
            wx.LogError("Get/Create {} chart failed!".format(event.name))

    def OnChartCFG(self, event):
        """
        ChartCFGEvt handler. event need parameters as follow:

        :type event: ChartCfgEvt
        """
        child = self.FindWindowByName(event.name)
        if child is None:
            child = self.AddChart(event)
        if child is not None:
            wx.QueueEvent(child, event.Clone())
        else:
            wx.LogError("Get/Create {} chart failed!".format(event.name))

        event.Skip()

    def AddChart(self, event):
        """
        Add new chart for this panel. event need parameters as follow:
            name, string: the chart name.
            chartType, int:
                0, LineChart
                1, BarChart
                2, PieChart
            xdata: work for BarChart
            ydata: work for LineChart and BarChart, for LineChart is int,
                for BarChart is Iterable int data with int/float/long
            data: work for PieChart, need be Iterable data with int/float/long
            labels: work for PieChart, need be Iterable with String
        :type event: ChartEvt
        :rtype: LineChartPanel or BarChartPanel or PieChartPanel or FigureCanvasBasePanel
        """
        name = event.name
        if event.chartType == CHART_LINE_TYPE:
            chartType = LineChartPanel
        elif event.chartType == CHART_BAR_TYPE:
            chartType = BarChartPanel
        elif event.chartType == CHART_PIE_TYPE:
            chartType = PieChartPanel
        else:
            return

        child = chartType(self, wx.ID_ANY, Figure(), name)
        self.sizer.Add(child, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Layout()
        self.Refresh()
        if self.CanScroll(wx.VERTICAL):
            self.SetupScrolling(scroll_x=False, scroll_y=True, scrollToTop=False)
        return child

    def PostData(self):
        for i in range(0, 6, 1):
            t = xrange(0, 10, 1)
            s = np.random.random()
            r = np.random.random_integers(1, 100, 10)
            p = np.random.random(4)
            LineChartEvt = ChartEvt(chartType=CHART_LINE_TYPE,
                                    name="TestLineChart"+str(i),
                                    ydata=s)
            BarChartEvt = ChartEvt(chartType=CHART_BAR_TYPE,
                                   name="TestBarChart"+str(i),
                                   xdata=t,
                                   ydata=r)
            PieChartEvt = ChartEvt(chartType=CHART_PIE_TYPE,
                                   name="TestPieChart"+str(i),
                                   data=p,
                                   labels=["a", "b", "c", "d"])
            wx.QueueEvent(self, LineChartEvt)
            wx.QueueEvent(self, BarChartEvt)
            wx.QueueEvent(self, PieChartEvt)



class FigureCanvasBasePanel(FigureCanvas):
    """
    FigureCanvs 这是一个wxWidgets对象，继承自wxPanel
    """
    def __init__(self, parent, wx_id=wx.ID_ANY, figure=Figure(), name=''):
        super(FigureCanvasBasePanel, self).__init__(parent, wx_id, figure)
        self.figure = figure
        self.name = name
        self.axes = self.figure.add_subplot(111)
        self.SetMaxSize((480, 360))
        self.SetMinSize((480, 360))
        self.draw_flag = Event()
        self.chart_cfg = {
            "relim": False,
            "visible_only": False,
            "grid": True,
            "legend": False,
            "title": self.name
        }
        self._data_updated = False

        self.xdata = None
        self.ydata = None

        self.axes.grid(self.chart_cfg['grid'])
        self.axes.set_title(self.name)
        self.axes.get_yaxis().set_major_formatter(FuncFormatter(y_fmt))
        self.SetName(self.name)

        self.Bind(EVT_CHART, self.OnChart)
        self.Bind(EVT_CHART_CFG, self.OnChartCFG)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def UpdateData(self, event):
        """
        Need override. This method is for update data for visual.
        :type event: ChartEvt
        """
        pass

    def OnChart(self, event):
        """
        :type event: ChartEvt
        """
        self.draw_flag.set()
        try:
            self.UpdateData(event)
        except Exception, msg:
            wx.LogWarning("{} update failed, error msg: {},\n\tevent body: {}".format(
                self.name,
                msg,
                event.__dict__
            ))
        else:
            self._isDrawn = False

    def OnChartCFG(self, event):
        """
        Need override.
        :type event: ChartCfgEvt
        """
        self.draw_flag.set()
        self.chart_cfg.update(event.cfg)

    def OnIdle(self, event):
        """
        :type event: wx.IdleEvent
        """
        if self.draw_flag.is_set():
            self._DoDraw()
        event.Skip()

    def _onPaint(self, evt):
        """
        Called when wxPaintEvt is generated
        """

        # DEBUG_MSG("_onPaint()", 1, self)
        drawDC = wx.PaintDC(self)
        if not self._isDrawn:
            self.draw(drawDC=drawDC)
        else:
            self.gui_repaint(drawDC=drawDC)
        # For memory leak on WxPython 3.0.2 and Python 2.7, disable the Destroy method.
        # drawDC.Destroy()
        evt.Skip()

    def _onSize(self, evt):
        """
                Called when wxEventSize is generated.

                In this application we attempt to resize to fit the window, so it
                is better to take the performance hit and redraw the whole window.
                """

        # DEBUG_MSG("_onSize()", 2, self)
        sz = self.GetParent().GetSizer()
        if sz:
            si = sz.GetItem(self)
        if sz and si and not si.Proportion and not si.Flag & wx.EXPAND:
            # managed by a sizer, but with a fixed size
            size = self.GetMinSize()
        else:
            # variable size
            size = self.GetClientSize()
        if getattr(self, "_width", None):
            if size == (self._width, self._height):
                # no change in size
                return
        self._width, self._height = size
        if self._width <= 0:
            self._width = 1
        if self._height <= 0:
            self._height = 1
        # Create a new, correctly sized bitmap
        self.bitmap = wx.Bitmap(width=self._width, height=self._height)

        self._isDrawn = False

        if self._width <= 1 or self._height <= 1:
            return  # Empty figure

        dpival = self.figure.dpi
        winch = self._width / dpival
        hinch = self._height / dpival
        self.figure.set_size_inches(winch, hinch, forward=False)

        # Rendering will happen on the associated paint event
        # so no need to do anything here except to make sure
        # the whole background is repainted.
        self.Refresh(eraseBackground=False)
        super(FigureCanvasBasePanel, self).resize_event()


    def _DoDraw(self):
        if not self.draw_flag.is_set():
            return
        try:
            # Relimit
            self._DoRelim()

            # Grid
            self._DoGrid()

            # Legend
            self._DoLegend()

            # Update chart title
            self._DoUpdateTitle()

            # Update label for x and y. At WxAgg need big resolution. Disable it now.
            # self._DoUpdateXYLabel()
        except Exception, msg:
            wx.LogWarning("{} draw failed, error msg: {},\n\tchart cfg: {},\n\tdata: {}".format(
                self.name,
                msg,
                self.chart_cfg,
                (self.xdata, self.ydata)
            ))
            return
        else:
            self.Refresh(eraseBackground=True)
        finally:
            self.draw_flag.clear()

    def _DoRelim(self):
        fixed_lim = False
        if 'xlim' in self.chart_cfg:
            self.axes.set_xlim(self.chart_cfg['xlim'])
            fixed_lim = True
        if 'ylim' in self.chart_cfg:
            self.axes.set_ylim(self.chart_cfg['ylim'])
            fixed_lim = True
        if not fixed_lim and self.chart_cfg['relim'] and self._data_updated:
            self.axes.relim(self.chart_cfg['visible_only'])
            self._data_updated = False
            self.axes.autoscale_view()

    def _DoGrid(self):
        self.axes.grid(self.chart_cfg['grid'])

    def _DoLegend(self):
        if self.chart_cfg['legend']:
            self.axes.legend()

    def _DoUpdateTitle(self):
        if 'title' in self.chart_cfg:
            self.axes.set_title(self.chart_cfg['title'])

    def _DoUpdateXYLabel(self):
        if 'xlabel' in self.chart_cfg:
            wx.LogDebug('{} set XLable: {}'.format(
                self.name,
                self.chart_cfg['xlabel']
            ))
            self.axes.set_xlabel(self.chart_cfg['xlabel'])
        if 'ylabel' in self.chart_cfg:
            wx.LogDebug('{} set YLable: {}'.format(
                self.name,
                self.chart_cfg['ylabel']
            ))
            self.axes.set_ylabel(self.chart_cfg['ylabel'])

    def draw(self, drawDC=None):
        """
        Render the figure using agg.
        """
        super(FigureCanvas, self).draw()

        buff = self.get_renderer().tostring_rgb()
        self.bitmap.CopyFromBuffer(buff, wx.BitmapBufferFormat_RGB)
        self._isDrawn = True
        self.gui_repaint(drawDC=drawDC, origin='WXAgg')
        del buff

    def gui_repaint(self, drawDC=None, origin='WX'):
        """
        Performs update of the displayed image on the GUI canvas, using the
        supplied wx.PaintDC device context.

        The 'WXAgg' backend sets origin accordingly.
        """
        # DEBUG_MSG("gui_repaint()", 1, self)
        if self.IsShownOnScreen() and self.bitmap.IsOk():
            if not drawDC:
                # not called from OnPaint use a ClientDC
                # drawDC = wx.ClientDC(self)
                return

            # following is for 'WX' backend on Windows
            # the bitmap can not be in use by another DC,
            # see GraphicsContextWx._cache
            if wx.Platform == '__WXMSW__' and origin == 'WX':
                img = self.bitmap.ConvertToImage()
                bmp = img.ConvertToBitmap()
                drawDC.DrawBitmap(bmp, 0, 0)
            else:
                drawDC.DrawBitmap(self.bitmap, 0, 0)


class LineChartPanel(FigureCanvasBasePanel):
    def __init__(self, *args, **kwargs):
        super(LineChartPanel, self).__init__(*args, **kwargs)
        self.xdata = np.arange(-10, 0, 1)
        self.ydata = deque(np.zeros(10), 10)
        self.line, = self.axes.plot(self.xdata, self.ydata, )
        self.chart_cfg['relim'] = True

    def UpdateData(self, event):
        if isinstance(event.data['ydata'], Iterable):
            for i in event.data['ydata']:
                self.ydata.append(i)
        elif isinstance(event.data['ydata'], (int, float, long)):
            self.ydata.append(event.data['ydata'])
        else:
            return
        self.line.set_ydata(self.ydata)
        self._data_updated = True


class BarChartPanel(FigureCanvasBasePanel):
    def __init__(self, *args, **kwargs):
        super(BarChartPanel, self).__init__(*args, **kwargs)
        self.xdata = None
        self.ydata = list()
        self.axes._hold = False

    def UpdateData(self, event):
        self.xdata = event.data['xdata']
        for data in event.data['ydata']:
            if isinstance(data, (int, float, long)):
                self.ydata.append(data)
            elif isinstance(data, (str, unicode)):
                if data.isdigit():
                    self.ydata.append(float(data))
                else:
                    continue
            if len(self.ydata) > len(event.data['ydata']):
                self.ydata.pop(0)
        if len(self.xdata) != len(self.ydata):
            wx.LogWarning("{} get data format error. Data body: xdata: {}, ydata: {}".format(
                self.name,
                event.data['xdata'],
                event.data['ydata']
            ))
            return
        self.axes.bar(self.xdata, self.ydata, label=self.xdata)


class PieChartPanel(FigureCanvasBasePanel):
    def __init__(self, *args, **kwargs):
        super(PieChartPanel, self).__init__(*args, **kwargs)

    def UpdateData(self, event):
        self.axes.cla()
        self.axes.axis('equal')
        self.axes.pie(event.data['ydata'],
                      labels=event.data['xdata'],
                      autopct=lambda p: "{:.0f}\n({:.1f}%)".format(p*sum(event.data['ydata'])/100, p))
        self._data_updated = True
'''

if __name__ == '__main__':
    pass
