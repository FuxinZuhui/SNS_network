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
    print(string)
    print(len(string))
    spot=[x.strip().split('/')for x in string.split(',')]
    print(spot)

def isInArticle(article,list):
    for x in list:
        if x in article:
            return True
    return False


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
        for i in range(len(spot)):
            if isInArticle(data1,spot[i]):
                for j in range(len(spot)) :
                    if i != j and isInArticle(data1,spot[j]):
                        Matrix[i][j] +=1


read_path(r'D:\PycharmProjects\SNS\articles')
print(Matrix)
data2 = pd.DataFrame(Matrix)
data2.to_csv('matrix5.csv', index=0, columns=None, encoding='utf-8')