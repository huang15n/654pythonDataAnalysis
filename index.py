from tkinter import *
import re
import operator
from crawler import Crawler # this is to include the self-defined crawler class 
#the class uses the argument , text file name for constructor, csv name for cosntructor 
import requests
from sort import insertion_sort, merge_sort, bubble_sort, quick_sort,bucket_sort
import readFileToSort
import string
import readFileToKeyword
from matching import boyer_moore
from matching import bruteforce
from matching import kmp
from matching import trie
from collections import Counter
import collections 
import heapq

def crawlWebSite():
	global textForTitles
	linkToSearch = webLink.get()
	fileNameOutput = fileName.get()
	max_page = pages.get()
	crawler_for_links=Crawler()
	connection = requests.get(linkToSearch)
	pattern=re.compile("(https:)\/\/[a-zA-Z]*\.[a-zA-Z]*\.[a-zA-Z]*/[a-zA-Z]*/[a-zA-Z0-9-]*/[a-zA-Z0-9]*/(bn_)[a-zA-Z0-9]*")
   	
	if (pattern.match(linkToSearch) and connection.status_code == 200):
			textForTitles = crawler_for_links.crawl_to_pages(max_page,fileNameOutput,linkToSearch)
			labelForSiteAgain = Label(window,text="processed given link",bg="green",width=50).grid(row=4,column=1)
			text = textForTitles.split(' ')
			for word in text: 
				string_list_to_search.append(word)


			
 			
	else: 
			labelForSiteAgain = Label(window, text = linkToSearch+" is not a valid address", bg= "red",width=50).grid(row=4,column=1)
	#labelForSiteAgain = Label(window,text=link).pack()
def sorting():
	fileNameToSort = fileName.get()
	merge_sort_time = 0
	quick_sort_time = 0
	heapsort_time = 0
	 
	if algorihtm1.get():
		merge_sort_time = readFileToSort.readFilesAndSort(fileNameToSort,1)
		Label(window, text = "merge sort took " + str(merge_sort_time) + "millisecond",width=50).grid(row=13,column=0)
		print(merge_sort_time)

	if algorihtm2.get():
		quick_sort_time = readFileToSort.readFilesAndSort(fileNameToSort,2)
		Label(window, text = "quick sort took " + str(quick_sort_time) + "millisecond",width=50).grid(row=14,column=0)
		print(quick_sort_time)
	if algorihtm3.get():
		heapsort_time = readFileToSort.readFilesAndSort(fileNameToSort,3)
		Label(window, text = "heap sort took " + str(heapsort_time) + "millisecond",width=50).grid(row=15,column=0)
		print(heapsort_time)
	
	



def searchKeyWord():
	fileNameToKeyword = fileName.get()
	keyword_to_search = keyword.get()
	if matching1.get():
		(textToSearch,timeToSearch) = readFileToKeyword.readFilesToKeyword(fileNameToKeyword,keyword_to_search,1)
		Label(window, text = "brute force found "+keyword_to_search+" appeared " + str(textToSearch)+" times, time spent on"+str(timeToSearch) ,width=50).grid(row=22,column=0)
	if matching2.get():
		(textToSearch,timeToSearch) = readFileToKeyword.readFilesToKeyword(fileNameToKeyword,keyword_to_search,2)
		Label(window, text = "boyer moore found "+keyword_to_search+" appeared " + str(textToSearch)+" times, time spent on"+str(timeToSearch) ,width=50).grid(row=23,column=0)
	if matching3.get():
		(textToSearch,timeToSearch) = readFileToKeyword.readFilesToKeyword(fileNameToKeyword,keyword_to_search,3)
		Label(window, text = "KMP found "+keyword_to_search+" appeared " + str(textToSearch)+" times, time spent on"+str(timeToSearch) ,width=50).grid(row=24,column=0)
	
def enter_keyword1(key):
	global keyword_string
	global textForTitles
	keyword_string += key.char
	cnt = Counter()
	my_dictionary = {}
	show_options = {}

	print(key.char)
	if((key.char > '!' and key.char < 'z' or key.char == ' ') and len(keyword_string) >= 1):
		print(keyword_string)
		patternForSearchEngine = re.compile(keyword_string+"[a-zA-Z]+")
		textToMatchPattern = str(textForTitles)
		word_to_search = str(keyword)
		


		for words in string_list_to_search:
			cnt[words] += 1
			if patternForSearchEngine.match(words):
				print(words + " :" +str(cnt[words]))
				my_dictionary[words] = cnt[words]


		sorted_dictionary = sorted(my_dictionary.items(),key=operator.itemgetter(1),reverse = True)
		dropdown_list1 = OptionMenu(window,*sorted_dictionary).grid(row=5,column=2)
		for key in sorted_dictionary:
			print(key)


	else :
		keyword_string = keyword_string[0:len(keyword_string)-2]
		print(keyword_string)
	
		
