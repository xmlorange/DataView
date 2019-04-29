# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 解决坐标轴负刻度乱码问题
plt.rcParams['axes.unicode_minus'] = False
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['Simhei']


def scatter_plot():
    # 散点图
    x = np.linspace(0, 2 * np.pi, 50)
    y = np.random.random(50)
    plt.scatter(x, y)
    plt.show()


def color_scatter_plot():
    # 散点图
    x = np.random.randint(1, 100, 100)
    y = np.random.rand(100)

    size = np.random.rand(100) * 500
    color = np.random.rand(100)

    plt.rc('figure', figsize=(10, 4))
    plt.scatter(
        x, y, size, color,
        alpha=.6,
        # linewidths=2
    )
    plt.colorbar()  # 显示色条
    plt.show()


def bar_plot():
    """柱状图，条形图"""
    size = 5
    a = np.random.random(size)
    x = np.arange(size)

    plt.bar(x, a)
    plt.show()


def multiple_bar():
    """簇状图"""
    size = 5
    a = np.random.random(size)
    b = np.random.random(size)
    c = np.random.random(size)
    d = np.random.random(size)
    x = np.arange(size)

    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, a, width=width, label='a')
    plt.bar(x + width, b, width=width, label='b')
    plt.bar(x + width * 2, c, width=width, label='c')

    plt.legend()
    plt.show()


def accumulation_bar():
    """堆积柱状图"""
    n = 5
    men_means = (20, 35, 30, 27, 35)
    women_means = (25, 30, 28, 10, 35)
    ind = np.arange(n)
    width = 0.35

    # p1 = plt.bar(ind, men_means, width, color='#d62728')
    # p2 = plt.bar(ind, women_means, width, bottom=men_means)

    plt.bar(ind, men_means, width, color='#d62728', label='men')
    plt.bar(ind, women_means, width, bottom=men_means, label='women')

    plt.ylabel('Scores')
    plt.title('Score by group and gender')
    plt.xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
    plt.yticks(np.arange(0, 81, 10))

    # plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    plt.legend()
    plt.show()


def accumulation_bar_with_num():
    """带方差的推积累柱状图"""
    n = 5
    men_means = (20, 35, 30, 27, 35)
    women_means = (25, 30, 28, 10, 35)

    men_std = (2, 3, 4, 1, 2)
    women_std = (3, 5, 2, 3, 3)

    ind = np.arange(n)
    width = 0.35

    plt.bar(ind, men_means, width, color='#d62728', label='men', yerr=men_std)
    plt.bar(ind, women_means, width, bottom=men_means, label='women', yerr=women_std)

    plt.ylabel('Scores')
    plt.title('Score by group and gender')
    plt.xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
    plt.yticks(np.arange(0, 81, 10))

    plt.legend()
    plt.show()


if __name__ == '__main__':
    scatter_plot()
