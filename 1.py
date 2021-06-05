import torch 


x = torch.empty(5,3)
print(x)


x1 = torch.zeros(5,3, dtype=torch.long)

print(x1)


x2 = torch.tensor([5.5, 3])

print(x2)
