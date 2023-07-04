import math 
import scipy.stats as stats
import numpy as np
from statsmodels.stats.weightstats import zconfint
from statsmodels.stats.weightstats import _zconfint_generic, _tconfint_generic
#задача 1
print("задача 1")
# Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a
# с надежностью 0.95, 
# если выборочная средняя M = 80, а объем выборки n = 256.
sigma=16
alfa=0.05
dov_interval=0.95
M=80
n=256
z_alfa_2=stats.norm.ppf(0.975)
print(f"доверительный интервал ({round(M-z_alfa_2*sigma/math.sqrt(n),3)},{round(M+z_alfa_2*sigma/math.sqrt(n),3)})")
#задача 2
print("задача 2")
# В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные 
# данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону
# распределения вероятностей, оценить истинное значение величины
# X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95. 
x=np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
x_sr=np.mean(x)
sigma=np.std(x,ddof=1)
n=10
t_alfa_2=stats.t.ppf(0.975,n-1)
print(f"доверительный интервал ({round(x_sr-t_alfa_2*sigma/math.sqrt(n),3)},{round(x_sr+t_alfa_2*sigma/math.sqrt(n),3)})")
#задача 3
print("задача 3")
# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 
# Используя эти данные построить
# 95% доверительный интервал для разности 
# среднего роста родителей и детей.
x=np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
y=np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
x_sr=np.mean(x)
d_x=np.var(x,ddof=1)
std_x=np.std(x,ddof=1)
y_sr=np.mean(y)
d_y=np.var(y,ddof=1)
delta=x_sr-y_sr
d=(d_x+d_y)/2
se=math.sqrt(d/len(x)+d/len(y))
t_alfa_2=stats.t.ppf(0.975,len(x)+len(y)-2)
print(f"доверительный интервал ({round(delta-t_alfa_2*se,3)},{round(delta+t_alfa_2*se,3)})")
print(_tconfint_generic(x_sr,std_x,9, 0.05,'two-sided' ))
 







