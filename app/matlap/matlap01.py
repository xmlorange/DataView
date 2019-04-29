# -*- coding: utf-8 -*-

from pylab import *

# 解决坐标轴负刻度乱码问题
rcParams['axes.unicode_minus'] = False
# 解决中文乱码问题
rcParams['font.sans-serif'] = ['Simhei']
# 设置图片大小 单位英寸
rc('figure', figsize=(6, 3))


def pylab_way():
    x = linspace(-5, 5, 10)
    y = x ** 2

    figure()  # 实例化绘图对象
    plot(x, y, 'r')  # r 是颜色 red

    xlabel('x')
    ylabel('y')
    title('pylab 显示')
    show()


def sub_pylab_way():
    x = linspace(-5, 5, 10)
    y = x ** 2

    figure()
    subplot(1, 2, 1)
    plot(x, y, 'r--')
    xlabel('x')
    ylabel('y')
    title('sub pylab')

    subplot(1, 2, 2)
    plot(y, x, 'g*-')
    xlabel('y')
    ylabel('x')
    title('sub pylab 2 显示')

    show()


if __name__ == '__main__':
    # pylab_way()
    sub_pylab_way()
