


# get current date (formatted)
def getDate():
    import datetime
    now = datetime.datetime.now()
    return now.strftime('%d-%m-%Y')


def createFile(tekst=""):

    filename = getDate() + ".txt"
    print(filename)

    with open(filename, 'a') as file:
        string = "Date checked: " + filename.strip('.txt') + "\n"
        file.write(string)
        file.write(tekst)
        file.write("--------------------------------------------\n")



createFile()