Principal = float(input("Enter the Pricipal Amount : "))
Time = float(input("Enter the Time (the number of years) : "))
Rate = float(input("Enter Interest rate : "))
Simple_interest = lambda P,t,r:( P*t*r) //100
print("Simple interest rate is: " ,Simple_interest(Principal,Time,Rate))


    