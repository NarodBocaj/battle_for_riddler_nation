import pandas as pd 

files = ["castle-solutions.csv", "castle-solutions-2.csv", "castle-solutions-3.csv", "castle-solutions-4.csv"]
dataframes = []

for file in files:
    df = pd.read_csv("./prev_battles/" + file)
    dataframes.append(df)

all_battles = pd.concat(dataframes, ignore_index=True)

print(all_battles)