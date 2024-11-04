import matplotlib.pyplot as plt
import numpy as np

## PLOT 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
## a figura terá 2 linhas, 3 colunas e esse subplot será o primeiro
plt.plot(x,y)
plt.title("Título 1")


## PLOT 2

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
## a figura terá 2 linhas, 3 colunas e esse subplot será o segundo
plt.plot(x,y)
plt.title("Título 2")

## PLOT 3

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
## a figura terá 2 linhas, 3 colunas e esse subplot será o terceiro
plt.plot(x,y)
plt.title("Título 3")

## PLOT 4

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
## a figura terá 2 linhas, 3 colunas e esse subplot será o quarto
plt.plot(x,y)
plt.title("Título 4")


## PLOT 5

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
## a figura terá 2 linhas, 3 colunas e esse subplot será o quinto
plt.plot(x,y)
plt.title("Título 5")

## PLOT 6

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
## a figura terá 2 linhas, 3 colunas e esse subplot será o sexto
plt.plot(x,y)
plt.title("Título 6")



plt.suptitle("Título Mestre")
plt.show() 