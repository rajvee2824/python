import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

print(df.loc[0])
print(df.loc[[0, 1]])


df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)

df = pd.read_csv('data.csv')

print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)

df = pd.read_json('data.json')

print(df.to_string())
