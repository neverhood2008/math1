import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
def mult(a,b):
    mass=[]
    for i in range(len(a)):
        mass.append(a[i]*b[i]) 
    # print(f"массив : {mass}") 
    return mass
def func(b0,b1,a):
    mass=[]
    for i in range(len(a)):
        mass.append(b0+b1*a[i]) 
    # print(f"массив : {mass}") 
    return mass
def sum(a):
    summa=0
    for i in range(len(a)):
        summa+=a[i]
    print(f"сумма : {summa}") 
    return summa
def kvadrat(a):
    mass_kvad=[]
    for i in range(len(a)):
        mass_kvad.append(a[i]**2) 
    print(f"квадрат : {mass_kvad}") 
    return mass_kvad
# 1 . Даны значения величины заработной платы заемщиков банка (zp)
#  и значения их поведенческого кредитного скоринга (ks):
#   zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
#    ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Используя математические операции, посчитать коэффициенты линейной 
# регрессии, приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
#задача 1
print("задача 1")
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832] 
n=10
b1 = (n*np.sum(mult(zp,ks)) - np.sum(zp)* np.sum(ks) )/ (n*np.sum(kvadrat(zp)) - np.sum(zp) ** 2)
print(f"b1={b1}") 
b0 = np.mean(ks) - b1 * np.mean(zp)
print(f"b0={b0}")
r = np.corrcoef(zp, ks)[0, 1]
print(f"коэффициент корреляции={r}")
plt.scatter(zp, ks)
plt.show() 
ks_predskaz=func(b0,b1,zp)
plt.plot(zp,ks_predskaz)
plt.show() 
#  

# 2.Посчитать коэффициент линейной регрессии при заработной плате (zp),
#  используя градиентный спуск (без intercept).
#задача 2
print("задача 2")
x=zp
y=ks
def mass_spusk_kvadrat(b1,x,y):
    mass=[]
    for i in range(len(x)):
        mass.append((b1*x[i]-y[i])**2) 
    # print(f"массив : {mass}") 
    return mass
def mse_(b1,y,x,n=10):
    return np.sum(mass_spusk_kvadrat(b1,x,y))/n

def mass_spusk(b1,x,y):
    mass=[]
    for i in range(len(x)):
        mass.append((b1*x[i]-y[i])*x[i]) 
    # print(f"массив : {mass}") 
    return mass

alfa=0.000001
b1=0.1
n=10
for i in range(10000):
    b1-=alfa*(1/n)*np.sum(mass_spusk(b1,y,x))
    if i%500==0:
        print("i={i},b1={b1}, mse={mse}".format(i=i,b1=b1,mse=mse_(b1,y,x)))

# 3.Произвести вычисления как в пункте 2, но с 
# вычислением intercept. Учесть, что изменение коэффициентов должно 
# производиться на каждом шаге одновременно (то есть изменение 
#   одного коэффициента не должно влиять на изменение
#  другого во время одной итерации).
#задача 3
print("задача 3")
x=zp
y=ks
def mass_spusk_kvadrat_zadan3(b0,b1,x,y):
    mass=[]
    for i in range(len(x)):
        mass.append((b1*x[i]+b0-y[i])**2) 
    # print(f"массив : {mass}") 
    return mass
def mse_zadanie3(b0,b1,y,x,n=10):
    return np.sum(mass_spusk_kvadrat(b1,x,y))/n

def mass_spusk_zadanie3(b0,b1,x,y):
    mass=[]
    for i in range(len(x)):
        mass.append((b1*x[i]+b0-y[i])*x[i]) 
    # print(f"массив : {mass}") 
    return mass

alfa=0.000001
b1=0.1
b0=0.1
n=10
for i in range(10000):
    b1-=alfa*(2/n)*np.sum(mass_spusk_zadanie3(b0,b1,x,y))
    if i%1000==0:
        print("i={i},b1={b1}".format(i=i,b1=b1))
        print("i={i},b1={b1}, mse={mse}".format(i=i,b1=b1,mse=mse_zadanie3(b0,b1,y,x)))
