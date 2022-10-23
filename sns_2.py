# f = open('spot.txt', 'w+', encoding='UTF-8')
import os

with open('spot.txt', encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
    string=data.strip("\'")
    spot = string.split(',')
    print(spot)
def read_path(file_pathname):
    # 遍历该目录下的所有文件
    iss_flag=1
    a=0
    while iss_flag:
        for filename in os.listdir(file_pathname):
            a+=1
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
        if a >5:
            iss_flag==0



read_path(r'D:\PycharmProjects\SNS\articles')

