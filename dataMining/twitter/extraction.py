__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"


#------------------------------------------------------------------------------

from dataMining.settings import STANFORD_NER, STANFORD_NER_JAR, TWITTER_REGEX, TWITTER_CUSTOM_STOPWORDS, TWITTER_CUSTOM_PHRASES_LEFT, TWITTER_CUSTOM_PHRASES_RIGHT,\
    TWITTER_LOCATIONS
from dataMining.twitter.tweet import Tweet

import re

from textblob import TextBlob, Word
from textblob.wordnet import Synset

import nltk
from nltk.corpus import stopwords
from nltk.tag.stanford import NERTagger
from nltk.corpus.reader import TaggedCorpusReader

#------------------------------------------------------------------------------
    
    
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
    #englishStops = stopwords.words('english')
    #customStops = stopwords.words(TWITTER_CUSTOM_STOPWORDS)
    #combinedStops = set(englishStops).union(set(customStops))
    #capitaldStops = [word.title() for word in combinedStops]
    #combinedStops = set(capitaldStops).union(set(combinedStops))
    #return combinedStops

    customStops = stopwords.words(TWITTER_CUSTOM_STOPWORDS)
    capitaldStops = [word.title() for word in customStops]
    combinedStops = set(capitaldStops).union(set(customStops))
    return combinedStops


def cleaner(tweet, stopWords):
    words = tweet.split()
    cleanedData = [word for word in words if word not in stopWords]
    cleanedData = " ".join(cleanedData)
    return cleanedData

#------------------------------------------------------------------------------

def regex_removal(tweet):
    text = tweet.text
    for expression in TWITTER_REGEX:
        text = re.sub(expression, "", text).strip()   
    return text
 
def phraseLeft(tweet):
    text = tweet.text
    for phrase in TWITTER_CUSTOM_PHRASES_LEFT:
        index = text.find(phrase)
        if index != -1:
            index = index + len(phrase)
            text = (text[index:])
    return text

def phraseRight(tweet):
    text = tweet.text
    for phrase in TWITTER_CUSTOM_PHRASES_RIGHT:
        index = text.find(phrase)
        if index != -1:
            text = (text[:index])
    return text
    
def tags(tweet): 
    tweetTags = TextBlob(tweet).tags
    nounList = [pos[0] for pos in tweetTags if pos[1][0] == 'N']
    return ' '.join(nounList) 

def nltkTags(tweet):
    text = nltk.word_tokenize(tweet)
    tags = nltk.pos_tag(text)
    return [pos[1] for pos in tags]

# doesnt work - causes changes correctly spelled words    
def spellcheck(tweet):
    return TextBlob(tweet).correct()


#------------------------------------------------------------------------------
# runner



def runner(tweet):   
    if type(tweet) != Tweet:
        pass
    else: 

        cleanTweet = tweet
        cleanTweet.text = phraseLeft(cleanTweet)
        cleanTweet.text = phraseRight(cleanTweet)
        cleanTweet.text = regex_removal(cleanTweet)
        text = cleanTweet.text
        
        # ner - organization, location, person
        nerList = stanfordContext(text)       
        text = cleaner(text, nerList)
        # stopwords
        text = cleaner(text, stopWords(text))
        # metadata
        text = cleaner(text, tweet.metaData())

        return text.strip()

    
if __name__ == "__main__":
    print('intitializing...')
    t = Tweet(text="RT @jobz4it: #jobs4u #jobs Information Technology (IT) Solutions Analyst, Washington, DC http://t.co/z0OVXm1xFC #infotech")
    print(runner(t))
