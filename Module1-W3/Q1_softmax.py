import torch
import torch.nn as nn

# test library output
soft_max = nn.Softmax()
data = torch.Tensor([1, 2, 3])
output = soft_max(data)
print(output)


# my Softmax function
class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x, dim=-1, keepdim=True)
        return exp_x / sum_exp_x


# my SoftmaxStable function
class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x, dim=-1, keepdim=True).values
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x, dim=-1, keepdim=True)
        return exp_x / sum_exp_x


my_soft_max = Softmax()
my_soft_max_stable = SoftmaxStable()

my_soft_max_output = my_soft_max(data)
my_soft_max_stable_output = my_soft_max_stable(data)

print(my_soft_max_output)
print(my_soft_max_stable_output)
