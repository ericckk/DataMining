
#! /usr/bin/env python

__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

import unittest
from dataMining.twitter.extraction import regex_removal, phraseLeft, phraseRight
from dataMining.twitter.tweet import Tweet

class TestExtractionClass(unittest.TestCase):
    
    def testPunctuation(self):
        self.testTweet = Tweet(text=';Th:is ,is| a test.')
        self.assertEqual("This is a test", regex_removal(self.testTweet))
        
    def testCityStateZipcode(self):
        self.testTweet = Tweet(text='Data Warehouse/Systems Architect Miami city, FL 50064')
        self.assertEqual("Data Warehouse/Systems Architect", regex_removal(self.testTweet))    

    def testUrl(self):
        self.testTweet = Tweet(text='http://t.co/Ju4CbTEiam Developer - AWS Sales Operations  #Seattle #Jobs http://t.co/yudRz40Uyq')
        self.assertEqual("Developer  AWS Sales Operations", regex_removal(self.testTweet))  

    def testPhraseLeft(self):
        self.testTweet = Tweet(text='Developer - AWS is looking for a Sales Operations')
        self.assertEqual("Sales Operations", phraseLeft(self.testTweet)) 
        
    def testPhraseRight(self):
        self.testTweet = Tweet(text='Developer needed for a Sales Operations  #Seattle #Jobs http://t.co/yudRz40Uyq')
        self.assertEqual("Developer", phraseRight(self.testTweet))        
                
               
                
                
if __name__ == '__main__':
    unittest.main()