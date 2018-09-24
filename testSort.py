'''
Created on Mar 17, 2018


sort modual retrived from: https://github.com/TheAlgorithms/Python
'''
import random

from sort import insertion_sort, merge_sort, bubble_sort, quick_sort,bucket_sort
 
random_items = [random.randint(-50, 100) for c in range(32)]
 
print ('Before: ', random_items)
#insertion_sort.insertion_sort(random_items)
#heap_sort.heap_sort(random_items)
#merge_sort.merge_sort(random_items)
#bubble_sort.bubble_sort(random_items)
arrayForQuick = bucket_sort.bucketSort(random_items, bucketSize=len(random_items))

 
print ('After : ', arrayForQuick)
 
