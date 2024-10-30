# A maioria dos utilitários do matplotlib está sob o submódulo pyplot
import matplotlib.pyplot as plt      # import com o ''apelido''
import numpy as np                   # import do numpy

# O comando plot() serve para desenhar pontos (markers) em um diagrama,
# Esta função desenha uma linha entre os pontos
# Está função recebe os parâmetros para determinar os pontos no diagrama
# O parâmetro 1 recebe um array com os pontos do eixo x ("linha horizontal")
# O parâmetro 2 recebe um array com os pontos do eixo y ("linha vertical")

xpoints = np.array([5, 15])  # A linha sairá do ponto 5 ao 15 (eixo horizontal)
ypoints = np.array([0, 350]) # A linha sairá do ponto 0 ao 350 (eixo vertical)

plt.plot(xpoints, ypoints)
plt.show()
