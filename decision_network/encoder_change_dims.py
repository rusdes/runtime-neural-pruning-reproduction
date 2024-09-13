import torch
import torch.nn as nn
import CONSTANTS

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(torch.cuda.is_available())

class ChangeDims(nn.Module):
    def __init__(self, in_dims, out_dims):
        super().__init__()
        self.fc3 = nn.Linear(in_dims, out_dims)

    def forward(self, x):
        # input 2048, output 128
        x = self.fc3(x)
        return x