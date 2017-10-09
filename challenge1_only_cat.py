
# Parse wikipedia cat article and store in a text file

                        
""" **************** """                        
""" Read in packages """
""" **************** """ 

import re


""" ************************ """                        
""" Parse xml to text file   """
""" ************************ """ 

open('wiki_only_cat.txt', 'w').close()

ref =re.compile(r'<ref.*?>.*?</ref>')

with open('wiki_only_cat_raw.txt', 'r') as input_file:
    text_str=input_file.read().replace('\n', ' ')

text_str = text_str.encode("ascii", errors="ignore").decode().lower()
text_str = ref.sub("", text_str)
with open("wiki_only_cat.txt", "a") as wiki_file:
    wiki_file.write(text_str)
 
