import datetime


# get current date (formatted)
def getDate():

    # get todays date
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d_%H%M')


def createFile(tekst=""):

    # file with filename that equals todays date
    sub_directory = "./results/"
    date = getDate()
    file_extension = ".txt"
    filename_path = "".join((sub_directory, date, file_extension))
    print(filename_path)
    print(date)

    with open(filename_path, 'a') as file:
        first_line = "Date checked: " + date + "\n"
        file.write(first_line)
        file.write(tekst)
        file.write("--------------------------------------------\n")



createFile()