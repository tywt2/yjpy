# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import networkx as nx

def show():
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 100), (0, 2, 5.5)])  # ��ӱߵ�Ȩֵ
    pos = [(110.999444444444, 35.0216666666667), (110.795277777778, 35.2052777777778),
           (110.613888888889, 35.1211111111111)]  # Ԫ���е����������ǵ�i����0��ʼ���������������
    nx.draw(G, pos, with_labels=True, node_color='b')  # ��������ͼ
    plt.xlim(0, 180)  # �����׽���X�����귶Χ
    plt.ylim(0, 90)  # �����׽���Y�����귶Χ
    plt.show()  # ��ʾͼ��
pass


def show2():
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 100), (0, 2, 5.5)])  # ��ӱߵ�Ȩֵ
    pos = [(110.999444444444, 35.0216666666667), (110.795277777778, 35.2052777777778),
           (110.613888888889, 35.1211111111111)]  # Ԫ���е����������ǵ�i����0��ʼ���������������
    nx.draw(G, pos, with_labels=True, node_color='b')  # ��������ͼ
    plt.xlim(0, 180)  # �����׽���X�����귶Χ
    plt.ylim(0, 90)  # �����׽���Y�����귶Χ
    plt.show()  # ��ʾͼ��
pass

show2()