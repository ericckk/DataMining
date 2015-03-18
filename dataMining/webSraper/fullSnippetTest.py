from __future__ import division
import fullSnippet


linkFile = "../google/output/outputNewlinks.txt"
snippetFile = "../google/output/outputNew.txt"

f = open(linkFile)
links = f.readlines()
f.close()


f = open(snippetFile)
snippets = f.readlines()
f.close()

'''
 #for development used to iscolate links 
j=13
print "opening this link "+ (links[j])[6:]
print "Searching for this snippet:- "+ (snippets[j])[6:]		
snippet_full=fullSnippet.run((snippets [j])[9:], (links[j])[6:])
'''
def test():
	i = 0
	fail = 0
	while (i<len(links)-1):
		print "----------------------------------------"
		print "link id = "+str(i)
		print "Opening this link "+ (links[i])[6:]
		print "Searching for this snippet:- "+ (snippets[i])[6:]
		
		snippet_full=fullSnippet.run((snippets [i])[9:], (links[i])[6:])
		if (len(snippet_full)> len((snippets [i])[9:])):
			print "Found the snippet "+ ((snippets [i])[9:]) + " within: "+snippet_full
		else:
			print "Unable to find Full Snippet ***"
			fail +=1	
		i +=1
	print "-------------------------"
	print "Statistics: \nAttempts ="+ str(i) + "\nFails =" + str(fail)
	ratio= float(fail/i)
	print "The percentage of failed attempts = "+ "{:.0%}".format(ratio)
	print "The percentage of successful attempts = "+ "{:.0%}".format(float(1 - ratio))
test()

