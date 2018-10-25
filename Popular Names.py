def getNamesList(filename):
    """This function reads a file and creates a list with its contents"""
    filename_list = []
    filename = open(filename, 'r')
    for linefromfile in filename:
         linefromfile = linefromfile.rstrip('\n')
         filename_list.append(linefromfile)
    filename.close()
    return filename_list

def checkName(name, nameList):
    """This function checks whether or not a name is in a list, it returns 0 if it's not im the list and its rank in the list if it is"""
    x = 0
    for i in range(0, len(nameList)):
        if name == nameList[i]:
            x = 1
    if x == 0:
        return 0
    else:
        return nameList.index(name) + 1

boy_list = getNamesList('BoyNames.txt')
girl_list = getNamesList('GirlNames.txt')

name = input("Enter a person's name or 'stop' to stop: ")

while name != 'stop':
    if checkName(name, boy_list) > 0:
        print(name, "is a popular boys name and it's ranked: ", checkName(name, boy_list))
    elif checkName(name, girl_list) > 0:
        print(name, "is a popular girls name and it's ranked: ", checkName(name, girl_list))
    if checkName(name, boy_list) == 0:
        print(name, "is not a popular boys name")
    if checkName(name, girl_list) == 0:
        print(name, "is not a popular girls name")
    print('')
    name = input("Enter a person's name or 'stop' to stop: ")
