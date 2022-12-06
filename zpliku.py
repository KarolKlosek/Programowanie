
with open('readme.txt', 'r') as plik:
    print("Wpisz numer linii :")
    
    nrlini = []
    nrlini.append(int(input()))
    linijkakonkretna = []
    try:
        for i, line in enumerate (plik):
            if i in nrlini:
                linijkakonkretna.append(line.strip())
            elif i > 37:
                break
    except:
        print("Error")
    print(nrlini, linijkakonkretna)
