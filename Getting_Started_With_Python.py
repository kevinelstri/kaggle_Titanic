# -*-coding:utf-8-*-
######################
# by kevinelstri
# 数据集：train.csv
# Getting Started With Python
######################
import csv as csv
import numpy as np

######################
# Titanic
######################
# ---------------------
# csv 读取csv文件，并转换成矩阵形式
# ---------------------
csv_file_object = csv.reader(open('../Data/train.csv', 'rb'))  # 打开并读取csv文件
header = csv_file_object.next()  # 获取字段属性值
print header

data = []
for row in csv_file_object:  # 将csv文件按行读取加入到list元组中
    data.append(row)
data = np.array(data)  # 将list元组构成矩阵形式

#----------------------
# 操作csv文件，熟悉csv语法
#----------------------
print data[0]
print data[0, 3]  # 获取第0行的第三列元素
print data[0::, 3]  # "0::"表示从开头到结尾所有的行，3表示第三列，默认读取的为string类型
print data[0::, 2].astype(np.float)  # 将string类型转换为float类型
number_passengers = np.size(data[0::, 1].astype(np.float))  # 获取总人数
number_survived = np.sum(data[0::, 1].astype(np.float))  # 获取幸存者的人数
proportion_survived = number_survived / number_passengers  # 幸存者的比例
print 'number_passengers=', number_passengers
print 'number_survived=', number_survived
print 'proportion_survived=', proportion_survived  # 幸存比例

#----------------------
# 运用：男女幸存者比例
#----------------------
women_only_state = data[0::, 4] == "female"
men_only_state = data[0::, 4] != "female"

women_onboard = data[women_only_state, 1].astype(np.float)  # 船上女性
men_onboard = data[men_only_state, 1].astype(np.float)  # 船上男性

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'proportion_women_survived=', proportion_women_survived  # 女性幸存者比例
print 'proportion_men_survived=', proportion_men_survived  # 男性幸存者比例
