import tweepy, pickle
from hireGround.settings import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
from dataMining.twitter.tweet import Tweet




class Cursor(object):
    def __init__(self, filehandle):
        self._api = self._initialize()
        self._filename = filehandle

    def _initialize(self):
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.secure = True
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)
        
    def page(self, query):    
        tweetCount = 0
        pageCount = 0
        
        for page in tweepy.Cursor(self._api.search, q=query, rpp=100, lang='en').pages(5):
            pageCount +=1
            for tweet in page:
                tweetCount +=1
                text = tweet.text.encode('utf-8')
                name = tweet.author.name.encode('utf8')
                screenName = tweet.author.screen_name.encode('utf8')
                hashtags = tweet.entities.get('hashtags')
                location = tweet.user.location.encode('utf8')
                t = Tweet(text, name, screenName, hashtags, location)
                print(t)
                
            print('page: ' + str(pageCount) + '.....................')
            print('pages: ' + str(pageCount) + ' tweet count: ' + str(tweetCount))

            
if __name__ == "__main__":
    c = Cursor('g')
    c.page('jobs information technology')
    
