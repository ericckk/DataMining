'''
@author - Eric Kingori
@description  - Given a file of links this program will use the scraper to extract the the 
text from the link then pass the text to mining module that will parse and iscolate potential
relevant information
@limitations - If file structure is changed this code must be updated 
'''
from __future__ import division
import os
import tagScraper
import mining
import re
import os.path  
import nltk, re, pprint
from nltk import word_tokenize

#opens all text files in output directory
def openFiles(outputDir):
	for filename in os.listdir(outputDir):
		if("links" in filename):
			print "extracting links from: " + outputDir + "/"+ filename
			f = open(outputDir + "/"+ filename)
			read = f.readlines()
			output = 'output/data/'
			i=0
			for line in read:
				if (line[:5] == "Link:"):
					if (".pdf" in line):
						print "Cannot scrape through pdfs"
					else:			
						link = line[6:]
						i+=1
						dataset = tagScraper.remote(link,"NULL", False )
						mining.processLanguage(output+str(i)+".txt", dataset)
				
				
									
				
			f.close()

outputDir = "../google/output"
openFiles(outputDir)

