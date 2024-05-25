# %matplotlib inline
import numpy as np
import torch
from torch.distributions import multinomial 
import torchvision 
from matplotlib_inline import backend_inline
from d2l import torch as d2l

if torch.cuda.is_available():
    print(1)
else :
    print(0)