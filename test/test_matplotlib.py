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


import numpy as np
from numpy import math
from matplotlib import pyplot


def matplotlib_test1():
    """
    绘制线图 （Matlab风格接口）
    :return:
    """
    # 创建画图板
    fig = pyplot.figure()

    # 创建绘图区
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(224)

    # 准备数据
    x = np.linspace(0, 2*np.pi)       # 创建等差素列, 数据开始点为0, 数据结束点为2Pi，样本数量默认50
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # 在绘图区绘图
    ax1.plot(x, y_sin)
    ax2.plot(x, y_sin, 'go--', linewidth=2, markersize=12)      # fmt = '[marker][line][color]', "go--" = 绿色圆形虚线
    ax3.plot(x, y_cos, color='red', marker='+', linestyle='dashed')

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test2():
    """
    绘制线图 （面向对象接口）
    :return:
    """
    # 准备数据
    x = np.linspace(0, 10, 200)          # 创建等差素列, 数据开始点为0, 数据结束点为10，样本数量200
    x2 = np.linspace(0, 2 * np.pi, 200)  # 创建等差素列, 数据开始点为0, 数据结束点为2Pi，样本数量200
    y2 = np.sin(x)

    data_obj = {'x': x,
                'y1': 2 * x + 1,
                'y2': 3 * x + 1.2,
                'mean': 0.5 * x * np.cos(2 * x) + 2.5 * x + 1.1}

    # 创建一个画图板和两个画图区
    fig, (ax1, ax2) = pyplot.subplots(1, 2, sharex=True)

    # 填充两条线之间的颜色
    ax1.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)

    # 在绘图区1中绘图
    ax1.plot('x', 'mean', color='black', data=data_obj)

    # 在绘图区2中绘图
    ax2.plot(x2, y2, 'g-')

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test3():
    """
    绘制散点图
    :return:
    """
    # 准备数据
    x = np.arange(10)                   # 创建固定步长的列表，起点是0，终点是9，步长为1
    y = np.random.randn(10)             # 返回一组10个服从标准正态分布的随机样本值，作为列表

    # 创建一个画图板和一个画图区
    fig, ax = pyplot.subplots()

    # 创建标签
    ax.set_title('Scatter Plot')        # 设置标题
    ax.set_xlabel('X')                  # 设置X轴标签
    ax.set_ylabel('Y')                  # 设置Y轴标签

    # 绘制散点图
    ax.scatter(x, y, color='red', marker='+')

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test4():
    """
    绘制柱状图
    :return:
    """
    # 准备数据
    np.random.seed(1)                   # 设置固定随机数生成时所用算法开始的整数值, 导致每次随机数相同
    x = np.arange(5)                    # 创建固定步长的列表，起点是0，终点是4，步长为1
    y = np.random.randn(5)              # 返回一组5个服从标准正态分布的随机样本值，作为列表

    # 创建一个画图板和三个画图区，重新设置了图形的大小
    fig, axes = pyplot.subplots(ncols=3, figsize=pyplot.figaspect(1. / 2))

    # 在绘图区1中绘图
    axes[0].axhline(0, color='gray', linewidth=2)               # 在水平方向上画线
    axes[0].bar(x, y, color='lightblue', align='center')        # 绘制水平方向上柱状图

    # 在绘图区2中绘图
    axes[1].axvline(0, color='gray', linewidth=2)               # 在垂直方向上画线
    axes[1].barh(x, y, color='lightblue', align='center')       # 绘制垂直方向上柱状图

    # 在绘图区3中绘图
    axes[2].axhline(0, color='gray', linewidth=2)                       # 在水平方向上画线
    vert_bars = axes[2].bar(x, y, color='lightblue', align='center')    # 绘制水平方向上柱状图
    for bar, height in zip(vert_bars, y):
        if height < 0:                                                  # 如果y轴为负，则标红标粗
            bar.set(edgecolor='darkred', color='salmon', linewidth=3)

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test5():
    """
    绘制直方图
    :return:
    """
    np.random.seed(19680801)                        # 随机数生成时所用算法开始的整数值, 导致每次随机数相同

    n_bins = 10
    x = np.random.randn(1000, 3)
    print(x)

    # 创建一个画图板和四个画图区,重新设置了图形的大小一倍
    fig, axes = pyplot.subplots(nrows=2, ncols=2, figsize=pyplot.figaspect(1. / 2))
    # ax由n*m的Axes组展平成1*nm的Axes组
    ax0, ax1, ax2, ax3 = axes.flatten()

    # 在绘图区1中绘图
    colors = ['red', 'tan', 'lime']
    ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)   # 绘制直方图 （传统的直方图，多个数据条行图排排列）
    ax0.legend(prop={'size': 10})                       # 设置图例
    ax0.set_title('bars with legend')                   # 设置绘图区1标题

    # 在绘图区2中绘图
    ax1.hist(x, n_bins, density=True, histtype='barstacked')    # 绘制直方图 （多个数据相互堆叠）
    ax1.set_title('stacked bar')                        # 设置绘图区2标题

    # 在绘图区3中绘图
    ax2.hist(x, histtype='barstacked', rwidth=0.9)      # 绘制直方图 （多个数据相互堆叠， 中间隔开）

    # 在绘图区4中绘图
    ax3.hist(x[:, 0], rwidth=0.9)                       # 绘制直方图 （传统的直方图，多个数据条行图排排列， 中间有间隔）
    ax3.set_title('different sample sizes')             # 设置绘图区4标题

    # 自动调整布局，使标题之间不重叠
    fig.tight_layout()

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test6():
    """
    绘制饼图
    :return:
    """
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # 创建一个画图板和2个画图区
    fig1, (ax1, ax2) = pyplot.subplots(2)

    # 在绘图区1中绘图
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)       # autopct : 显示百分比, labels : 提供标签, shadow : 在饼图下面画阴影
    ax1.axis('equal')           # 设置等比坐标轴

    # 在绘图区2中绘图 (explode : 各个饼面偏离的距离， startangle : 各个饼面的起点从x轴逆时针旋转的角度， pctdistance : 每个饼图切片的中心与autopct生成的文本开头之间的比率)
    ax2.pie(sizes, autopct='%1.2f%%', shadow=True, startangle=90, explode=explode,
            pctdistance=1.12)
    ax2.axis('equal')           # 设置等比坐标轴
    ax2.legend(labels=labels, loc='upper right')            # 设置图例， 位置偏右偏上

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test7():
    """
    绘制箱形图
    :return:
    """
    data = [5, 6, 2, 4, 8, 9, 10, 2, 4, 5, 3, 5, 15]
    data2 = [5, 6, 2, 4, 8, 9, 10, 2, 4, 5, 3, 5, 15]

    fig, (ax1, ax2) = pyplot.subplots(2)
    ax1.boxplot(data)
    ax2.boxplot(data2, vert=False)  # 控制方向
    pyplot.title("Box-plot Test")
    pyplot.show()


