import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model


def sigmoid(x):
    return 1/(1+np.exp(-x))

print(sigmoid(5))
