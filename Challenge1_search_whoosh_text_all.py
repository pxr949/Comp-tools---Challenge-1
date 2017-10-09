
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

ix = open_dir('index_all')


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
        
pattern = ['elephants', (0, 20), 'are', (0, 20), 'to']
file = 'wiki.txt'

search_whoosh_text(file, pattern)

pattern = ['technical', (0, 20), 'university', (0, 20), 'denmark']
file = 'wiki.txt'

search_whoosh_text(file, pattern)

pattern = ['testing', (0, 20), 'with', (0, 20), 'a', (0, 30), 'lot', (0, 4), 'of', (0, 5), 'words']
file = 'wiki.txt'

search_whoosh_text(file, pattern)

pattern = ['stress', (0, 250), 'test']
file = 'wiki.txt'

search_whoosh_text(file, pattern)

pattern = ['object', (10, 200), 'application', (0, 100), 'python', (10, 200), 'system', (0, 100), 'computer', (0, 10), 'science', (0, 150), 'linux', (0, 200), 'ruby']
file = 'wiki.txt'

search_whoosh_text(file, pattern)


        
