from __future__ import division  
import nltk, re, pprint
from nltk import word_tokenize




def processLanguage(filename, dataSet):
	f = open(filename, 'w')

	try:    
               	dataSet = unicode(dataSet, errors = 'ignore')
                sent_detector= nltk.data.load('tokenizers/punkt/english.pickle')
                sentences = sent_detector.tokenize(dataSet.strip())
                #print '\n----------\n'.join(sentences)
                #sentences = nltk.sent_tokenize(dataSet)
                sentences = [nltk.word_tokenize(sent) for sent in sentences]
                sentences = [nltk.pos_tag(sent) for sent in sentences]
                
		print "SW - single word extraction, MW - multiple word extraction"
		for sentence in sentences:
			grammar ="""
				     MW:{<DT>?<JJ.>+<NN.>+}
					{<NN.>+<CC>?<NN.>+}
					{<NN.>+<IN>*<JJ>*<NN.>+}
					{<NN.>+2}
				     SW: {<NN.>}
				"""
				#SW:{<NN.>}
                        parser = nltk.RegexpParser(grammar)
                        result = parser.parse(sentence)
                	result.set_label("NP")
			result.leaves()
			 
			for items in result:
				if "(MW" in str(items):
					f.write(getText(items))
				if "(SW" in str(items):
					f.write(getText(items))	
					
				#items.leaves()
				

                        
	except Exception, e:
		print (str(e))
	f.close()

#this method removes all POS tags and extract the text
def getText(nltk_tree):
	words = str(nltk_tree)
	words = words[3:]
	parse = re.compile('([/]|[)]|NNP|NNS|ADJ|CC|CD|DT|EX|FW|IN|JJ|JJR|JJS|LS|MD|NN|NNPS|PDT|POS|PRP|RB|RBR|RBS|RP|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WDT|WP|WRB)')
	words =parse.sub('', words)	
	print words
	return words

'''
f = open ("../../output/jobskills.txt")
dataSet = f.read().decode('utf8')
f.close()
processLanguage("../../output/jobskillsResults.txt", dataset)
'''



