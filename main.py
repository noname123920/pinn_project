import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = torch.tanh(self.fc1(x))
        x = self.fc2(x)
        return x

net = Net()

# Данные
x_data = torch.linspace(-3, 3, 100).reshape(-1, 1)
y_data = x_data ** 2

# Функция потерь и оптимизатор
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.01)

# Цикл обучения
for epoch in range(2000):
    y_pred = net(x_data)
    loss = loss_fn(y_pred, y_data)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f"Эпоха {epoch}, loss = {loss.item():.6f}")


x = torch.tensor([[2.0]])
y = net(x)
print(y)