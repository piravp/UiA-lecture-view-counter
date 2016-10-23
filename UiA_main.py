import requests as rq
from bs4 import BeautifulSoup
import re
import datetime


def getDate():

    # get todays date
    now = datetime.datetime.now()
    return now.strftime('%d-%m-%Y')


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

r = rq.get("https://video.uia.no/category/Undervisning%3EFakultet+for+teknologi+og+realfag%3EMA-209")

soup = BeautifulSoup(r.text, "html.parser")

# hent ut alle span-tagsene med class='stat'    (dette er klassen som inneholder antall visninger)
#span_with_stat = str(soup.find_all("span", "stat"))

# hent ut tallene
#find_number = re.findall(r"<\/span>\d{1,}", span_with_stat)

# find_number = re.findall(r"<\/span>\d{1,}", span_with_stat)
# print(len(find_number))
#
#
# print(find_number)

# get title (unfiltered)
class_with_title = soup.find_all(class_="media-heading")
str_class_with_title = str(soup.find_all(class_="media-heading"))
# finn forelesning (filtered)
find_date = re.findall(r"Time \d.+\d", str_class_with_title)
find_date_sub = re.sub(r"(Time \d)(.+\d)", r'(\2) \1', str_class_with_title)    # bytte rekkefølge på antall og dato


# get number of people watched (unfiltered)
div_with_phoneData = soup.find_all(class_="phoneData")
str_div_with_phoneData = str(soup.find_all(class_="phoneData"))
# make sure we're getting the right number (half-filtered)
find_number_and_spans = re.findall(r"<\/span>\d{1,}", str_div_with_phoneData)
viewers = []
j = 0
for i in find_number_and_spans:
    viewers.append(find_number_and_spans[j].strip('</span>'))
    j+=1

print(viewers)
print()

# remove span-tag, print only number
# for spanNumber in find_number:
#     number = spanNumber.strip('</span>')
#     print(number)
print("-----")
print(find_date)


biblio = {}
counter = -1

from collections import OrderedDict
biblio_ordered = OrderedDict()


for element in find_date:
    counter += 1
    info = "Lecture:", element, "\t", "Watched:", viewers[counter]
    infoo = "Lecture: %s \t Watched: %s" % (element, viewers[counter])
    print(infoo)
    createFile(infoo+"\n")

    # biblio[element] = viewers[counter]  # putting in dictionary fucks up the order
    biblio_ordered[element] = viewers[counter]


# for key, value in biblio.items():
#     print(key + ":\t" + value)

# for key, value in biblio_ordered.items():
#     print(key + ":\t" + value)

print()
# print(biblio_ordered)
print("Lectures that match:", len(div_with_phoneData))

# TODO: structure code, rename variables, possibility to add additional courses

# Git problem: http://git.661346.n2.nabble.com/can-anybody-explain-the-following-to-a-git-noob-td2955567.html


