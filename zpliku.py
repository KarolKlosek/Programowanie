
with open('readme.txt', 'r') as fp:
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