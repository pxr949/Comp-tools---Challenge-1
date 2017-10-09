
# Parse wikipedia articles with titles starting with "a" and store in a text file
                        
""" **************** """                        
""" Read in packages """
""" **************** """ 

import xml
import xml.etree.cElementTree as cet
import re


""" ************************ """                        
""" Parse xml to text file   """
""" ************************ """ 

open('wiki_a.txt', 'w').close()

xmlfile = 'enwiki-20170820-pages-articles.xml'

textTag = '{http://www.mediawiki.org/xml/export-0.10/}text'
titleTag = '{http://www.mediawiki.org/xml/export-0.10/}title'

countPage = 0

ref =re.compile(r'<ref.*?>.*?</ref>')

for event, elem in cet.iterparse(xmlfile, events=("start", "end")):
    #if elem.tag == 'page' and event == "start":
    #    countPage +=1
    #    """print("currently pasing article " + str(countPage))"""
    #elem.clear()
    if elem.tag == titleTag and event == "start":
        currentPage = countPage
        artTitle = str(elem.text).encode("ascii", errors="ignore").decode().lower()
    #elem.clear()
    if elem.tag == textTag  and event == "end" and len(artTitle) > 0:# and currentPage == countPage and event == "start":
        bodyText = str(elem.text).encode("ascii", errors="ignore").decode().lower().replace('\n', " ")
        if bodyText[0:9] != "#redirect" and artTitle[0] == 'a':
            text_str = str(elem.text).encode("ascii", errors="ignore").decode().lower()
            text_str = text_str.replace('\n', " ")
            text_str = ref.sub("", text_str)
            with open("wiki_a.txt", "a") as wiki_file:
                wiki_file.write(text_str+'\n')
    elem.clear()





