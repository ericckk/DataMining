__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"


#------------------------------------------------------------------------------
# imports


from dataMining.settings import STANFORD_NER, STANFORD_NER_JAR, TWITTER_CUSTOM_STOPWORDS, TWITTER_CUSTOM_PHRASES_LEFT, TWITTER_CUSTOM_PHRASES_RIGHT
from dataMining.twitter.tweet import Tweet

import re

from textblob import TextBlob, Word
from textblob.wordnet import Synset

import nltk
from nltk.corpus import stopwords
from nltk.tag.stanford import NERTagger
from nltk.corpus.reader import TaggedCorpusReader


#------------------------------------------------------------------------------
# functions    
    
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
    customStops = stopwords.words(TWITTER_CUSTOM_STOPWORDS)
    combinedStops = set(englishStops).union(set(customStops))
    capitaldStops = [word.title() for word in combinedStops]
    combinedStops = set(capitaldStops).union(set(combinedStops))
    return combinedStops

def cleaner(tweet, stopWords):
    words = tweet.split()
    cleanedData = [word for word in words if word not in stopWords]
    cleanedData = " ".join(cleanedData)
    return cleanedData

#------------------------------------------------------------------------------
# regex    

# ; : . , |
def punctuation(tweet):
    return re.sub(r"(;|:|\.|,|\|)", "", tweet)
 
# @username        
def username(tweet):
    return re.sub(r"@\w*", "", tweet)

def hashtags(tweet):
    return re.sub(r"#\w*", "", tweet) 
    
def hyperlinks(tweet):
    return re.sub(r"http://.*|https://.*", "", tweet)

# () [] remove brackets leave text
def brackets(tweet):
    return re.sub(r"(\(|\)|\[|\])", "", tweet) 

# remove everything within brackets
def bracketText(tweet):
    tweet = re.sub(r'\[(.+?)\]', "", tweet)
    return re.sub(r'\([^)]*\)', "", tweet)

# - / \
def dashSlash(tweet):
    return re.sub(r"(-|\/|\\)", " ", tweet)

def cutoff(tweet):
    return re.sub(r"\w*\.{3}", "", tweet)

def phraseLeft(tweet):
    text = tweet
    for phrase in TWITTER_CUSTOM_PHRASES_LEFT:
        index = text.find(phrase)
        if index != -1:
            index = index + len(phrase)
            text = (text[index:])
    return text

def phraseRight(tweet):
    text = tweet
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

def metaData(tweet):
    text = tweet.text
    return tweet.metaData()

def runner(tweet):   
    if type(tweet) != Tweet:
        pass
    else: 
        metaDataList = metaData(tweet)
        text = tweet.text
        
        text = phraseLeft(text)
        text = phraseRight(text)
        text = cutoff(text)
        
        # regex removal
        text = hyperlinks(text)
        text = hashtags(text) 
        text = username(text)   
        text = bracketText(text)

        # ner - organization, location, person
        nerList = stanfordContext(tweet.text)
        text = punctuation(text)        
        text = cleaner(text, nerList)
        # stopwords
        text = cleaner(text, stopWords(tweet.text))
        # metadata
        text = cleaner(text, metaDataList)
        
        #text = dashSlash(text)
        #text = tags(text)
        #text = spellcheck(text)
        
        tb = TextBlob(text)
        words = tb.words
        test = ' '.join(words)
        
        return test

    
    
#------------------------------------------------------------------------------
# experimental

def similarity(word1, word2):
    word = Word(word1).get_synsets()
    word2 = Word(word2).get_synsets()   
    return word[0].path_similarity(word2[0])
    

#------------------------------------------------------------------------------
# local
     
if __name__ == "__main__":
    pass
