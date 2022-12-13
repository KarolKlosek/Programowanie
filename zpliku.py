print("choose a file ")
print("1 - Lorem Ipsum")
print("2 - Gaius Iulius Gaii")
print("3 - Imperium Romanum")
print("4 - Publius Vergilius Maro")

choseeFile = input("Enter File Number: ")

choseeFile = int(choseeFile)



if choseeFile == 1:
    print("1")
    chosenFile = "FileToRead/1.txt"
elif choseeFile == 2:
    print("2")
    chosenFile = "FileToRead/2.txt"
elif choseeFile == 3:
    print("3")
    chosenFile = "FileToRead/3.txt"
elif choseeFile == 4:
    print("4")
    chosenFile = "FileToRead/4.txt"
else:
    print("Wrong number")


asdf = "'FileToRead/1.txt'"

with open(asdf, 'r') as fp:
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
