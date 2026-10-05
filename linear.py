import torch
import torch.nn as nn

layer = nn.Linear(2, 3) # y=x*W+b

x = torch.tensor([[1.0, 2.0]])

print(layer(x))
print(type(layer))
print(layer.weight)
print(layer.bias)