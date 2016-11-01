import requests as rq
from bs4 import BeautifulSoup
import re
import _filehandler


r = rq.get("https://video.uia.no/category/Undervisning%3EFakultet+for+teknologi+og+realfag%3EMA-209")

soup = BeautifulSoup(r.text, "html.parser")


# get title (unfiltered)
class_with_title = soup.find_all(class_="media-heading")
str_class_with_title = str(soup.find_all(class_="media-heading"))
# find lecture (filtered)
find_date = re.findall(r"Time \d.+\d", str_class_with_title)
#find_date_sub = re.sub(r"(Time \d)(.+\d)", r'(\2) \1', str_class_with_title)    # change order on viewers and lecture


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

print("Viewers-count table:", viewers)
print("Lecture table:\t\t", find_date)

print()
print("-----")


from collections import OrderedDict
biblio_ordered = OrderedDict()

biblio = {}
counter = -1

for element in find_date:
    counter += 1
    info = "Lecture:", element, "\t", "Watched:", viewers[counter]
    infoo = "Lecture: %s \t Watched: %s" % (element, viewers[counter])
    print(infoo)

    _filehandler.createFile(infoo+"\n")
    #createFile(infoo+"\n")

    # put in dictionary in declared order using OrderedDict
    biblio_ordered[element] = viewers[counter]

print()

# NOTE: Dictionary is for when script is further developed to put results in .csv
# # print content inside dictionary
# for key, value in biblio_ordered.items():
#     print(key + ":\t\t" + value)

print("Lectures that match:", len(div_with_phoneData))


# TODO: Add requirements.txt-file - run 'pip freeze' to get version of all modules installed.
# TODO: structure code, rename variables, possibility to add additional courses


# Git problem: http://git.661346.n2.nabble.com/can-anybody-explain-the-following-to-a-git-noob-td2955567.html

# For .exe file
input("Press any key to exit.")

