num1 = int (input("Enter the marks obtaind out of 100 in subject-1 : "))
num2 = int (input("Enter the marks obtaind out of 100 in subject-2 : "))
num3 = int (input("Enter the marks obtaind out of 100 in subject-3 : "))
num4 = int (input("Enter the marks obtaind out of 100 in subject-4 : "))
num5 = int (input("Enter the marks obtaind out of 100 in subject-5 : "))
num6 = int (input("Enter the marks obtaind out of 100 in subject-6 : "))

total, avarage, percentage = None, None, None

total= (num1+num2+num3+num4+num5+num6)
avarage = ((num1+num2+num3+num4+num5+num6)/6)
percentage = ((total/600)*100)

print("Total marks obtained : ", total)
print("Avarage marks obtained : ", avarage)
print("Percentage marks obtained : ", percentage)
