import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1, c = 'r', linewidth = '5') 
## 'c' ou 'color' muda a linha da cor
## linewidth define o tamanho da linha
plt.plot(y2, c = 'k', linewidth = '5')
## exemplo de 'multiplos plots'
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
## exemplo vários 'plots', com pares x-y
plt.show()