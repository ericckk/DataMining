#! /usr/bin/env python

import argparse
from twitter.cursor import Cursor 
from twitter.stream import StdOutListener, Stream
from settings import TWITTER_CURSOR_FILE, TWITTER_STREAM_FILE

def getArgs():

    parser = argparse.ArgumentParser(description='data mining app')
    parser.add_argument('-tc', '--cursor', nargs=1, type=str, action="store", )
    parser.add_argument('-ts', '--stream', nargs=1, type=str, action="store", )
    parser.add_argument('-ta', '--algorithm', nargs=1, type=str, action="store", )
    return parser.parse_args()

def twitterCursor(query):
    c = Cursor(open(TWITTER_CURSOR_FILE, 'w'))
    c.page(query)

def twitterStream(query):
    listener = StdOutListener(open(TWITTER_STREAM_FILE, 'w'))
    Stream(listener, query)
    
available_actions = {"cursor": twitterCursor, "stream": twitterStream,}

if __name__=='__main__':
    
    args = vars(getArgs())
    
    
    method = args.items().pop()[0]
    additional = args.items().pop()[1]
    print(args.items())
    available_actions[method](additional)