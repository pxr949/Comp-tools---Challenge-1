# -*- coding: utf-8 -*-
"""
Search wiki articles with brute force
"""
                        
""" **************** """                        
""" Read in packages """
""" **************** """ 

import re
from datetime import datetime
    
    
""" ********************************* """                        
""" Function to search the file       """
""" ********************************* """

def get_matches_starting_at(data, pattern, index, starting_index, resulting_matches):
	sub_data = data[index:]

	P = pattern[0]
	if sub_data[:len(P)] == P:
		if len(pattern) == 1:
			resulting_matches.append((starting_index,index+len(P)))
		else:
			for new_index in range(pattern[1][0]+1, pattern[1][1]+2):
				get_matches_starting_at(data, pattern[2:], index+len(P)+new_index-1, starting_index, resulting_matches)
		
		return resulting_matches
	else:
		return []

def get_all_matches(data, pattern):
	matches_found = []
	for index in range(len(data)):
		matches_at_index = get_matches_starting_at(data, pattern, index, index, [])
		matches_found += matches_at_index
		
	return set(matches_found)   


""" ********************************* """                        
""" Search only cat file              """
""" ********************************* """

""" PATTERN 1 """

startTime = datetime.now()

pattern = ["cat",(0,1),"in",(0,1),"hat"]

wiki = open("wiki_only_cat.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_only_cat_result_1.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_only_cat_result_1.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_only_cat_result_1.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
""" PATTERN 2 """

startTime = datetime.now()

pattern = ["or",(0,10),"or",(0,10),"or"]

wiki = open("wiki_only_cat.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_only_cat_result_2.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_only_cat_result_2.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_only_cat_result_2.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
""" PATTERN 3 """

startTime = datetime.now()

pattern = ["when",(15,25),"republic",(15,25),"along"]

wiki = open("wiki_only_cat.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_only_cat_result_3.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_only_cat_result_3.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_only_cat_result_3.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
    
""" ********************************* """                        
""" Search articles with a in title   """
""" ********************************* """

""" PATTERN 1 """

startTime = datetime.now()

pattern = ["cat",(0,1),"in",(0,1),"hat"]

wiki = open("wiki_a.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_a_result_1.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_a_result_1.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_a_result_1.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
""" PATTERN 2 """

startTime = datetime.now()

pattern = ["or",(0,10),"or",(0,10),"or"]

wiki = open("wiki_a.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_a_result_2.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_a_result_2.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_a_result_2.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
""" PATTERN 3 """

startTime = datetime.now()

pattern = ["when",(15,25),"republic",(15,25),"along"]

wiki = open("wiki_a.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_a_result_3.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_a_result_3.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_a_result_3.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
    
""" ********************************* """                        
""" Search all articles               """
""" ********************************* """

""" PATTERN 1 """

startTime = datetime.now()

pattern = ["cat",(0,1),"in",(0,1),"hat"]

wiki = open("wiki.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_result_1.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_result_1.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_result_1.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
""" PATTERN 2 """

startTime = datetime.now()

pattern = ["or",(0,10),"or",(0,10),"or"]

wiki = open("wiki.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_result_2.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_result_2.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_result_2.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    
""" PATTERN 3 """

startTime = datetime.now()

pattern = ["when",(15,25),"republic",(15,25),"along"]

wiki = open("wiki.txt", "r")
words = set({})

for line in wiki:
    result = get_all_matches(line,pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))
print(words)
    
endTime = datetime.now()
runTime = endTime - startTime
    
open('wiki_result_3.txt', 'w').close()
#writing results to file
for word in words:
    with open("wiki_result_3.txt", "a") as wiki_file:
        wiki_file.write(word+'\n')
with open("wiki_result_3.txt", "a") as wiki_file:
    wiki_file.write('runtime: '+str(runTime))
    






  

       


                

        

        





