#1 задача1
# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 
# 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать 
# (желательно без использования статистических методов наподобие std,
#   var, mean) среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.
import numpy as np
import math
def avarage_func(massiv):
    summa=0
    for i in range(len(massiv)):
        summa+=massiv[i]
    return summa/len(massiv)
def biased_variance_func(massiv):
    summa=0
    n=len(massiv)
    avarage_val=avarage_func(massiv)
    for i in range(n):
        summa+=(massiv[i]-avarage_val)**2
    return summa/n
def unbiased_variance_func(massiv):
    summa=0
    n=len(massiv)
    avarage_val=avarage_func(massiv)
    for i in range(n):
        summa+=(massiv[i]-avarage_val)**2
    return summa/(n-1)
array_new=[100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
print(f'Массив:{array_new}')
array_new.sort()
print(f'Массив:{array_new}')
avarage_value=avarage_func(array_new)
print(f"среднее арифметическое = {avarage_value}")
biased_variance_value=round(biased_variance_func(array_new),2)
print(f"смещенная дисперсия = {biased_variance_value}")
unbiased_variance_value=round(unbiased_variance_func(array_new),2)
print(f"СКО смещенной дисперсии = {round(math.sqrt(biased_variance_value),2)}")
print(f"несмещенная дисперсия = {unbiased_variance_value}")
print(f"СКО несмещенной дисперсии = {round(math.sqrt(unbiased_variance_value),2)}")
#2 способ
print("2 способ")
print(f"смещенная дисперсия = {round(np.var(array_new),2)}")
print(f"СКО смещенной дисперсии = {round(np.std(array_new),2)}")
print(f"несмещенная дисперсия = {round(np.var(array_new,ddof=1),2)}")
print(f"СКО несмещенной дисперсии = {round(np.std(array_new,ddof=1),2)}")
