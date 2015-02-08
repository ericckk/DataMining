'''
Created on Oct 23, 2014

@author: Cory
@author: Matt
'''

import urllib2
import urllib
import pprint
import nltk
from apiclient.discovery import build

def getSnippets(response, output):
    #iterate through the keys in the query response (dictionary)
    counter = 0
    for key in response.keys():
        #items key holds the link information
        if key == "items":
            #iterate over the items dictionary
            for itemValue in response[key]:
                #iterate over the keys in that dictionary
                for itemKey in itemValue.keys():
                    #print snippet
                    if itemKey == "snippet":
                        output.write("Snippet: ")
                        output.write(repr(itemValue[itemKey]))
                        output.write("\n")
                        counter = counter + 1
                    #print if it is a link
                    '''elif itemKey == "link":
                        output.write("Link: ")
                        output.write(itemValue[itemKey])
                        output.write("\n\n")'''
    print("Amount of responses " + str(counter))


def processText(file, jobQuery):
    f = open(file, 'r')
    text = f.read()
    
    text = text.replace("\\n", " ")
    text = text.replace("\\xa0", "")
    text = text.replace("\\u201c", "")
    text = text.replace("\\u201d", "")
    
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
    grammar = "list: {(<NN|NNS|JJ|VB|IN|VBG>+<,>)+}"
    cp = nltk.RegexpParser(grammar)
    
    for sentence in tokens:
        #break
        result = cp.parse(sentence)
        
        for node in result:
                    
            name = ""
            if type(node) is nltk.Tree:
                if node.label() == 'list':
                    print node
                    break
                    for element in node:
                        #print element[0]
                        if element[1] == "NN":
                            name = name + element[0] + " "
                            
            if name != "":
                print name
    
'''    i = 0
    j = 1
    found = True
    jobs = []
    jobQuery = "jobs such as"
    queryTokens = nltk.word_tokenize(jobQuery)
    queryLength = len(queryTokens)
    #print(queryTokens)
    
    while i < len(tokens):
        found = True
        if tokens[i] == queryTokens[0]:
            
            while (j < queryLength):
                #print(tokens[i+1])
                #print(queryTokens[j])
                if tokens[i+1] == ',':
                    i = i + 1
                    continue
                elif tokens[i+1] != queryTokens[j]:
                    found = False;
                    break
                i = i + 1
                j = j + 1
                
        else:
            found = False
        if found:
            print("Found Query")
            
            #determine if it is a list
            j = i
            phrase = tokens[j]
            while tokens[j] != ".":
                 phrase = phrase + " " + tokens[j]
                 j = j+1
                 
            jobs = phrase.split(",");
            
            for job in jobs:
                job = job.strip()
        i = i+1'''
        
    #return jobs

#nltk.download('all')

query = "jobs such as software engineer"

processText("output/output.txt", query)

#print(jobs)


api_key = "AIzaSyCHwlWEjEcdeH1KRnmIi9fq5Dnx2JBeVRw"
search_Engine_ID = "016745198537660285174:espiwqmbexg"

domain = "Information Technology"
jobSynonym = ["jobs", "occupations", "professions", "professionals"]
form = ["such as", "including", "like"]

counter = 0;
query = "\"* Jobs such as Software Engineer\""

'''
output = open(("output/output.txt"), 'w+')
for js in jobSynonym:
    for fm in form:
        query = "\"* " + domain + " " + js + " " + fm + "\""
        print "Query is: " + query


        service = build("customsearch", "v1", developerKey=api_key)

        #file that will hold the output
        #will create the file if it does not exist (w+)
        counter = counter + 1

        response = service.cse().list(q = query, cx = search_Engine_ID).execute()
        
        getSnippets(response, output)
        #pprint.pprint(response, output)
'''
        
        





