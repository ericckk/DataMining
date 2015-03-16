
#! /usr/bin/env python

__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"


import pickle, nltk
from dataMining.twitter import extraction

pickledTweets = 'twitter_cursor_output.p'
cleanTweets = 'results.txt'

def pickleLoader(pklFile):
    try:
        while True:
            yield pickle.load(pklFile)
    except EOFError:
        pass


def readPickleFile(filename):
    tweets = []
    with open(filename) as f:
        for tweet in pickleLoader(f):
            tweets.append(tweet)
    return tweets

def readTextFile(filename):
    textfile = open(filename, 'r')
    textfileList = textfile.readlines()
    textfile.close()
    return textfileList
    
def tester():
    tweetList = readPickleFile(pickledTweets)
    resultList = readTextFile(cleanTweets)

    count1 = 0
    count2 = 0
    precision = 0
    
    for tweet, result in zip(tweetList, resultList):
       
        count1 = count1 +1
        print(tweet)
        extract = extraction.runner(tweet)
        
        extractTokens = nltk.word_tokenize(extract)
        resultTokens = nltk.word_tokenize(result)
        
        precisionList = [word for word in resultTokens if word in extractTokens]
        if len(precisionList) == len(resultTokens):
            precision = precision + 1
        
        print('Exrt: ' + extract)
        print('Cort: ' + result)

        
        if (extract.strip() == result.strip()):
            count2 = count2 +1
            
    print('Precision: ' + str(precision) + ' out of ' + str(count1) + ' or ' + str(float("{0:.2f}".format(precision/float(count1)))) + '% of retrieved instances are relevant (positive predictive value)')
    print('Recall: ' + str(count2) +' out of ' + str(precision) + ' or ' + str(float("{0:.2f}".format(count2/float(precision)))) + '% of the relevant instances are retrieved (sensitivity)')
    
if __name__ == '__main__':
    tester()

