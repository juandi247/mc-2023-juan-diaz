import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([2.2, 3, 4.5, 6, 8.5, 12])

def linear_regression(x, y):
  
  n = len(x)
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_xy = np.sum(x * y)
  sum_x_squared = np.sum(x**2)
  slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
  intercept = (sum_y - slope * sum_x) / n
  r_squared = ((n * sum_xy - sum_x * sum_y) / np.sqrt(
    (n * sum_x_squared - sum_x**2) * (n * np.sum(y**2) - sum_y**2)))**2
  return slope, intercept, r_squared


def exponential_regression(x, y):
  log_y = np.log(y)
  slope, intercept, r_squared = linear_regression(x, log_y)
  a = np.exp(intercept)
  b = slope
  return a, b, r_squared




a, b, r_squared = exponential_regression(x, y)
print("Regresión exponencial por mínimos cuadrados:")
print("a =", a)
print("b =", b)

plt.plot(x, y, 'o', )
plt.plot(x, a*np.exp(b*x),)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
