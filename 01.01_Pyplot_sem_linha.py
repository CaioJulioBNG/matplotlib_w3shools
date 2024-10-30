import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 5, 7 ,8 , 9, 11, 15, 21])
ypoints = np.array([3, 10, 11, 15, 32, 35, 39, 1])

plt.plot(xpoints, ypoints, 'o') # o parâmetro 'o' significa 'anéis', serve para não 'imprimir a linha'
plt.show()                      # serve para mostrar o gráfico