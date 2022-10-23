import os
import numpy as np
import pandas as pd
row = 137
col = 137
Matrix = np.zeros((row,col))
with open('spot3.txt', encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
    string=data.strip("\'")
    spot = string.split(',')
    print(spot)
    print(len(spot))
    for i in range(len(spot)):
        if '/' in spot[i]:#找到某个存在多种名称的景点
            string1=spot[i]
            spot2 = string1.split('/')
            print(spot2)
            spot.insert(i, spot2)  # 把生成的景点列表插到原来的景点位置上
            spot.__delitem__(i + 1)# 把重复的未拆分景点列表插删除
    print(spot)

def matrix_11(matrix,list,data,i,j):#当两个景点都只有一种名称时
    if list[i] in data and list[j] in data and list[i] != list[j]:
        matrix[i][j] += 1
    return matrix
def matrix_1n(matrix,list,data,i,j):#当第一个景点有一种名称，第二个景点有n个名称时
    for n in range(len(list[j])):
        if list[i] in data and list[j][n] in data:
            matrix[i][j] += 1
            break
    return matrix
def matrix_n1(matrix,list,data,i,j ):#当第一个景点有n个名称，第二个景点只有一种名称时
    for n in range(len(list[i])):
        if list[i][n] in data and list[j] in data:
            matrix[i][j] += 1
            break
    return matrix
def matrix_nn(matrix,list,data,i,j):#当两个景点都有n种名称时
    spot_find = False
    for m in range(len(list[i])):
        for n in range(len(spot[j])):
            if  list[i][m] in data and list[j][n] in data and i!=j:
                matrix[i][j] += 1
                spot_find = True
                break
        if spot_find:
            break
    return matrix

def c_occurrence_num(matrix,list,data):#计算景点的共现次数的矩阵
    lenth=len(list)
    for i in range(lenth):
        for j in range(lenth):
            if len(list[i]) == 1 and len(list[j])==1:  # 1V1
                matrix_11(matrix,list,data,i,j)
            elif len(list[i]) == 1 and len(list[j])!=1: # 1Vn
                matrix_1n(matrix,list, data, i, j,matrix)
            elif len(list[i]) != 1 and len(list[j])==1: # nV1
                matrix_n1(matrix,list, data, i, j,matrix)
            elif len(list[i]) != 1 and len(list[j])!=1: # nVn
                matrix_nn(matrix,list, data, i, j)
    return matrix

def read_path(file_pathname):
    # 遍历该目录下的所有文件
    for filename in os.listdir(file_pathname):
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
        c_occurrence_num(Matrix,spot,data1)

read_path(r'D:\PycharmProjects\SNS\articles')
print(Matrix)
data2 = pd.DataFrame(Matrix)
data2.to_csv('matrix4.csv', index=0, columns=None, encoding='utf-8')

# from fuzzywuzzy import fuzz
# a = data.user.apply(lambda user: fuzz.ratio(user, '的环境萨克汇顶科技'))
# a = a.nlargest(10).reset_index()
# a.columns = ["名称", "相似度"]
# a.名称 = data.user[a.名称].values
