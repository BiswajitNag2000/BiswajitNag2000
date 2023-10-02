'''ch = (input("Hello User, Plese Enter a Character: "))
if(ch =="a" or ch == "e" or ch =="i" or ch == "o" or ch == "u" or ch =="A" or ch == "E" or ch =="I" or ch == "O" or ch == "U"):
     print (ch, "is a vowel")
else:
     print (ch,"is a consonant")'''

character = input("Enter a character: ")

if len(character) == 1:
    if character in 'aeiouAEIOU':
        print(f"The character {character} is a vowel.")
    else:
        print(f"The character {character} is a consonant.")
else:
    print("Please enter only a single character.")