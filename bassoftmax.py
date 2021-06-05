import torch
import numpy 
from time import time 

'''
x1 as the size of the house 
x2 as the age of the house 

y as the price of the house 


so we have -->
yhat = x1w1 + x2w2 + b 

'''

a = torch.ones(1000)
b = torch.ones(1000)

start = time()
c = torch.zeros(1000)

for i in range(1000):
    c[i] = a[i] + b[i]

print(time() - start)

start = time()

d = a + b

print(time() - start)

#0.008577585220336914
#5.125999450683594e-05

