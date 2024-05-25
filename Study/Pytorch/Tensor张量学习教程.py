import os
import pandas as pd
import torch

x=torch.arange(4,dtype=torch.float32)
print(x,x.sum())

"""
    axis=
    0表示行/纵向求和 1表示列/横向求和
    keepdims=True 表示不降维求和
"""

