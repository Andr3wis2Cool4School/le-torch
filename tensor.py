import torch 
import numpy as np 

data = [[1,2], [3,4]]
x_data = torch.tensor(data)

print(x_data)

# shape is a tuple of tensor dimensions

shape = (2,3,) # shape is a tuple

rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print('rand tensor', rand_tensor)
print('ones tensro', ones_tensor)
print('zero tensor', zeros_tensor)

# attributes of a tensor
print(rand_tensor.shape)
print(rand_tensor.size)
print(rand_tensor.dtype)
print(rand_tensor.device)
