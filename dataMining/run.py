
#! /usr/bin/env python

__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"


import argparse, pickle

from twitter.extraction import runner
from twitter.cursor import Cursor 
from twitter.stream import StdOutListener, Stream
from twitter.tweet import Tweet
from google.googleProcessing import googleJobs, googleSkills
from google.query import runSkills, runTitles
from google.test.googleTests import test 

from settings import TWITTER_CURSOR_FILE, TWITTER_STREAM_FILE, GOOGLE_TITLE_SNIPPET_FILENAME, GOOGLE_SKILL_SNIPPET_FILENAME

def getArgs():
    parser = argparse.ArgumentParser(description='data mining app')
    parser.add_argument('-t', '--cursorclean', type=str, action="store", )    
    parser.add_argument('-tc', '--cursor', type=str, action="store", )
    parser.add_argument('-ts', '--stream', type=str, action="store", )

    return parser.parse_args()

def twitterCursor(query):
    c = Cursor(open(TWITTER_CURSOR_FILE, 'w'))
    c.page(query)
    c.close()

def twitterStream(query):
    listener = StdOutListener(open(TWITTER_STREAM_FILE, 'w'))
    Stream(listener, query)
    
def pickleLoader(pklFile):
    try:
        while True:
            yield pickle.load(pklFile)
    except EOFError:
        pass
    
def twitterCursorClean(test):

    with open(TWITTER_CURSOR_FILE, 'r') as f:
        for tweet in pickleLoader(f):
            print(tweet)
            cleanText = runner(tweet)
            print("ANSW: " + cleanText)
            print('-------------------')
    file.close()

def twitterStreamClean(test):

    with open(TWITTER_STREAM_FILE, 'r') as f:
        for tweet in pickleLoader(f):
            cleanText = runner(tweet)

            print(tweet)
            print(cleanText)
            print('-------------------')
    file.close()

#GOOGLE FUNCTIONS    
def googleGetJobTitles(jobName):
    googleJobs(jobName)
    
def googleGetSkills(jobName):
    googleSkills(jobName)
    
def googleQueryTitles(initialTitle):
    runTitles(initialTitle, GOOGLE_TITLE_SNIPPET_FILENAME)
    
def googleQuerySkills(initialTitle, searchTitle):
    runSkills(initialTitle, searchTitle, GOOGLE_SKILL_SNIPPET_FILENAME)
    
def googleAlgorithmTest():
    test()
        
    
available_actions = {"cursor": twitterCursor, "stream": twitterStream, "cursorclean": twitterCursorClean, 
                     "googlejobs": googleGetJobTitles, "googleskills": googleGetSkills, "googleAlgorithmTest": googleAlgorithmTest,
                     "googleQueryTitles": googleQueryTitles, "googleQuerySkills": googleQuerySkills}

if __name__=='__main__':
    
    args = vars(getArgs())
    l = [{k:v} for k, v in args.iteritems() if v is not None]
    method, methodArgs = l.pop().popitem()
    available_actions[method](methodArgs)
