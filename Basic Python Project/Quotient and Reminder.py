def add(Divident,Divisor):
    i = (Divident//Divisor)
    print ('Quotient : ',i)
    s = (Divident%Divisor)
    print ('Remainder : ',s)
    return (i,s)
Divident = int (input('Enter the Divident : '))
Divisor = int (input('Enter the Divisor : '))
print (add(Divident,Divisor))