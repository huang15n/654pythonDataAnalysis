'''
Created on Mar 17, 2018

boyer_moore.py retrieved from: https://gist.github.com/mengzhuo/d713cb8be6c871995b79
kmp.py retrieved from: http://code.activestate.com/recipes/117214-knuth-morris-pratt-string-matching/
'''

from search import boyer_moore, kmp


target = "trusthardtoothbrushestoothgood"
pattern = "oo"

value=boyer_moore.boyer_moore(pattern, target)
value2=kmp.KnuthMorrisPratt(target,pattern)

print("total found words:",pattern,"has value ",value)
print("total found words:",pattern,"has value ",value2)