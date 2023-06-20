# задача2
#В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, 
# из второго - 4. Какова вероятность того,
# что 3 мяча белые?
import math
def comb(a,b):
    comb=math.factorial(b)/(math.factorial(a)*math.factorial(b-a))
    return comb
#0 белых из первого ящика
p0=comb(0,5)/comb(0,8)*comb(2,3)/comb(2,8)*comb(3,5)/comb(3,12)*comb(1,7)/comb(1,9)
#print(p0)
#1 белый из первого ящика
p1=comb(1,5)/comb(1,8)*comb(1,3)/comb(1,7)*comb(2,5)/comb(2,12)*comb(2,7)/comb(2,10)
#print(p1)
#2 белых из первого ящика
p2=comb(2,5)/comb(2,8)*comb(1,5)/comb(1,12)*comb(3,7)/comb(3,11)
p=p1+p0+p2
#print(p2)
p=round(p,2)
print(f"вероятность, что 3 мяча белые={p}")




