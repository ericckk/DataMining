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
        self._hashtags, self._hashtagIndex = self._hashtagSplit(hashtags)
        self._location = self._decode(location)
     
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = self._decode(value)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = self._decode(value)

    @property
    def screenName(self):
        return self._screenName
    
    @screenName.setter
    def screenName(self, value):
        self._screenName = self._decode(value)

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = self._decode(value)

    @property
    def hashtags(self):
        return self._location

    @property
    def hashtagIndex(self):
        return self._hashtagIndex
    
    @hashtags.setter
    def hashtags(self, value):
        self._hashtags, self._hashtagIndex = self._hashtagSplit(value)

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        self._location = self._decode(value)
                        
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
