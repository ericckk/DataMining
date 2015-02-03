import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tag.stanford import NERTagger
from dataMining.settings import STANFORD_NER, STANFORD_NER_CON11, STANFORD_NER_MUC7, STANFORD_NER_JAR





#---------------------------------------------------------------------------------- 
def stanford1(tweet):
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
 
if __name__ == "__main__":
    t = "#California #Jobs Project Manager, Information Technology: Los Angeles Cloudtrend Inc. Specializes in building... http://t.co/t6MtQpQmyx"
    #e = Extractor()
    data1 = stanford1(t)
    print(data1)
    data2 = stanfordCon11(t)
    print(data2)
    data3 = stanfordMuc7(t)
    print(data3)    
           