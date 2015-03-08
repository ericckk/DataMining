import urllib2
import urllib
from apiclient.discovery import build

def getSnippets(response, output, links):
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
                    elif itemKey == "link":
                        links.write("Link: ")
                        links.write(itemValue[itemKey])
                        links.write("\n\n")
    print("Amount of responses " + str(counter))
    
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
                
            getSnippets(response, output, links)
            #pprint.pprint(response, output)
                   
if doSkills:
    
    outputName = "SoftwareEngineer"
    output = open(("output/" + outputName + ".txt"), 'w+')
    links = open(("output/" + outputName + "links.txt"), 'w+')
    
    for fm in form:
        query = " "
        
        print "Query is: " + query
        
        
        service = build("customsearch", "v1", developerKey=api_key)
        
        #file that will hold the output
        #will create the file if it does not exist (w+)
        counter = counter + 1
        
        response = service.cse().list(q = query, cx = search_Engine_ID).execute()
                
        getSnippets(response, output, links)
        #pprint.pprint(response, output)       
        