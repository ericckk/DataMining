import urllib2
import urllib
from apiclient.discovery import build
from webScraper import fullSnippet
import re


def getSnippets(response, output, links, getFullSnippet):

    #iterate through the keys in the query response (dictionary)
    snippetCounter = 0
    linkCounter = 0
    for key in response.keys():
        #items key holds the link information
        if key == "items":
            #iterate over the items dictionary
            for itemValue in response[key]:
                #iterate over the keys in that dictionary
                for itemKey in itemValue.keys():
                    #print snippet
                    if itemKey == "snippet":
			if(getFullSnippet == False):
		                output.write("Snippet: ")
		                output.write(repr(itemValue[itemKey]))
		                output.write("\n")
			else:
				snippet = repr(itemValue[itemKey])
                        snippetCounter += 1 #counter for snippets founds
                    #print if it is a link
                    elif itemKey == "link":
			linkCounter +=1 #counter for links returned		        
			links.write("Link: ")
		        links.write(itemValue[itemKey])
		        links.write("\n")
			#if get fullSnippet is activated and the link counter mathches the Snippet counter
			if(getFullSnippet == True and linkCounter == snippetCounter):
				snippet_full = fullSnippet.run(snippet, itemValue[itemKey], 2)
				output.write("Snippet: ")
		                try:
					
					#parsing the snippet to try an remove as much niose initially as posible
					
					'''
					snippet_full=re.sub('\\t', '-', snippet_full)
					snippet_full=re.sub('\\r', '-', snippet_full)			
					snippet_full=re.sub('\\n', '-', snippet_full)		
					regex = re.compile('[^a-zA-Z\s,]')
					snippet_full=regex.sub(' ', snippet_full)
					#snippet_full=re.sub('\_\_+', '_', snippet_full)
					'''
					snippetArray= snippet_full.split()
					snippet_full = ' '.join(snippetArray)					
					regex = re.compile('[^a-zA-Z\s,\']')
					snippet_full=regex.sub('.', snippet_full)
					snippet_full=re.sub('\.\.+', '.', snippet_full)
					#writing new snippet					
					snippet_full=repr(snippet_full)
					output.write(snippet_full)	
				except (UnicodeEncodeError, AttributeError) as e:
					#write oriinal Snippet upon error
		                	output.write(repr(snippet))
				output.write("\n")
			
				
    print("Amount of responses " + str(snippetCounter))
    
''' END OF getSnippets() FUNCTION '''
    
api_key = "AIzaSyCHwlWEjEcdeH1KRnmIi9fq5Dnx2JBeVRw"
search_Engine_ID = "016745198537660285174:espiwqmbexg"

domain = "Information Technology"
jobSynonym = ["jobs", "occupations", "professions"]
form = ["such as", "including", "like"]

counter = 0;
query = "\"* Jobs such as Software Engineer\""

blacklist = ["\"* Information Technology occupations including\"", "\"* Information Technology occupations like\"",
             "\"* Information Technology professions such as\"", "\"* Information Technology professions including\"",
             "\"* Information Technology professions like\""]

blacklist2 = [("occupations", "including"), ("occupations", "like"), ("professions", "like")]
    
outputName = "outputNew"
output = open(("output/" + outputName + ".txt"), 'w+')
links = open(("output/" + outputName + "links.txt"), 'w+')

#this activates the full Snippet Capability
getFullSnippet = False
if(getFullSnippet ==  True):
	output = open(("output/" + outputName + "Full.txt"), 'w+')

doSkills = False
    
if not doSkills:
    for js in jobSynonym:
        for fm in form:
            badQuery = False
            for tuple in blacklist2:
                if js == tuple[0] and fm == tuple[1]:
                    badQuery = True
                
            if badQuery:
                continue
                
            query = "\"* " + js + " " + fm + " software engineer" +"\""
                
            if query in blacklist:
                continue
                
            print "Query is: " + query
        
        
            service = build("customsearch", "v1", developerKey=api_key)
        
            #file that will hold the output
            #will create the file if it does not exist (w+)
            counter = counter + 1
        
            response = service.cse().list(q = query, cx = search_Engine_ID).execute()
                
            getSnippets(response, output, links, getFullSnippet)
            #pprint.pprint(response, output)
                   
if doSkills:
    
    jobTitle = "software engineer"
    
    #TODO generate from jobTitle
    queryTitle = "software engineering"
    
    outputName = jobTitle.replace(" ", "")
    output = open(("output/" + outputName + "Skills.txt"), 'w+')
    links = open(("output/" + outputName + "links.txt"), 'w+')
    
    for fm in form:
        if fm == "like":
            continue
        
        query = "\"" + queryTitle + " skills " + fm + "\"" 
        
        print "Query is: " + query
        
        
        service = build("customsearch", "v1", developerKey=api_key)
        
        #file that will hold the output
        #will create the file if it does not exist (w+)
        counter = counter + 1
        
        response = service.cse().list(q = query, cx = search_Engine_ID).execute()
                
        getSnippets(response, output, links, getFullSnippet)
        #pprint.pprint(response, output)       
        
