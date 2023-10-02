import pandas as pd
print ("The series is : ")
ser = pd.Series(["India","Canada","Australia","Japan","Germany","France"],index=["IND","CAN","AUS","JAP","GER","FRA"])
print(ser)
print("Lenth of the serise is :", len(ser))
print("Shape of the serise", ser.shape)
print("Size of the serise", ser.size)