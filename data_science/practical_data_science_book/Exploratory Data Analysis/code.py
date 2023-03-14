import pandas as pd
from scipy.stats import *

state = pd.read_csv("data/state.csv")

print(state['Population'].mean())
print(trim_mean(state['Population'], 0.1))
print(state['Population'].median())