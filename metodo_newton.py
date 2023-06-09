# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fFZLZWdk-211be0XCdRm0zu1BPUwM0ZU
"""

from math import *
import numpy as np
import matplotlib . pyplot as plt
def funcion1(x):
    return np.exp(x) + 2**(-x)+ 2*cos(x)-6
def d1(x):
    return np.exp(x) - (np.log(2)/( 2**(x))) -2*sin(x)
    
#Método de newton
# guarda valores iniciales para Newton
pi=1.1
# Ingreso datos de entrada para los diferentes métodos a trabajar
a = 1
b = 2

#guarda valores iniciales del error y del número de iteraciones
tol = 0.000000001  #float(input("Ingrese el valor de la tolerancia: "))
nmax = 20 #float(input("Ingrese el número máximo de iteraciones: "))
error = 100
niter = 0
# Método de  Newton

#Evaluacion de la función en los puntos a, b y m

i=1
print("# iter  \t\t P  \t\t error")
print("{0} \t\t {1:6.4f}  \t {2:6.4f}".format(i, pi, error ))

# ciclo iterativo
while error > tol and i <= nmax:
    fa=funcion1(pi)  
    da=d1(pi)
    p = pi - (fa/da)
    error = abs(p - pi)

    pi=p
    i += 1
    print("{0} \t\t {1:6.6f} \t {2:6.6f}".format(i, p,error ))

print("La raíz de la función dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:6.7f}".format(a,b,p))