from numpy.random.mtrand import randint
import math
import predictor

x = list(range(0, 101, 1))
for i in range(0, len(x), 1):
    x[i] = x[i] / 2
y = list()
for i in range(0, len(x), 1):
    y.append(randint(0, 100))
y.sort()
y.reverse()
y[0] = 100
prec = [0]
LR = predictor.Predictor()
LR.añadirDatos(y, x, 100)
print(LR)
punto0 = LR.predecirX(prec)
print(punto0)
print(LR.predecirY(punto0))
for i in range(0, len(x), 1):
    y[i] = randint(0, 100)
y.sort()
y.reverse()
LR.añadirDatos(y, x, 100)
print(LR)
punto0 = LR.predecirX(prec)
print(punto0)
print(LR.predecirY(punto0))
punto = math.ceil(punto0[0])
print(punto)
prec = list(range(0, punto, 1))
prec.append(punto0[0])
print(prec)
print(LR.predecirY(prec))
