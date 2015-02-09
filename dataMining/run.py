
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

from settings import TWITTER_CURSOR_FILE, TWITTER_STREAM_FILE

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
            cleanText = runner(tweet)

            print(tweet)
            print(cleanText)
            print('-------------------')
    file.close()
    
    
available_actions = {"cursor": twitterCursor, "stream": twitterStream, "cursorclean": twitterCursorClean,}

if __name__=='__main__':
    
    args = vars(getArgs())
    l = [{k:v} for k, v in args.iteritems() if v is not None]
    method, methodArgs = l.pop().popitem()
    available_actions[method](methodArgs)
