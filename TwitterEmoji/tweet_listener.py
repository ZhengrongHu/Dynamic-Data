#!/usr/bin/env python
__author__ = "Jiajun Chen, Zhengrong Hu"
__version__ = "1.0"
__email__ = "j.chen9@med.miami.edu,z.hu1@umiami.edu"
__status__ = "Tested"

from tweepy import StreamListener
import json,sys,time


# This is a basic listener that just prints received tweets to stdout.
class TweetListener(StreamListener):

    def __init__(self):
        self.counter = 0

    def on_data(self, data):

        if 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        else:
            output = open('tweetsData.json', 'a+')
            self.counter += 1
            output.write(data)
            output.close()
            return True

    def on_error(self, status):
        sys.stderr.write("[ERROR]: "+ str(status)+"\n")
        return

    def on_limit(self, track):
        sys.stderr.write("[Limit]: "+ track + "\n")
        return

    def on_timeout(self):
        sys.stderr.write("Timeout, pause for 60 seconds...\n")
        time.sleep(60)
        return

