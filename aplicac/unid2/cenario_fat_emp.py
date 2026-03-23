import numpy as np

precos = np.array([100, 50, 20])
quantidades = np.array([10, 5, 8])

faturamento = precos * quantidades
print(faturamento)

total = np.sum(faturamento)
print(total)

indice_max = np.argmax(quantidades)
print(indice_max)
