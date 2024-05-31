import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import mlflow
import torch
import torch.nn as nn

#%%  
class SOM(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(SOM, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.weights = nn.Parameter(torch.randn(hidden_dim, input_dim))

    def forward(self, x):
        return torch.matmul(self.weights, x)
# experiment with scratch version of som
