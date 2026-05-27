import torch

x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# torch.triu函数用于返回输入张量的上三角部分，其他部分用0填充。
# 参数diagonal指定了对角线的位置，默认值为0，表示主对角线。正值表示上方的对角线，负值表示下方的对角线。
print(torch.triu(x))
# 输出:
# tensor([[1, 2, 3],
#         [0, 5, 6],
#         [0, 0, 9]])

print(torch.triu(x, diagonal=-1))
# 输出:
# tensor([[1, 2, 3],
#         [4, 5, 6],
#         [0, 8, 9]])