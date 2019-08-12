import math


def ComputeArea():
    #arr = data.split(';')
    with open('data.txt', "r") as f:  # 设置文件对象
        str = f.read()  # 可以是随便对文件的操作
    arr = str.split(';')
    arr_len = len(arr)
    if arr_len < 3:
        return 0.0
    temp = []
    for i in range(0,arr_len):
        temp.append([float(x) for x in arr[i].split(',')])
    s = temp[0][1] * (temp[arr_len -1][0]-temp[1][0])

    for i in range(1,arr_len):
        s += temp[i][1] * (temp[i-1][0] - temp[(i+1)%arr_len][0])
    return round(math.fabs(s/2)*9101160000.085981,6)


ComputeArea()