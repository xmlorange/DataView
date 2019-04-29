# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 解决坐标轴负刻度乱码问题
plt.rcParams['axes.unicode_minus'] = False
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['Simhei']

np.random.seed(1026)


def test_2_object():
    x = np.linspace(0, 5, 10)
    y = x ** 2
    fig = plt.figure(figsize=(8, 5), dpi=100)

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # 添加坐标轴 left bottom width height range(0-1)
    axes.plot(x, y, 'r')

    axes.set_xlabel('x')
    axes.set_ylabel('y')

    plt.title('pylab 显示')

    ax = fig.add_subplot(221)
    # ax = fig.add_subplot(2, 2, 1)

    ax.set_title('面向对象方式绘图')
    ax.plot(x, y)

    plt.show()
    plt.close(0)


def show_sin():
    x = np.linspace(0, 2 * np.pi, 50)
    plt.plot(x, np.sin(x), x, np.sin(2 * x), x, np.cos(x))
    plt.title("正弦曲线")

    plt.show()


def custom_line_style():
    x = np.linspace(0, 2 * np.pi, 50)
    # plt.plot(x, np.sin(x), color='y', linestyle='--')
    plt.plot(x, np.sin(x), 'k^:')
    plt.show()


def multiple_images():
    # x = np.linspace(0, 2 * np.pi, 50)
    # y = np.sin(x)

    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)  # 和subplot有区别
    # 可以用下表取然后画图
    # axes[0].plot(x, y, 'r-')
    # axes[0].set_xlabel('x')
    # axes[0].set_ylabel('y')
    # axes[0].set_title('title')
    for i in range(2):
        for j in range(2):
            axes[i, j].plot(np.random.randn(100), 'r-')

    plt.subplots_adjust(wspace=0, hspace=0)  # 设置图例之间的间距
    plt.show()


def test_subplot():
    x = np.linspace(0, 2 * np.pi, 50)
    y = np.cos(x ** 2)

    plt.subplot(2, 1, 1)
    plt.plot(x, np.sin(x), 'r-', label='sin(x)')
    plt.title('compare')
    # 添加纵坐标标签
    plt.ylabel('sin(x)')
    plt.grid()  # 添加网格

    plt.legend(loc='lower left')  # 参数有 best upper lower left right

    # 指向第二个绘图子区
    plt.subplot(2, 1, 2)
    plt.plot(x, y, 'g.:', label='$cos(x^2)$')
    plt.xlabel('x')
    plt.ylabel('cos(x)')

    # 设置y轴范围
    plt.ylim(-2, 1)
    plt.grid()  # 添加网格
    plt.legend(loc='best')  # 图例显示位置  最佳

    plt.savefig('sin cos.png', dpi=800)  # 保存图片
    plt.show()


def ticks_tag():
    """
    刻度及刻度标签
    :return:
    """
    plt.plot(np.random.randn(1000).cumsum())
    plt.yticks([-50, -40, -30, -20, -10, 0, 10, 20])
    plt.xticks([0, 250, 500, 750, 1000],
               ['Jan', 'Feb', 'Mar', 'Apr', 'May'],  # 刻度映射
               rotation=30,  # 刻度旋转 30 度
               fontsize=15   # 字体大小
               )
    plt.title('ticks and tags', fontsize=20)
    plt.xlabel('Stages', fontsize=16)
    plt.show()


if __name__ == '__main__':
    # show_sin()
    # test_2_object()
    # custom_line_style()
    # multiple_images()
    # test_subplot()
    ticks_tag()
