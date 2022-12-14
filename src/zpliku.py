

print("choose a file ")
print("1 - Lorem Ipsum")
print("2 - Gaius Iulius Gaii")
print("3 - Imperium Romanum")
print("4 - Publius Vergilius Maro")

choseeFile = int(input("Enter File Number: "))

if choseeFile == 1:
    chosenFile = "FilesToRead/1.txt"
elif choseeFile == 2:
    chosenFile = "FilesToRead/2.txt"
elif choseeFile == 3:
    chosenFile = "FilesToRead/3.txt"
elif choseeFile == 4:
    chosenFile = "FilesToRead/4.txt"
else:
    print("Wrong number")
if choseeFile in range(5):

    with open("{}".format(chosenFile), 'r') as fp:
        file = fp.readlines()
    
    nrLine = int(input("Enter line number:"))
    nrLine = nrLine - 1 
    currentLine = []
    lenFile = len(file)
    
    if lenFile > nrLine + 1:
        for i, line in enumerate (file):
            if i == nrLine:
                currentLine.append(line.strip())
            elif i > lenFile:
                break
        print(currentLine)
    else:
        print("no lines")
else:
    print ("no file")