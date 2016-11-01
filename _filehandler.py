import datetime
import os


def getDate():

    # get todays date
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d_%H%M')


def createResultsDir():

    # create subdirectory to put results inside
    try:
        os.mkdir(os.curdir + "/results")
    except:
        print("Directory already exists.")


def createFile(text=""):

    # subdirectory where results should reside
    createResultsDir()

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
        file.write(text)
        file.write("--------------------------------------------\n")