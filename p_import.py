import pandas as pd


data = pd.read_csv('test_data.txt', header=None, sep=';')
print(data.iloc[:, 1])
