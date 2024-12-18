#%%
import pandas as pd
# %%
data = pd.read_csv("KKYLOUIS332.csv")
data.head(10)
print(data.head(10))
print(data.loc[0])
data.describe()
data.dtypes
# %%