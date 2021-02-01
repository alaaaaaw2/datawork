# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:23:55 2021

@author: YaoWei3
"""

import pandas as pd
d = pd.read_csv('./car_complain.csv')
df= pd.DataFrame(d)
#0代表没有，1代表存在
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies('.'))

#数据清洗
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
df['brand'] = df['brand'].apply(f)

'''对品牌进行聚合，并对id进行计数操作'''

result = df.groupby(['brand'])['id'].agg(['count'])

'''车型投诉总数的计算'''
result2=df.groupby(['car_model'])['id'].agg(['count'])
print(result)
print(result2)
''''品牌与车型进行聚合，'''
result3=df.groupby(['brand','car_model'])['id'].agg(['count'])
''''转换为正常dataframe'''
result3.reset_index(inplace=True)
#确定品牌包含的车型数
result4 = result3.groupby(['brand'])['car_model'].agg(['count'])
#品牌下投诉总数
result5= result3.groupby(['brand'])['count'].agg(['sum'])
#转化为正常dataframe
result4.reset_index(inplace=True)
result5.reset_index(inplace=True)
#表格连接
result5=result4.merge(result5,how='right')
#求出品牌平均车型投诉数
result5['avr']=result5['sum']/result5['count']
#排序
result6=result5.sort_values(by= 'avr',ascending=False)
print(result6)
result6.to_csv('./result.csv')