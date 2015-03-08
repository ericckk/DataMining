'''
Created on Oct 23, 2014

@author: Cory
@author: Matt
'''

import urllib2
import urllib
import pprint
import nltk
import re
from apiclient.discovery import build

def processText(file, jobQuery):
    f = open(file, 'r')
    text = f.read()
    
    text = text.replace("\\n", "")
    #text = text.replace("\\xa0", "")
    #text = text.replace("\\u201c", "")
    #text = text.replace("\\u201d", "")
    #text = text.replace("u'", "")
    
    #text = re.sub("\\n$", "", text)
    #text = re.sub("\\xa0$", "", text)
    #text = re.sub("\\u201c$", "", text)
    #text = re.sub("\\u201d$", "", text)
    #text = re.sub("u'$", "", text)
    
    #print(text)
    tokens = nltk.sent_tokenize(text)
    tokens = [nltk.word_tokenize(sentence) for sentence in tokens]
    tokens = [nltk.pos_tag(word) for word in tokens]
    #print tokens
    #list: {(<NN|JJ|VB|IN|VBG>+<,>)+(<CC><NN|JJ|VB|IN|VBG>+)*}
    '''grammar = """
            comma: {<NN|JJ|VB|IN|VBG>+<,>}
            endlist: {<CC>(<NN|JJ|VB|IN|VBG>+)}
            list: {<comma>+(<endlist>)}
            
            
            
            """'''
    grammar = """
            list: {(<NN|NNS|NNP|VB|VBG|JJ|CC|PRP|IN|TO>+<,>)+}
            and: {<NN|NNS|JJ|VB|IN|VBG>*<CC><NN|NNS|JJ|VB|IN|VBG>+}
            """
            
    #grammar = "and: {(<NN|NNS|JJ|VB|IN|VBG>+<,>)+<NN|NNS|JJ|VB|IN|VBG>*<CC><NN|NNS|JJ|VB|IN|VBG>+}"
    cp = nltk.RegexpParser(grammar)
    
    for sentence in tokens:
        #break
        result = cp.parse(sentence)
        
        for node in result:
                    
            name = list(" ")
            counter = 0
            if type(node) is nltk.Tree:
                if node.label() == 'list':
                    #print node
                    #break
                    for element in node:
                        #print element[0]
                        if element[1] == ",":
                            counter = counter + 1
                            name.append("")
                            continue
                        if element[1] == "CC":
                            counter = counter + 1
                            name.append("")
                            continue
                        else:
                            if element[0] == "jobs" or element[0] == "professionals" or element[0] == "occupations"or element[0] == "as"or element[0] == "including"or element[0] == "like":
                                name[counter] = ""
                            else:
                                name[counter] = name[counter] + element[0] + " " + "(" + element[1] + ")" + " "
                              
                
                elif node.label() == 'and':
                    for element in node:
                        if element[1] == "CC":
                            counter = counter + 1
                            name.append("")
                            continue
                        else:
                            if element[0] == "jobs" or element[0] == "professionals" or element[0] == "occupations"or element[0] == "as"or element[0] == "including"or element[0] == "like":
                                name[counter] = ""
                            else:
                                name[counter] = name[counter] + element[0] + " " + "(" + element[1] + ")" + " "
                    
                                
            if len(name) == 1:
                if name[0] == " " or name[0] == "":
                    continue
            if len(name) == 2:
                if name[0] == "" and name[1] == "":
                    continue
            print name
            
''' END OF processText() FUNCTION '''

#nltk.download('all')


query = " "

processText("output/outputNew.txt", query)

#print(jobs)



        
        





