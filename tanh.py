import torch
import matplotlib.pyplot as plt

# x = torch.tensor([-3.0, -1.0, 0.0, 1.0, 3.0])
# y = torch.tanh(x)
# print(y)

# for x_val in [-5.0, -2.0, -1.0, 0.0, 1.0, 2.0, 5.0]:
#     print(f"tanh({x_val}) = {torch.tanh(torch.tensor(x_val)).item():.4f}")

x = torch.linspace(-5, 5, 200)
y = torch.tanh(x)

plt.plot(x.numpy(), y.numpy())
plt.show()