import random
n = input ("What is your name : ")
print("Alright", n ,"Welcome to your math Quiz : ")
score = 0
question = 0
finish = False 
ops = ['+','-','*', '//']
rand1 = random.randint (1,10)
rand2 = random.randint (1,10)
operation = random.choice(ops)
maths = eval(str(rand1) + operation + str(rand2))
print("Your question is:" , rand1 , operation , rand2 ,)
question = question + 1 
d = int(input('what is your :'))
if d == maths:
        print ('corrent')
        score = score + 1 
else:
       print ("Incorrent.the corrent answer is :" , maths)  




