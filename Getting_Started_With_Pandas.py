# -*-coding:utf-8-*-

##############
# by kevinelstri
# 数据集为：train.csv
# Getting Started With Pandas
##############

import numpy as np
###
# 使用csv进行读取数据
###
import csv as csv

csv_file_object = csv.reader(open('../Data/train.csv', 'rb'))
header = csv_file_object.next()
# print header

data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)
# print data

###
# 使用pandas进行读取数据
###
import pandas as pd

df = pd.read_csv('../Data/train.csv')
print df.head(3)
print df
print df.tail(3)
print df.dtypes
print df.info()
print df.describe()

print df['Age'][0:10]
print type(df['Age'])
print df['Age'].mean()
print df[['Age', 'Sex', 'Pclass']][0:10]
print df[df['Age'] > 50]
print df[df['Age'] > 50][['Name', 'Sex', 'Age']]
print df[df['Age'].isnull()][['Name', 'Sex', 'Age']]

for i in range(1, 4):
    print i, len(df[(df['Sex'] == 'male') & (df['Pclass'] == i)])  # 逻辑运算

# import pylab as p
# df['Age'].hist()
# p.show()

###
# 清洗数据
###
df['Gender'] = 1  # 增加了一列Gender，值全部为1
print df.head(3)

df['Gender'] = df['Sex'].map(lambda x: x[0].upper())  # 将Sex列的首字母的大写形式复制给Gender列
print df.head(3)

df['Gender'] = df['Sex'].map({'female': 0, 'male': 1}).astype(int)  # 将sex转换为二值，male(男)为1，female(女)为0
print df[['Name', 'Age', 'Gender']][0:10]

###
# 处理Age的空值问题
#     the average age of passagers is 29.6991176, so let the value of age is simillar with average.
#     the median might be better
#     let's build another reference table to calculate what each of these medians are:
###
median_ages = np.zeros((2, 3))  # 创建一个2行3列的全为0的矩阵,由于Sex值为2个，Pclass值为3个
print median_ages
print '--------------------------------------------------------------------------------'

##############
# 分析：dropna()就是去除Age==NaN的情况，等同于 df['Age'].notnull()
#      median()指的是一组数据的中位数
##############
sum = df[(df['Gender'] == 1) & (df['Pclass'] == 1)]['Age'].sum()  # 满足条件的Age求和
len = len(df[(df['Gender'] == 1) & (df['Pclass'] == 1) & (df['Age'].notnull())]['Age'])
print 'sum=', sum
print 'len=', len
print 'avg=', sum / len  # 满足条件的avg平均值
print (df[(df['Gender'] == 1) & (df['Pclass'] == 1) & (df['Age'].notnull())]['Age']).median()  # 与下面for循环里面的判断是等价的

for i in range(0, 2):
    for j in range(0, 3):  # Gender的取值为0,1     Pclass的取值为1,2,3
        median_ages[i, j] = df[(df['Gender'] == i) & (df['Pclass'] == j + 1)]['Age'].dropna().median()
print median_ages
print '---------------------------------------------------------------------------------'

####
# 新建一个AgeFill列表，将Age数据复制进去，并将空值补齐
####
df['AgeFill'] = df['Age']
print df[['Name', 'Age', 'AgeFill']][0:20]
print
print df[df['Age'].isnull()][['Name', 'Age', 'AgeFill']].head(10)  # Age为空的列表
print

for i in range(0, 2):
    for j in range(0, 3):  # 空值补齐，将上述矩阵中的数据对应到空值里面
        df.loc[(df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j + 1), 'AgeFill'] = median_ages[i, j]
print df[df['Age'].isnull()][['Name', 'Age', 'AgeFill']].head(10)

print '---------------------------------------------------------------------------------'

df['AgeIsNull'] = pd.isnull(df.Age).astype(int)
print df[['Name', 'Age', 'AgeFill', 'AgeIsNull']].head(10)

#####
# 特征工程
#####
df['FamilySize'] = df['SibSp'] + df['Parch']
print df[['SibSp', 'Parch', 'FamilySize']]

df['Age*Class'] = df.AgeFill * df.Pclass
print df[['SibSp', 'Parch', 'FamilySize', 'Age*Class', 'Survived']]
print df[['SibSp', 'Parch', 'FamilySize', 'Age*Class', 'Survived', 'Sex']]

# import pylab as p
# df['Age*Class'].hist()
# p.show()

####
# final preparation:
#   (1)determine what columns we have left which are not numeric
#   (2)send our pandas.DataFrame back to a numpy.array
####
print df.dtypes
print
print df.dtypes[df.dtypes.map(lambda x: x == 'object')]

print df.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)  # 删除没有用到的列
print
print df.drop(['Age'], axis=1)  # Age这列已经没用了，也删除
print
print df.dropna()  # 删除表中仍然有空值的行

# convert it into a numpy array
# pandas can send back an array using the .values method
train_data = df.values  # 将数据转换成矩阵形式
print train_data

