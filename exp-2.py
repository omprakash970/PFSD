import pandas as pd

data = {
    "Name": ["Om", "Rahul", "Anita"],
    "Age": [19, 20, 18],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df[["Age", "Marks"]])
print(df.alloc[1])