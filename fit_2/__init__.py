# 使用Python来操作数据实现线性拟合
from turtle import pd

import matplotlib.pyplot as plt
import numpy as np

# import pandas as pd

ais_data = pd.read_csv('./newen.csv', encoding='utf-8')  # 读出数据
ais_data = ais_data.dropna(axis=0, subset=['SHIP_ENGINE_POWER', 'SHIP_SPEED'])  # 删除数据中为NaN的数据
ship_power = ais_data['SHIP_ENGINE_POWER'].values
ship_ncr = ais_data['SHIP_SPEED'].values
x = np.array(ship_ncr)  # 将数据写成矩阵的形式，因为下列函数在调用使用数据的时候都是用的矩阵
y = np.array(ship_power)
plot = plt.plot(x, y, "*", label='SHIP_ENGINE_POWER')  # 画图，散点图，label是为了添加图片上的数据*的名字
'''
   进行线性拟合
'''
fit = np.polyfit(x, y, 1)  ##拟合函数的次方，这里的数字是次方1，代表一次方即，ax+b，2代表二次方
print(fit)
p1 = np.poly1d(fit)  # 进行曲线的拟合，拟合曲线
yvals = p1(x)
plot2 = plt.plot(x, yvals, 'r', label='SHIP_SPEED')  # 画图，直线图
plt.xlabel('SHIP_SPEED')  # x轴的名称
plt.ylabel('SHIP_ENGINE_POWER')  # y轴的名称
plt.title('nihe')  # 拟合函数的名称
plt.legend()  # 为了展示label的内容
plt.show()  # 展示图片
