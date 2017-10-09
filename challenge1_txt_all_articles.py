
# Parse wikipedia articles and store in a text file

                        
""" **************** """                        
""" Read in packages """
""" **************** """ 

import xml
import xml.etree.cElementTree as cet
import re


""" ************************ """                        
""" Parse xml to text file   """
""" ************************ """ 

open('wiki.txt', 'w').close()

xmlfile = 'enwiki-20170820-pages-articles.xml'

text_tag = '{http://www.mediawiki.org/xml/export-0.10/}text'

ref =re.compile(r'<ref.*?>.*?</ref>')

for event, elem in cet.iterparse(xmlfile):
    if elem.tag == text_tag:
        if str(elem.text)[0:9] != '#REDIRECT':
            text_str = str(elem.text).encode("ascii", errors="ignore").decode().lower()
            text_str = text_str.replace('\n', " ")
            text_str = ref.sub("", text_str)
            with open("wiki.txt", "a") as wiki_file:
                wiki_file.write(text_str+'\n')
    elem.clear()
 
