# import numpy as np
# import matplotlib.pyplot as plt
# # x = np.array([10,8, 13, 9,11,14, 6,4,12, 7,5])
# # y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68 ])
# # x3 = np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
# # y3 = np.array([7.46,6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
# x = np.array([10,8, 13, 9,11,14, 6,4,12, 7,5])
# y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68 ])
# X4 = x.reshape((11, 1))
# Y4 = y.reshape((11, 1))
# X5 = np.hstack([np.ones((11, 1)), X4])
# B = np.dot(np.linalg.inv(np.dot(X5.T, X5)), X5.T @ Y4)
# print(B)
# r = np.corrcoef(x, y)[0, 1]
# print(r)
# plt.scatter(x, y)
# plt.plot(x, 3.00009091 + 0.50009091 * x)
# plt.show()from scipy import stats
x3 = np.array([ 10,8, 9,11,14, 6,4,12, 7,5 ])
y3 = np.array([7.46,6.77, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
X4 = x3.reshape((10, 1))
Y4 = y3.reshape((10, 1))
X5 = np.hstack([np.ones((10, 1)), X4])
B = np.dot(np.linalg.inv(np.dot(X5.T, X5)), X5.T @ Y4)
print(B)
r = np.corrcoef(x3, y3)[0, 1]
print(r)
plt.scatter(x3, y3)
plt.plot(x, B[0] + B[1] * x)
plt.show()
Y_pred =  4.00564935 + 0.34538961 * x3 #модельные значения
resid = y3 - Y_pred
stats.shapiro(resid)

pred = 5.600000000000016 + 1.2257142857142853 * X3
resid = Y3 - pred
import scipy.stats as stats
stats.shapiro(resid)
stats.f.ppf(0.95, 1, 10)
21:42

Ssf = np.sum((pred - np.mean(Y3)) ** 2)
Sso = np.sum((Y3 - pred) ** 2)
Msf = Ssf / 1
Mso = Sso / 10
F = Msf/ Mso
print(F)