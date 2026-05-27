import torch
t = torch.tensor([[ 1,  2,  3,  4,  5,  6],
                  [ 7,  8,  9, 10, 11, 12]])
# view的作用是改变张量的形状，但不改变数据的内容
t_view1 = t.view(3, 4)
print(t_view1)
t_view2 = t.view(4, 3)
print(t_view2)