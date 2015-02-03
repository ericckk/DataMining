

class Tweet(object):
    def __init__(self, text, name=None, screenName=None, hashtags=None, location=None):
        self._text = text.decode('ascii', 'ignore').lower()
        self._name = name.decode('ascii', 'ignore').lower() 
        self._screenName = screenName.decode('ascii', 'ignore').lower()
        self._hashtags, self.hashtagIndex = self._hashtagSplit(hashtags)
        self._location = location.decode('ascii', 'ignore').lower()
        
    def __repr__(self):
        strRep = self._text + '\n' + self._name + '\n' + self._screenName + '\n' + self._location + '\n'
        strRep += ' '.join(self._hashtags) + '\n' + '\n'
        return strRep
    
    def _hashtagSplit(self, hashtags):
        htags, indices = [], []
        for tag in hashtags:
            htags.append(str(tag['text']))
            indices.append(tag['indices'])      
        return htags, indices