
__author__ = "Justin Milanovic"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

import unittest
from dataMining.twitter.extraction import regexRemoval, phraseLeft, phraseRight
from dataMining.twitter.tweet import Tweet
from dataMining.settings import TWITTER_PUNCTUATION, TWITTER_US_STATES, TWITTER_HYPERLINKS, TWITTER_HASHTAGS, TWITTER_ZIPCODE, TWITTER_MONEY, TWITTER_USERNAME, TWITTER_BRACKETS, TWITTER_SQUARE_BRACKETS_TEXT, \
TWITTER_CUTOFF, TWITTER_DASH_SLASH, TWITTER_US_STATES_2_WORD, TWITTER_STATES

class TestExtractionClass(unittest.TestCase):
   
    def testPunctuation(self):
        self.testTweet = Tweet(text=':;,.?!|RT @BlueLineTalent: Excellent opportunity with start-up for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?')
        self.assertEqual('RT @BlueLineTalent Excellent opportunity with startup for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http//tco/', regexRemoval(self.testTweet, [TWITTER_PUNCTUATION]))
        
    def testUSCityState(self):
        self.testTweet = Tweet(text='Houston, TX RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_US_STATES]))

    def testStates(self):
        self.testTweet = Tweet(text='Texas RT @BlueLineTalent: Excellent opportunity in Arkansas for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv? New Jersey')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in  for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_STATES]))

    def testUSCityState2Word(self):
        self.testTweet = Tweet(text='San Antonio, TX RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv? San Antonio, TX')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_US_STATES_2_WORD]))
    
    def testHyperlink(self):
        self.testTweet = Tweet(text='http://t.co/4l4Libv? RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs', regexRemoval(self.testTweet, [TWITTER_HYPERLINKS]))

    def testHashtags(self):
        self.testTweet = Tweet(text='#Austin RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in Austin, TX for Software Engineer (Jr/Mid Level) http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_HASHTAGS]))

    def testZipcode(self):
        self.testTweet = Tweet(text='55690 RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv? 55342')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_ZIPCODE]))

    def testMoney(self):
        self.testTweet = Tweet(text='$20,000 RT @BlueLineTalent: Excellent opportunity in Austin, TX for $5000 #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv? $62,50.00')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_MONEY]))

    def testUsername(self):
        self.testTweet = Tweet(text='@uofCalgary RT @BlueLineTalent: Excellent opportunity in Austin, TX for @uofCalgary #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv? @uofCalgary')
        self.assertEqual('RT: Excellent opportunity in Austin, TX for #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_USERNAME]))

    def testBrackets(self):
        self.testTweet = Tweet(text='RT @BlueLineTalent: Excellent opportunity in [Austin, TX] for #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in Austin, TX for #Java Software 33445 Engineer Jr/Mid Level #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_BRACKETS]))

    def testSquareBrackets(self):
        self.testTweet = Tweet(text='[Austin, TX] RT @BlueLineTalent: Excellent opportunity in [Austin, TX] for #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv? [Austin, TX]')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in for #Java Software 33445 Engineer (Jr/Mid Level) #Hibernate #CO #Jobs http://t.co/4l4Libv?', regexRemoval(self.testTweet, [TWITTER_SQUARE_BRACKETS_TEXT]))

    def testCutoff(self):
        self.testTweet = Tweet(text='RT @BlueLineTalent: Excellent opportunity in for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs htt...')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in for #Java Software Engineer (Jr/Mid Level) #Hibernate #CO #Jobs', regexRemoval(self.testTweet, [TWITTER_CUTOFF]))

    def testDashSlash(self):
        self.testTweet = Tweet(text='-RT @BlueLineTalent: Excellent opportunity in for #Java -Software Engineer - (Jr/Mid Level) \\#Hibernate #CO #Jobs htt//...')
        self.assertEqual('RT @BlueLineTalent: Excellent opportunity in for #Java Software Engineer  (JrMid Level) #Hibernate #CO #Jobs htt...', regexRemoval(self.testTweet, [TWITTER_DASH_SLASH]))

    def testPhraseLeft(self):
        self.testTweet = Tweet(text='@BlueLineTalent: is looking for a Sales Manager in Austin')
        self.assertEqual("Sales Manager in Austin", phraseLeft(self.testTweet)) 
        
    def testPhraseRight(self):
        self.testTweet = Tweet(text='Developer needed for a Sales Operations  #Seattle #Jobs http://t.co/yudRz40Uyq')
        self.assertEqual("Developer", phraseRight(self.testTweet))        
                
if __name__ == '__main__':
    unittest.main()