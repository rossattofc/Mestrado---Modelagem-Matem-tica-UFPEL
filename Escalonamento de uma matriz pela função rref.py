from sympy import *

a = ([[3, 2, -1, 0],
     [1, 3, 1, 1],
     [2, 2, -2, 2]])


M = (Matrix(a))

print (M)
M_esc = M.rref()
print (M_esc)
