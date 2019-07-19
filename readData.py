with open('data.txt', "r") as f:  # 设置文件对象
    str = f.read()  # 可以是随便对文件的操作
dat = str.split(';')
array = [[] for i in range(len(dat))]

for num in range(len(dat)):
    a = dat[num].split(',')
    a[0] = a[0].strip()
    a[1] = a[1].strip()
    array[num] = a
print(array)

