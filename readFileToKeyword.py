import csv 
import time 
from matching import boyer_moore
from matching import bruteforce
from matching import kmp

def readFilesToKeyword(filename,keyword,number):
	filename = filename+'.csv'
	keyword_csv = open(filename,"r+")
	reader = csv.reader(keyword_csv)
	data = ""
	start_time = time.time()
	keyword_csv.readline()
	for row in reader:
		data += (row[0])
	if number == 1:
		return (bruteforce.BruteForceMatch(data,keyword),time.time() - start_time)
	if number == 2:
		return (boyer_moore.boyer_moore(data,keyword), time.time() - start_time)
	if number == 3:
		return (kmp.KnuthMorrisPratt(data, keyword), time.time() - start_time)



	
