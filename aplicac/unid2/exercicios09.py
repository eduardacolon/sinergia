import numpy as np
import math

#1

vet1 = np.array([2, 4, 6, 8])
prim_ped = vet1 * 2
print(prim_ped)

seg_ped = prim_ped + 10
print(seg_ped)

#2

a = np.array([1,2,3])
b = np.array([4,5,6])

soma = a + b
print(soma)

sub = a - b
print(sub)

mult = a * b
print(mult)

np.dot(a, b)
print(np.dot(a, b))
#R = faz a multiplacção de cada elemento do vetor a pelo correspondente elemento do vetores e depois soma os resultados
R = 1*4 + 2*5 + 3*6
print(R)

v = np.array([10,20,30,40,50])
print(v)
print(v[0:3])
print(v[2 : 5])
print(v[::2])

v = np.array([5, 10, 15, 20])
soma = (np.sum(v))
print(soma)

media = np.mean(v)
print(media)

#np.sum() → soma tudo
#np.mean() → média (soma ÷ quantidade)