# UiA Lecture View Counter

A script that checks how many views each MA-209 lecture (lecture @ UiA) has recieved. Results are then dumped to .txt in a formatted fashion. 
Code needs refactoring.  

### Installation 
If you already have python installed (external modules required), you can run this from a command shell:
```
git clone https://github.com/piravp/UiA-lecture-view-counter
cd UiA-lecture-view-counter
pip install -r requirements.txt
python UiA_main.py
```

If you don't have python installed or don't want to set it up:
Download the latest executable from [releases](https://github.com/piravp/UiA-lecture-view-counter/releases).


### How it works
* [x] Step 1: Collect HTML from http://www.uia.no/video site that contains lecture for [MA-209](https://video.uia.no/category/Undervisning%3EFakultet+for+teknologi+og+realfag%3EMA-209).
* [x] Step 2: Filter out date and how many people have watched each lecture.
* [x] Step 3: Dump data to file
* [x] Step 4: Make an executable (.exe). 
* [ ] Step 5: Alternatively, the user may specify that he wants to dump all the data as .pdf. 
* [ ] Step 6: Write to a .xlsx file. First row holds datetime of execution of the code. 
       * First column holds date of lecture. Second column holds how many have watched when the first execution is done. 
       * Third column holds date of lecture. Fourth column holds how many have watched when the second execution is done. 
       * ...and so on
* [ ] Step 7: Delta count - compare how many more people have watched each lecture since last execution. A column on the end that shows delta-viewers. 

### Known issues
Only extracts data from the 16 last videos on the webpage even though there are 36 (at this moment). 
This is due to the fact that the html sourcecode isn't showing all of the info. 

*Update: The 'weird reason' for this is that the page requires the user to scroll down to load rest of the videoes.* 
        *Only when the user scrolls down can he view rest of the data. This is because there's a javascript script that* 
        *is fired to a API only when the user scrolls down.* 

### Libraries
- ```requests``` is used to collect full html. 
- ```bs4``` and ```re``` are used to filter out desired info. 
- ```datetime``` is used to name files according to current date. 
- ```collections.OrderedDict``` is used instead of the built-in dictionary because it messes up the order when each key/pair-value is declared. 
- ```os``` to create directory. 
