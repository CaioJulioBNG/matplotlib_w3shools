import matplotlib.pyplot as plt
import numpy as np

# Caso não o eixo x não seja diretamente declarado, os valores serão 0, 1, 2, 3 ..., dependendo do tamanho do ponto y

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()