import torch

a = torch.tensor(5.0)
print(a)

b = torch.tensor([1.0, 2.0, 3.0])
print(b)

c = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(c)

# print(type(a))
# print(b.shape)
# print(c.shape)


# print(b + b)
# print(b * 2)
# print(b ** 2)

print(c @ c)