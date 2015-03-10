#@author - Eric Kingori
#this program will extract a full snippet from link given the snippet and link

from __future__ import division
import os
import tagScraper
import re
import os.path  
import nltk, re, pprint
from bs4 import BeautifulSoup
from nltk import word_tokenize

#This method parses the snippet and opens the text from the link and returns the raw data

def run(snippet, link):
	print "Parsing snippet.."
	snippet = snippet.replace('\\n', '\n')
	#snippet = unicode(snippet, errors = 'ignore')
	p=re.compile('(u\'| u")')
	snippet = p.sub("", snippet)	
	snippet = snippet.replace("... ", "\n")
	
	snippetLines = re.split('\n', snippet)
	
	filename = 'output/scrapedData.txt'
	print "Accesing website for data..."
	if ".pdf" in link:
		print "Cannot extract from PDFs"
	else:
		read= tagScraper.remote(link, filename, False )
	try:
		read = read.decode('utf8')
	except Exception, e:
		print ("unable to extract data from website")
		return snippet
		
	'''
	tagScraper.remote(link, filename, True )
	f = open (filename)
	read = f.read().decode('utf8')
	
												
	f.close()
	'''
	return getSentences(read, snippetLines, snippet)


#this method takes in the raw data and for every sentence it conpares it with the snippets to if snippets is contained it returns teh full sentence 
def getSentences(read,snippetLines, snippet):
	try:    
		print "Looking for full snippet within sentences of the data returned.."
               	found = False;
                sent_detector= nltk.data.load('tokenizers/punkt/english.pickle')
		
                sentences = sent_detector.tokenize(read.strip())
		for sentence in sentences:
				for line in snippetLines:
					if (len(line)>3):
						if line in sentence:
							found= True
							return sentence  
		if(found == False):
			print "Unable to detect snippet using sentences switching to word comparisons.."
			i=0
			read = re.split("\n", read)
			for line in read:
				words = re.split(" ", line)
				words_Snippet = re.split(" ", snippetLines[i])
				j=0				
				for word in words_Snippet:
					if word in words:
						j+=1
				if (j>5):
					found = True
					return line
		if (found == False):
			# going to add more algorithms to deal with different types of sites and noise to reduce the failure percentage			
			return snippet			
											
				 
				
	except Exception, e:
		print (str(e))



#if running from another class comment out snippet = and link =
snippet = u'Find IT - Software jobs such as software engineer/programmer, functional \nconsultant/business analyst, system analyst and others in Singapore. View all IT\n\xa0...'
link = "http://job-search.jobstreet.com.sg/singapore/browse/computer-software-it-jobs/"

#run (snippet, link)


