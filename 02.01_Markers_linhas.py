import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r', marker = 'o', ms = 20, mec ='r', mfc = 'black') 
## 'o:r' Serve para modificar a 'linha' formato: marker|line|color                                     
## 'ms'  Serve para modificar o tamanho do 'ponto'
## 'mec' Serve para mudar a cor da BORDA do 'ponto'
## 'mfc' Serve para mudar a cor INTERNA do 'ponto'
plt.show()


'''     Modificadores da linha
'-' 	Solid line 	
':' 	Dotted line 	
'--' 	Dashed line 	
'-.' 	Dashed/dotted line
'''

'''     Modificadores de Cores (PODE USAR HEXADECIMAL)
'r' 	Red 	
'g' 	Green 	
'b' 	Blue 	
'c' 	Cyan 	
'm' 	Magenta 	
'y' 	Yellow 	
'k' 	Black 	
'w' 	White
'''
