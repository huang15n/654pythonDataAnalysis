


def BruteForceMatch(text, pattern ):
	counter = 0
	m = len(pattern)#this is to define the len of the pattern
	n = len(text)#this is to define the length of the text
	for i in range(0, n - m + 1):
		j = 0
		while j in range(m) and (text[i+j] == pattern[j]):
			j += 1	
		if j == m:
			counter += 1
			
	return counter










    