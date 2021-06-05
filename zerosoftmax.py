import torch 
import matplotlib.pyplot as plt
import numpy as np 
import random 

num_inputs = 2 
num_examples = 1000

true_w = [2, -3.4]
true_b = 4.2

features = torch.randn(num_examples, num_inputs, dtype=torch.float32)

labels = true_w[0] * features[:, 0] + true_w[1] * 
