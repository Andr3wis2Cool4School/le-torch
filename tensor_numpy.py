import torch

tensor = torch.ones(4,4)
print(tensor)

print('First Row', tensor[0])
print('First Column', tensor[:, 0])
print('Last Column', tensor[..., -1])

tensor[:,1] = 0
print(tensor)
