import torch

x = torch.tensor(2.0, requires_grad=False)
t = torch.tensor(3.0, requires_grad=True)

f = x**2 + t**3

f.backward()

print("df/dx = ", x.grad)
print("df/dt = ", t.grad)