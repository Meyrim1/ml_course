import pandas as pd

df = pd.read_csv("data/cars_fuel_efficiency.csv")
print("Shape:", df.shape)
print()
print("Types:")
print(df.dtypes)
print()
print("Stats:")
print(df.describe())
print()
print("Пропуски:")
print(df.isna().sum())