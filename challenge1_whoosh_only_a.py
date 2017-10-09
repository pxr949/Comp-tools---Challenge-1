
"""
Course: Computational tools in big data
Exercise: Challenge 1
Date: October 2017

About: Create whoosh index on wikipedia articles where title starts with "a"
"""
                       
                        
""" Importing packages """

import whoosh
from whoosh import qparser
from whoosh.fields import Schema, TEXT

import os.path
from whoosh.index import create_in

from whoosh.qparser import QueryParser


""" Setting up whoosh """

#ana = whoosh.analysis.NgramTokenizer(10)
#schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True, analyzer = ana))
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

writer = ix.writer()
title_no = 1

wiki = open("wiki_a.txt", "r")

for line in wiki:
    writer.add_document(title=str(title_no), content=line)
    title_no = title_no +1
writer.commit()


""" search test """

query = QueryParser("content", ix.schema).parse('alabama press')
results = ix.searcher().search(query, terms=True)

for hit in results:
    print(hit.matched_terms())
    
    
# seeting up search for regular expressions
def regex_maker(node):
    if node.has_text:
        node = qparser.RegexPlugin.RegexNode(node.text)
        node.set_fieldname("content")
        return node
    

import whoosh.qparser as qparser
qp = qparser.QueryParser("content",ix.schema)
qp.add_plugin(qparser.PseudoFieldPlugin({"regex": regex_maker}))

q = qp.parse('regex:ala.{0,2}ma')  

results = ix.searcher().search(q, terms = True, limit = None)
for hit in results:
   print(hit.matched_terms())
    
    
import re

""""""""""""""""""""""""""""""""
""" Insert your pattern here """

input = 'cat[0,2]hat'

""""""""""""""""""""""""""""""""
input = 'cat[0,2]hat'
pattern = input.replace('[', '.{').replace(']', '}')
regex = re.compile(pattern)

"pattern = 'cat.{0,2}hat'"
print(pattern)

wiki = open("wiki.txt", "r")
regex = re.compile(pattern)
words = set({})

for line in wiki:
    result = regex.findall(line)
    "for entry in result:"
    "    print(entry)"
    words = words.union(set(result))
print(words)

""""""""""""""""""""""""""""""""













  

       


                

        

        





