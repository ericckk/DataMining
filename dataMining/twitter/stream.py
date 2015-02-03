import tweepy, json, pickle
from dataMining.settings import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
from dataMining.twitter.tweet import Tweet


class StdOutListener(tweepy.StreamListener):
    
    def __init__(self, filehandle):
        self._filehandle = filehandle    
    
    def on_data(self, data):
        decoded = json.loads(data)
       
        #.encode('ascii', 'ignore')
       
        text = decoded['text']
        name = decoded['user']['name']
        screenName = decoded['user']['screen_name']
        description = decoded['user']['description']
        hashtags = decoded['entities']['hashtags']
        location = decoded['user']['location']
        tweet = Tweet(text, name, screenName, description, hashtags, location)
        
        print(tweet)
        '''
        print(type(text.encode('ascii', 'replace')))
        print(type(name.encode('ascii', 'replace')))
        print(type(screenName.encode('ascii', 'replace')))
        if description is not None:
            print(type(description.encode('ascii', 'replace')))
        print(hashtags)
        if location is not None:
            print(type(location.encode('ascii', 'replace')))
        print('\n')
        '''
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
    
    
    