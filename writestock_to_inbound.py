import pandas as pd
from pandas import DataFrame
df = pd.read_csv('test_portofolie.csv')

print(df)

print()

columns = []
for header in df.columns:
    columns.append(header)
    print(header)

rows = []

print()

#print(df.values[:-1])

dict = {}
list = []

#Setter feil key, skal være fra kolonnene
#må lage liste over valgte aksjer, og finne indeksene deres
# for å så velge kolonnenavn og resterende info.
for mark in df.values[:-1]:
    #print(df[mark].values[:-1])
    print(mark)
    dict[mark[0]] = mark[1:].tolist()

print("LESE DICT")
print(dict)

df_to_Store = pd.DataFrame(dict, columns = columns )
print("LESE NY DF")

print(df_to_Store)

df_to_Store.to_csv('df_to_Store.csv', header =True)
