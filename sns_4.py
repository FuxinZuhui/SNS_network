# f = open('spot.txt', 'w+', encoding='UTF-8')
import os
import numpy as np
import pandas as pd
row = 137
col = 137
matrix = np.zeros((row,col))
with open('spot2.txt', encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
    string=data.strip("\'")
    spot = string.split(',')
    print(spot)
    for i in range(len(spot)):
        if '/' in spot[i]:
            string1=spot[i]
            spot2 = string1.split('/')
            spot.insert(i, spot2)  # 把最大年龄对应的姓名插入到第一个
            spot.__delitem__(i + 1)
    print(spot)
    print(len(spot))

def read_path(file_pathname):
    # 遍历该目录下的所有文件
    for filename in os.listdir(file_pathname):
        # print(r'E:\AI\ship/{0}'.format(filename))
        path1 = os.path.join(r'D:\PycharmProjects\SNS\articles', filename)
        path2=os.path.join(r'D:\PycharmProjects\SNS\articles_3', filename)
        f1 = open(path1, 'r',encoding='utf-8')
        f2 = open(path2, 'w', encoding='utf-8')
        for line in f1.readlines():
            if line == '\n':
                line = line.strip('\n')
            f2.write(line)
        f2.close()
        f2 = open(path2, 'r', encoding='utf-8')
        data1 = f2.read()
        for i in range(len(spot)):
            if len(spot[i])!=1: #表示一个景点有多个可能名称
                spot_find = True #某个景点是否被找到的标签
                for j in range(len(spot[i])):
                    if spot_find:
                        for k in range(len(spot)) :
                            if len(spot[k])!=1:
                                for l in range(len(spot[k])):
                                    if spot_find:
                                        if spot[i][j] in data1 and spot[k][l] in data1 and spot[i][j] != spot[k][l]:
                                            if i!=k:
                                                matrix[i][k] += 1
                                                spot_find = False
                            else:
                                if spot[i][j] in data1 and spot[k] in data1 and spot[i][j] != spot[k]:
                                    matrix[i][k] += 1
                                    spot_find = False
            else:
                for m in range(len(spot)):
                    if len(spot[m])!=1:
                        spot_find2 = True
                        for n in range(len(spot[m])):
                            if spot_find2:
                                if spot[i] in data1 and spot[m][n] in data1 and spot[i] != spot[m][n]:
                                    matrix[i][m] += 1
                                    spot_find2 = False
                    else:
                        if spot[i] in data1 and spot[m] in data1 and spot[i] != spot[m]:
                            matrix[i][m] += 1

            # a=一个正则表达式

read_path(r'D:\PycharmProjects\SNS\articles')
print(matrix)
data2 = pd.DataFrame(matrix)
data2.to_csv('matrix3.csv', index=0, columns=None, encoding='utf-8')

# from fuzzywuzzy import fuzz
# a = data.user.apply(lambda user: fuzz.ratio(user, '的环境萨克汇顶科技'))
# a = a.nlargest(10).reset_index()
# a.columns = ["名称", "相似度"]
# a.名称 = data.user[a.名称].values
# a