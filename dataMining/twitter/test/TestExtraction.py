
#! /usr/bin/env python

__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

import unittest
from dataMining.twitter.extraction import punctuation


class TestExtractionClass(unittest.TestCase):
    
    def testPunctuation(self):
        self.testString = ';Th:is ,is| a test.'
        self.assertEqual("This is a test", punctuation(self.testString))
        
    

if __name__ == '__main__':
    unittest.main()