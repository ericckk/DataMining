__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tag.stanford import NERTagger
from dataMining.settings import STANFORD_NER, STANFORD_NER_CON11, STANFORD_NER_MUC7, STANFORD_NER_JAR


def stanford(tweet):
    st = NERTagger(STANFORD_NER, STANFORD_NER_JAR) 
    return st.tag(tweet.split())

def stanfordCon11(tweet):
    st = NERTagger(STANFORD_NER_CON11, STANFORD_NER_JAR) 
    return st.tag(tweet.split())

def stanfordMuc7(tweet):
    st = NERTagger(STANFORD_NER_MUC7, STANFORD_NER_JAR)
    return st.tag(tweet.split())
       
def stopwords(tweet):
    words = tweet.split()
    englishStops = set(stopwords.words('english'))
    with open('C:/path/numbers.txt', 'r') as f:
        customStops = f.readlines()
        combinedStops = set(englishStops).union(set(customStops))
        cleanedData = [word for word in words if word not in combinedStops ]
    return " ".join(cleanedData)

def punctuation(tweet):
    return re.sub(r"(-|;|:|\.|,|\(|\)|\|\\|\/)", "", tweet) 
        
def replies(tweet):
    return re.sub(r"@\w*", "", tweet)

def hashtags(tweet):
    return re.sub(r"#\w*", "", tweet) 
    
def hyperlinks(tweet):
    return re.sub(r"http://.*|https://.*", "", tweet)
    
def tags(tweet): 
    return TextBlob(tweet).tags

def stanfordContext(tweet):
    t = stanford(tweet)
    print(t)
    l = []
    for x in t:
        x = t.pop()
        j = x[0].encode('ascii', 'replace')
        k = x[1].encode('ascii', 'replace')
        if k != 'O':
            l.append(j)

    stop = set(l)

    words = tweet.split()
    cleanedData = [word for word in words if word not in stop ]
    cleanedData = " ".join(cleanedData)
    cleanedData = hyperlinks(cleanedData)
    cleanedData = hashtags(cleanedData)
    cleanedData = punctuation(cleanedData)
    
    print(tags(cleanedData.lower()))
        
    print(cleanedData.strip())

 
if __name__ == "__main__":
    pass

           