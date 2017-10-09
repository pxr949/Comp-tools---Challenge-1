
"""
Course: Computational tools in big data
Exercise: Challenge 1
Date: October 2017

About: Two step function to search wikipedia
"""


""" Importing packages """

import whoosh
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

import linecache
import re
from datetime import datetime


""" Loading indix """

ix = open_dir('index_a')


""" Define search function """

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


def search_whoosh_text(file, pattern):

    startTime = datetime.now()

    a_b =re.compile(r', \([0-9]+, [0-9]+\), ')
    pattern2 = str.replace(str(pattern), "[", "").replace("]","")
    pattern2 = pattern2.replace("'", "*")
    pattern2 = a_b.sub(" ", pattern2)

    query = QueryParser("content", ix.schema).parse(pattern2)
    results = ix.searcher().search(query, terms=True, limit = None)

    line_no = []
    line_no = [(hit["title"]) for hit in results]

    words = set({})

    for i in line_no:
        search_str = linecache.getline(file, int(i))
        result = get_all_matches(search_str, pattern)
        words = words.union(set([search_str[m[0]:m[1]] for m in result]))
    
    endTime = datetime.now()
    runTime = endTime - startTime
 
    result_file = file+str(pattern)+'.txt'
    open(result_file, 'w').close()
    #writing results to file
    for word in words:
        with open(result_file, "a") as wiki_file:
            wiki_file.write(word+'\n')
    with open(result_file, "a") as wiki_file:
        wiki_file.write('runtime: '+str(runTime))
        
        
""" Try a search for the specified patterns """
        
pattern = ['arnold', (0,10), 'schwarzenegger', (0,10), 'is']
file = 'wiki_a.txt'

search_whoosh_text(file, pattern)

pattern = ['apache', (0, 100), 'software']
file = 'wiki_a.txt'

search_whoosh_text(file, pattern)

pattern = ['aarhus', (30, 150), 'denmark']
file = 'wiki_a.txt'

search_whoosh_text(file, pattern)

pattern = ['english', (0, 100), 'alphabet']
file = 'wiki_a.txt'

search_whoosh_text(file, pattern)

pattern = ['first', (0, 85), 'letter', (0, 100), 'alphabet', (0, 200), 'consonant']
file = 'wiki_a.txt'

search_whoosh_text(file, pattern)


""" Try a search for a very general pattern """

pattern = ['a', (0, 100), 'e']
file = 'wiki_a.txt'

search_whoosh_text(file, pattern)
        
