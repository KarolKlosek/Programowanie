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
if chosenFile in range(5):
    with open("{}".format(chosenFile), 'r') as fp:
        file = fp.readlines()
    nrLine = []
    nrLine.append(int(input("Enter line number:")))
    currentLine = []
    lenFile = len(file)
    for i, line in enumerate (file):
        if i in nrLine:
            currentLine.append(line.strip())
        elif i > lenFile:
            break
    print(nrLine, currentLine)
else:
    print ("no file")