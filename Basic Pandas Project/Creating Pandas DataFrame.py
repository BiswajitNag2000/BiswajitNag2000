import pandas as pd

df = pd.DataFrame(columns=["Name", "Age", "Roll No."])
parts = int(input("Enter The number of Student Record you want to store :-"))

#for _ in range(parts):
for _ in range(parts):
  name = input("Enter The Name of Student :")
  age = input("Enter The Age of The Student in Years :")
  rollno = input("Enter The Roll No of The Student :")
  df1 = pd.DataFrame(data=[[name,age,rollno]],columns=["Name", "Age", "Roll No."])
  df = pd.concat([df, df1], axis=0)


df.index = range(len(df.index))
print("The Data Frame is-____")
print(df)