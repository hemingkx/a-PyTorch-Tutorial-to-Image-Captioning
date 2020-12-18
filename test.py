import torch
print(torch.__version__)

x = torch.Tensor([1.0])           # 声明一个变量
xx = x.cuda()                     # 将变量转换到GPU上
print(xx)

from torch.backends import cudnn         # 导入模块
cudnn.is_acceptable(xx)