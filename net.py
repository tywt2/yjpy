# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import networkx as nx

def show():
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 100), (0, 2, 5.5)])  # 添加边的权值
    pos = [(110.999444444444, 35.0216666666667), (110.795277777778, 35.2052777777778),
           (110.613888888889, 35.1211111111111)]  # 元组中的两个数字是第i（从0开始计数）个点的坐标
    nx.draw(G, pos, with_labels=True, node_color='b')  # 按参数构图
    plt.xlim(0, 180)  # 设置首界面X轴坐标范围
    plt.ylim(0, 90)  # 设置首界面Y轴坐标范围
    plt.show()  # 显示图像
pass


def show2():
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 100), (0, 2, 5.5)])  # 添加边的权值
    pos = [(110.999444444444, 35.0216666666667), (110.795277777778, 35.2052777777778),
           (110.613888888889, 35.1211111111111)]  # 元组中的两个数字是第i（从0开始计数）个点的坐标
    nx.draw(G, pos, with_labels=True, node_color='b')  # 按参数构图
    plt.xlim(0, 180)  # 设置首界面X轴坐标范围
    plt.ylim(0, 90)  # 设置首界面Y轴坐标范围
    plt.show()  # 显示图像
pass

show2()