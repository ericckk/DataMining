__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"


class Tweet(object):
    def __init__(self, text, name, screenName, description, hashtags, location):
        
        self._text = self._decode(text)
        self._name = self._decode(name)
        self._screenName = self._decode(screenName)
        self._description = self._decode(description)
        self._hashtags, self.hashtagIndex = self._hashtagSplit(hashtags)
        self._location = self._decode(location)
        
    def __repr__(self):
        strRep = "tweet: " + self._text + '\nname: ' + self._name + '\nscreen name: ' + self._screenName + '\ndescription: ' + self._description + '\nlocation: ' + self._location + '\nhashtags: '
        strRep += ' '.join(self._hashtags) + '\n' + '\n'
        return strRep
    
    def _decode(self, text):
        if text==None:
            return ''
        else:
            return text.encode('ascii', 'replace')
        
    def _hashtagSplit(self, hashtags):
        htags, indices = [], []
        for tag in hashtags:
            t = tag['text']
            i = tag['indices']
            htags.append(self._decode(t))
            indices.append(i)    
        return htags, indices
