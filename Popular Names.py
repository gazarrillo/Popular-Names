#Initializing List
boy_list = []
girl_list = []
#Opening File
boy_file = open('BoyNames.txt', 'r')
girl_file = open('GirlNames.txt','r')
#Reading Files and Appending Lists
for linefromfile in boy_file:
    linefromfile = linefromfile.rstrip('\n')
    boy_list.append(linefromfile)
boy_file.close()

for linefromfile in girl_file:
    linefromfile = linefromfile.rstrip('\n')
    girl_list.append(linefromfile)
girl_file.close()
#Name Input
name = input("Enter a person's name or 'stop' to stop: ")
#Loop
while name != 'stop':
    boy = 0
    girl = 0
#Going through both name lists
    for i in range(0, len(girl_list)):
        if name == girl_list[i]:
            print(name, "is a popular name and it's ranked: ", girl_list.index(name) + 1)
            girl = 1
        if name == boy_list[i]:
            print(name, "is a popular name and it's ranked: ", boy_list.index(name) + 1)
            boy = 1
    if girl == 0:
        print(name, "is not a popular girls name")
    if boy == 0:
        print(name, "is not a popular boys name")
    print('')
    name = input("Enter a person's name or 'stop' to stop: ")
