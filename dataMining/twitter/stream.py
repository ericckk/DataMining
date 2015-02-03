import tweepy, json, sys, pickle
from hireGround.settings import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
from dataMining.twitter.tweet import Tweet






class StdOutListener(tweepy.StreamListener):
    
    def __init__(self, filehandle):
        self._filehandle = filehandle    
    
    def on_data(self, data):
        decoded = json.loads(data)
       
        text = decoded['text'].encode('ascii', 'ignore')
        name = decoded['user']['name'].encode('ascii', 'ignore')
        screenName = decoded['user']['screen_name'].encode('ascii', 'ignore')
        hashtag = decoded['entities']['hashtags']
        location = decoded['user']['location'].encode('ascii', 'ignore')
        tweet = Tweet(text, name, screenName, hashtag, location)
        #self.pickleTweet(tweet)
        print(tweet)
        return True
          
    def pickleTweet(self, data):
        pickle.dump(data, self._filehandle)

    def on_error(self, status):
        print status
        
class Stream(object):
    
    def __init__(self, listener, query):
        self._auth = self._getToken() 
        self._listener = listener
        self._query = query
        self._stream = self._initialize()   

    def _getToken(self):
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)       
        return auth
    
    def _initialize(self):
        stream = tweepy.Stream(self._auth, self._listener)
        stream = stream.filter(track=[self._query]) 
        return stream   

if __name__ == '__main__':

    textfile = 'test.txt'
    query = "#jobs"
    listener = StdOutListener(textfile)
    
    print "initializing query: ..."
    print (textfile)
    print(query)
    twitterHandle = Stream(listener, query)
    
    
    