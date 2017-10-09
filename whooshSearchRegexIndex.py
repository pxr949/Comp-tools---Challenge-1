#import re
import whoosh
import whoosh.qparser as qparser

myIndexPath = "C:/Users/kdsv/Tools/challenge1/indexRealDeal2"

#open existing index
ix = whoosh.index.open_dir(myIndexPath)

# seeting up search for regular expressions

def regex_maker(node):
    if node.has_text:
        node = qparser.RegexPlugin.RegexNode(node.text)
        node.set_fieldname("content")
        return node
  
qp = qparser.QueryParser("content", ix.schema)
qp.add_plugin(qparser.PseudoFieldPlugin({"regex": regex_maker}))

q = qp.parse("regex:.*ala.{0,3}a")

results = ix.searcher().search(q, terms = True, limit = None)


allMatches = set()

for hit in results:
    a = hit.matched_terms()
    for i in range(0,len(a)-1):
        b = str(a[i][1]).replace("b'", "").replace("'","")
#        print(b)
        allMatches.add(b)

print(allMatches)