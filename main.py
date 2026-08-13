import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')   
df_test['Transported'] = False





