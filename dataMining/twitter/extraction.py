__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tag.stanford import NERTagger
from dataMining.settings import STANFORD_NER, STANFORD_NER_JAR, TWITTER_CUSTOM_STOPWORDS


def stanford(tweet):
    st = NERTagger(STANFORD_NER, STANFORD_NER_JAR) 
    return st.tag(tweet.split())

def stanfordContext(tweet):
    t = stanford(tweet)

    nerList = []
    for x in t:
        x = t.pop()
        j = x[0].encode('ascii', 'replace')
        k = x[1].encode('ascii', 'replace')
        if k != 'O':
            nerList.append(j)
    return set(nerList)
       
def stopWords(tweet):
    englishStops = stopwords.words('english')
    
    stopWordsFile = open(TWITTER_CUSTOM_STOPWORDS, 'r')
    customStops = []
    for stopWord in stopWordsFile:
        customStops.append(stopWord.rstrip('\n'))
        customStops.append(stopWord.rstrip('\n').title())
    
    return set(englishStops).union(set(customStops))

def cleaner(tweet, stopWords):
    words = tweet.split()
    cleanedData = [word for word in words if word not in stopWords]
    cleanedData = " ".join(cleanedData)
    return cleanedData

def punctuation(tweet):
    return re.sub(r"(-|;|:|\.|,|\(|\)|\|\\|\/|\|)", "", tweet) 
        
def replies(tweet):
    return re.sub(r"@\w*", "", tweet)

def hashtags(tweet):
    return re.sub(r"#\w*", "", tweet) 
    
def hyperlinks(tweet):
    return re.sub(r"http://.*|https://.*", "", tweet)
    
def tags(tweet): 
    tweetTags = TextBlob(tweet).tags
    nounList = [pos[0] for pos in tweetTags if pos[1][0] == 'N']
    return ' '.join(nounList) 


def runner(tweet):    
    clean = hyperlinks(t)
    clean = punctuation(clean)
    clean = cleaner(clean, stanfordContext(t))
    clean = cleaner(clean, stopWords(t))
    clean = tags(clean)
    clean = replies(clean)
    return clean
 
if __name__ == "__main__":
    t = "Now Hiring: is at Information Technology Teaching Assistant | Year Up Chicago: US - IL - Chicago | http://t.co/j1Y3KF5d48 #jobs"
    clean = runner(t)
    print(t)
    print(clean)
           