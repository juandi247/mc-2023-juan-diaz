import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Datos de la tabla

x = np.array([0, 1, 2, 3, 4,5,6])
y = np.array([4.2,1.4, 0,-0.4,-0.1,1.6,4.1])

def quadratic_func(x, a, b, c):
    return a*x**2 + b*x + c


popt, pcov = curve_fit(quadratic_func, x, y)


a, b, c = popt


r = np.corrcoef(x, y)[0, 1]

print(f"Coeficientes del polinomio ajustado: a={a:.2f}, b={b:.2f}, c={c:.2f}")
print(f"Coeficiente de correlación (r): {r:.2f}")


plt.xlim(-1,9)

plt.ylim(-1,6)

plt.scatter(x, y,label="Datos")
plt.plot(x, quadratic_func(x, a, b, c), label="Ajuste")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polinomio de segundo grado ajustado")
plt.legend()
plt.show()