# -*- coding: utf-8 -*-
"""
Course: Computational tools in big data
Exercise: Challenge 1
Date: October 2017

About: Create whoosh index on all wikipedia articles
"""
                       
                        
""" Importing packages """

import whoosh
from whoosh import qparser
from whoosh.fields import Schema, TEXT

import os.path
from whoosh.index import create_in

from whoosh.qparser import QueryParser

import linecache


""" Setting up whoosh """

#ana = whoosh.analysis.NgramTokenizer(10)
#schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True, analyzer = ana))
schema = Schema(title=TEXT(stored=True), content=TEXT)

if not os.path.exists("index_all"):
    os.mkdir("index_all")
ix = create_in("index_all", schema)

writer = ix.writer()
title_no = 1

wiki = open("wiki.txt", "r")

for line in wiki:
    writer.add_document(title=str(title_no), content=line)
    title_no = title_no +1
writer.commit()


""" search test """

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

query = QueryParser("content", ix.schema).parse('*arnold* *schwarzenegger* *is*')
results = ix.searcher().search(query, terms=True, limit = None)

line_no = []
line_no = [(hit["title"]) for hit in results]

pattern = ['arnold', (0, 10), 'schwarzenegger', (0, 10), 'is']

words = set({})

for i in line_no:
    search_str = linecache.getline('wiki_a.txt', int(i))
    result = get_all_matches(search_str, pattern)
    words = words.union(set([line[m[0]:m[1]] for m in result]))





  

       


                

        

        





