import csv 
from operator import itemgetter
from sort import insertion_sort, merge_sort, heap_sort, quick_sort,bucket_sort,radix_sort
import time 


def readFilesAndSort(filenameToSave,algorithm_choice):
	filename = filenameToSave+'.csv'
	unsorted_csv = open(filename,"r+")
	reader = csv.reader(unsorted_csv)
	data = []
	start_time = time.time()
	unsorted_csv.readline()
	for row in reader:
		data.append([(float)(row[3]),(row[0]),(float)(row[1]),(float)(row[2])])

	if algorithm_choice == 1:
		merge_sort.merge_sort(data)
		end_time = time.time() - start_time
		fieldnames_for_csv = ['item_description', 'item_price', 'item_shipping','total_price']
		sorted_csv_data = open(filename+"_mergesort.csv","w+")
		sorted_data_writer = csv.DictWriter(sorted_csv_data,fieldnames=fieldnames_for_csv)
		sorted_data_writer.writeheader()
		for items in data:
			sorted_data_writer.writerow({'item_description':items[1],'item_price':items[2],'item_shipping':items[3],"total_price":items[0]})
		
		sorted_csv_data.close()
		return end_time

	if algorithm_choice == 2:
		data = quick_sort.quick_sort(data)
		end_time = time.time() - start_time
		fieldnames_for_csv = ['item_description', 'item_price', 'item_shipping','total_price']
		sorted_csv_data = open(filename+"_quicksort.csv","w+")
		sorted_data_writer = csv.DictWriter(sorted_csv_data,fieldnames=fieldnames_for_csv)
		sorted_data_writer.writeheader()
		for items in data:
			sorted_data_writer.writerow({'item_description':items[1],'item_price':items[2],'item_shipping':items[3],"total_price":items[0]})
		sorted_csv_data.close()
		return end_time
	if algorithm_choice == 3:
		heap_sort.heap_sort(data)
		end_time = time.time() - start_time
		fieldnames_for_csv = ['item_description', 'item_price', 'item_shipping','total_price']
		sorted_csv_data = open(filename+"_heapsort.csv","w+")
		sorted_data_writer = csv.DictWriter(sorted_csv_data,fieldnames=fieldnames_for_csv)
		sorted_data_writer.writeheader()
		for items in data:
			sorted_data_writer.writerow({'item_description':items[1],'item_price':items[2],'item_shipping':items[3],"total_price":items[0]})
		sorted_csv_data.close()
		return end_time

	





	
	

