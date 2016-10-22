# UiA Lecture

Code is currently a mess aka. spaghetti code. 

### How it works
* [x] Step 1: Collect HTML from http://www.uia.no/video site that contains lecture for [MA-209](https://video.uia.no/category/Undervisning%3EFakultet+for+teknologi+og+realfag%3EMA-209).
* [x] Step 2: Filter out date and how many people have watched each lecture.
* [x] Step 3: Dump data to file
* [ ] Step 4: Alternatively, the user may specify that he wants to dump all the data as .pdf. 
* [ ] Step 5: Write to a .xlsx file. First row holds datetime of execution of the code. 
       * First column holds date of lecture. Second column holds how many have watched when the first execution is done. 
       * Third column holds date of lecture. Fourth column holds how many have watched when the second execution is done. 
       * ...and so on
* [ ] Step 6: Delta count - compare how many more people have watched each lecture since last execution. A column on the end that shows delta-viewers. 

### Known issues
Only extracts data from the 16 last videos on the webpage even though there are 36 (at this moment). 
This is due to the fact that the html sourcecode, for some weird reason, isn't showing all of the info. 

Update: The 'weird reason' for this is that the page requires the user to scroll down to load rest of the videoes. 
        Only when the user scrolls down he or she can view rest of the data. This is because there's a javascript that 
        runs in the background when the user scrolls down. 

### Libraries
```requests``` is used to collect full html. 
```bs4``` and ```re``` is used to filter out desired info. 
```datetime``` is used to name files according to current date. 

