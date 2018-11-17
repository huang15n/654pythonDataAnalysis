# Summary
To emulate the functionality of a mini search engine combines different sorts of algorithm, string manipulation and data structure libraries.
The thought process is comprised of scrapping data entry from the ecommerce website user provided, saving crawled data into the csv files, sorting data through its category and price, and keeping organized data into local csv files. Most importantly, autocompletion and ranking systems(e.g. how many words in the entire system, top ranking words shows ahead). 

# Disclaimer 
The purpose of this project is served to apply the existing python algorithm library to accomplish the tasks mention above and calculation the time efficiency and resource used.The algorithms provided was committed through various resource and comments inside the algorithms.py like files mentioned the implementation process and contributors.

# Introduction
The entire project was built in a way that user finds the ecommerce website they desire to analyze, strip the html tags and save the data entry individually into the local spreadsheet. Later, the graphical user window will allow the user to enter the keywords and accomplish autocompletition functionality 

# Usage
The index.py includes graphical applies user interface window Python's Tinker library where the user launch the program.
In the website url section, simply inputs the urls that users desire to make the analysis and the system will automatically check the validty of urls that is provided. Afterwards, the system needs the user to punch in how many pages will be crawled and it automatically keep track of the data. Once the fetching process is done, users have can choose to sort the data in accordance with price that simulates the basic spreadsheets. 
The browser simulation part is done by two input which serves as autocompletion algorithm that some modern browsers run inverted indexes and hash table. Due to the time frame, it was unable to perform more sophisticated tasks like showing the entire row through the product names.
