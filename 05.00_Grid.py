import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

fonte_1 = {'family':'serif','color':'red','size':10}
fonte_2 = {'family':'serif','color':'black','size':5}

plt.title("Exemplo de Título de Gráfico", fontdict=fonte_1, loc ='left')
## fontdict - Seleciona o estilo da fonte
## loc - Seleciona a posição do título
plt.xlabel("Exemplo eixo x", fontdict=fonte_2)
plt.ylabel("Exemplo eixo y", fontdict=fonte_2)
plt.grid(color = 'green', linestyle = '--', linewidth=0.3, axis='both')
## o comando 'axis' serve para determinar o estilo do 'grid'
plt.show()