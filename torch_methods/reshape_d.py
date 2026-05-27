import torch

x = torch.arange(1, 7)  # tensor([1, 2, 3, 4, 5, 6])

y = torch.reshape(x, (2, 3))
print(y)
# 输出:
# tensor([[1, 2, 3],
#         [4, 5, 6]])


# 使用 -1 自动推断
z = torch.reshape(x, (3, -1))
print(z)
# 输出:
# tensor([[1, 2],
#         [3, 4],
#         [5, 6]])