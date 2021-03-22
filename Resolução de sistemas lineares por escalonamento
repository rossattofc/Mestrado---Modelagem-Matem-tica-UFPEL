import numpy as np
import sys

# Inserir quantas incógnitas existem no sistema
n = int(input('Digite o número de incógnitas: '))

# Cria uma matriz com zeros para comparar e guardar os valores da matriz escalonada
a = np.zeros((n,n+1))

# Matriz para guardar as soluções do sistema
x = np.zeros(n)

# Método para imprimir apenas valores com duas casas decimais
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

# Leitura dos coeficientes da matriz, com as constantes inclusas, no formato 
# [x1 y1 z1 a]
# [x2 y2 z2 b]
# [x3 y3 z3 c]
print('Digite os coeficientes da matriz:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Aplicação do escalonamento
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Foi detectada uma divisão por zero, reveja os valores do sistema')
        
    for j in range(n):
        if i != j:
            razao = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - razao * a[i][k]
                print (a)

# Solução do sistema utilizando o método de pivotamento parcial

for i in range(n):
    x[i] = a[i][n]/a[i][i]

print('\nAs soluções do sistema são: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