def matplotlib_test8():
    """
    绘制泡泡图
    :return:
    """
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
    pyplot.scatter(x, y, s=area, c=colors, alpha=0.5)

    # 显示所有打开的画图板
    pyplot.show()


def matplotlib_test9():
    """
    绘制等高线（轮廓图）
    :return:
    """
    fig, (ax1, ax2) = pyplot.subplots(2)
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    z = np.sin(xx ** 2 + yy ** 2) / (xx ** 2 + yy ** 2)
    ax1.contourf(x, y, z)
    ax2.contour(x, y, z)

    pyplot.show()


def matplotlib_test10():
    """
    绘制二维码
    :return:
    """
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # the bar
    x = np.random.rand(500) > 0.7

    barprops = dict(aspect='auto', cmap='binary', interpolation='nearest')

    fig = pyplot.figure()

    # a vertical barcode
    ax1 = fig.add_axes([0.1, 0.1, 0.1, 0.8])
    ax1.set_axis_off()
    ax1.imshow(x.reshape((-1, 1)), **barprops)

    # a horizontal barcode
    ax2 = fig.add_axes([0.3, 0.4, 0.6, 0.2])
    ax2.set_axis_off()
    ax2.imshow(x.reshape((1, -1)), **barprops)

    pyplot.show()


if __name__ == '__main__':
    # matplotlib_test1()
    # matplotlib_test2()
    # matplotlib_test3()
    # matplotlib_test4()
    # matplotlib_test5()
    # matplotlib_test6()
    #matplotlib_test7()
    matplotlib_test8()
    #matplotlib_test9()
    #matplotlib_test10()
    pass