def enter_keyword2(key):
	global keyword_string2
	global textForTitles2
	keyword_string2 += key.char
	cnt = Counter()
	my_dictionary = {}
	show_options = {}
	wordList = []

	print(key.char)
	if((key.char > '!' and key.char < 'z' or key.char == ' ') and len(keyword_string2) >= 1):
		print(keyword_string2)
		textToMatchPattern = str(textForTitles2)
		word_to_search = str(keyword)
		


		inverted_index = collections.defaultdict(set)
		wordCollectionSet = set()
		for words in string_list_to_search:
			wordCollectionSet.add(words)

		unique_word_sorted = sorted(wordCollectionSet)
		inverted_index = collections.defaultdict(set)
		for i , word in enumerate(unique_word_sorted):
			for c in word.lower():
				inverted_index[c].add(i)

	

		for i in set.intersection(*(inverted_index[c] for c in keyword_string2)):
			wordList.append(unique_word_sorted[i])

		dropdown_list2 = OptionMenu(window,*wordList).grid(row=6,column=2)






	else :
		keyword_string2 = keyword_string2[0:len(keyword_string2)-2]
		print(keyword_string2)
	
		
			







window=Tk()
webLink = StringVar()
fileName = StringVar()
fileNameOutput = StringVar()
keyword = StringVar()
pages = IntVar()
algorihtm1 = IntVar() 
algorihtm2 = IntVar()
algorihtm3 = IntVar()
textForTitles = StringVar()
textForTitles2 = StringVar()
matching1 = IntVar()
matching2 = IntVar()
matching3 = IntVar()
keyword_string = ""
keyword_string2 = ""
string_list_to_search = []



window.title("654 Algorithm Analysis")
window.geometry("1000x1000")
labelForTitle = Label(window,text="Algorithm Analysis Tool",font=("Helvetica", 40,"bold")).grid(row=0)
 

labelForWebSite = Label(window,text ="Enter the Ebay's data you would like to crawl:",font=("Time New Roman",20)).grid(row=1,column=0,sticky=W)

websiteText=Entry(window,textvariable=webLink).grid(row=1,column=1,sticky=E)

labelForFileName = Label(window,text="Please enter the output file name",font=("Time New Roman",20)).grid(row=2,column=0,sticky=W)
fileNameText = Entry(window,textvariable=fileName).grid(row=2,column=1,sticky=E)

labeForNumbersOfPages = Label(window,text="how many pages of data you want",font=("Time New Roman",20)).grid(row=3,column=0,sticky=W)
pagesOfData = Entry(window,textvariable=pages).grid(row=3,column=1,sticky=E)



submitButtonForWeb=Button(window,text="Let's Crawl",command=crawlWebSite,width=50)
submitButtonForWeb.grid(row=4,column=0,sticky=E)

labelForKeyWord = Label(window,text = "Please enter keyword below for first engine:").grid(row=5,column=0)
keyword_entry_to_search = Entry()
keyword_entry_to_search.grid(row=5,column=1)
keyword_entry_to_search.bind("<Key>",enter_keyword1)


labelForKeyWord2 = Label(window,text = "Please enter keyword below for second engine:").grid(row=6,column=0)
keyword_entry_to_search2 = Entry()
keyword_entry_to_search2.grid(row=6,column=1)
keyword_entry_to_search2.bind("<Key>",enter_keyword2)
 




labelForAlgorithms = Label(window,text="please specify at least 2 algorihtms that you would like to sort the obtained data below:",font=("Times",20,"bold")).grid(row=8,column=0)
Checkbutton(window,text="Merge Sort",variable=algorihtm1,onvalue=1,offvalue=0).grid(row=9,column=0)
Checkbutton(window,text="Quick Sort",variable=algorihtm2,onvalue=1,offvalue=0).grid(row=10,column=0)
Checkbutton(window,text="Heap Sort",variable=algorihtm3,onvalue=1,offvalue=0).grid(row=11,column=0)
submitButtonForSortings= Button(window,text="Let's Sort",command=sorting,width=50).grid(row=12,column=0,sticky=E)
 

labelForSearchEngine = Label(window,text="Enter the keyword to count frequencies and select at least 2 algorithms :",font=("Times",20,"bold")).grid(row=16,column=0)
searchKeyWordSearchEngine = Entry(window,textvariable=keyword).grid(row=17,column=1)
Checkbutton(window,text="Brute Force",variable=matching1,onvalue=1,offvalue=0).grid(row=18,column=0)
Checkbutton(window,text="Boyer Moore",variable=matching2,onvalue=1,offvalue=0).grid(row=19,column=0)
Checkbutton(window,text="KMP",variable=matching3,onvalue=1,offvalue=0).grid(row=20,column=0)
submitButtonForSearchEngine = Button(window,text="Search Keyword Now",command =searchKeyWord,width=50).grid(row=21,column=0)





window.mainloop()

