# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tBsnnOPWIMxNZfZmXFU002OROQmjPhQw
"""

from math import *
import numpy as np
import matplotlib . pyplot as plt
def fn1(x):
    return 2**(-x)
def gn(x):
    return 2**(-x)
# guarda valores iniciales
i=0
po=1
p=0

tol = 0.00001 #float(input("Ingrese el valor de la tolerancia: "))
nmax = 100 #float(input("Ingrese el número máximo de iteraciones: "))


print("# iter\t\t x_n \t\t g(x_n) \t f(x_n)")

#Método del punto fijo 
# ciclo iterativo
while 17 > i :
  p=gn(po)
  print("{0} \t\t {1:6.6f} \t {2:6.6f} \t {3:6.6f} ".format(i, po,p ,fn1(p) ))

  if abs(p-po) < tol:
      break
  po=p
  i += 1
  

#print("La raíz de la función dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:6.7f}".format(a0,b0,m))
