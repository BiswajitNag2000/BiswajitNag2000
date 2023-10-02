file = open('DIY Dataset/Poem.txt', "r")
for line in file:
    print(line, end="")
file.close()