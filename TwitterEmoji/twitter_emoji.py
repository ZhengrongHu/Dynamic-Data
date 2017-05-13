# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = "Jiajun Chen, Zhengrong Hu"
__version__ = "1.0"
__email__ = "j.chen9@med.miami.edu, z.hu1@umiami.edu"
__status__ = "Tested"

# Import the necessary methods
from tweepy import OAuthHandler
from tweepy import Stream
from tweet_listener import TweetListener
import json, re
import pandas as pd
import matplotlib.pyplot as plt

# needs to pip install tweepy, pandas,matplotlib, emoji


# Variables that contains the user credentials to access Twitter API
access_token = "861255248647794688-KM68ySUJ2cEeqBjUbntqcleqkwwjPH3"
access_token_secret = "ynzuHJ0QYnc8D8j4xBlWMraj7DTyEBQnjQnXPVGpCrGOq"
consumer_key = "X2YZiQk52YUwxTtUc5pO1Y3VL"
consumer_secret = "Fh7H60jYSBPed8MdCRZxLtTKoOF4Y0zw9bdvU2K310P9RSsif1"


# Menu page
def menu():
    print "========Welcome to Twitter Emoji System========";
    print "Menu"
    print "[1]: Fetch tweets"
    print "[2]: Analyze data"
    print "[3]: Exit"
    option = raw_input("What would you like to do?:")
    return option


# Fetch tweets from Twitter API
def fetch_tweets():
    # Step1: Get keywords from user input
    user_input = raw_input("Please enter the keywords that you need to monitor(separate by comma):")
    keywords = user_input.replace(' ', '').split(",")  # does not change the original string

    print "Going to monitor following keywords:",
    print '[%s]' % ', '.join(map(str, keywords))

    # Step2: Perform Twitter authentication and connect to Twitter Streaming API
    print "Initializing the TwitterEmoji system..."
    listen = TweetListener()
    print "Connecting to the Twitter Server...",
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listen)
    print "[Done]"
    print "Start looking for emoji...."

    # ['trump', 'hillary', 'obama', 'bush', 'clinton']
    try:
        # This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=keywords)
    except:
        print "Reach the rate limit, data has been saved to a local file"
        stream.disconnect()
        # Count the amount number of tweets
        tweets_data = []
        tweets_file = open("tweetsData.json", "r")
        for line in tweets_file:
            try:
                tweets_data.append(json.loads(line))
            except:
                continue
        print "Now you have ", len(tweets_data), " tweets in the data file"
        main()


# extract emoji from the tweets
def extract_emoji(text):
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)
    emo = emoji_pattern.findall(text)
    emojis = []
    if len(emo) > 0:
        try:
            for emoitems in emo:
                for emoji in emoitems:
                    if len(emoji) > 0:
                        emojis.append(emoji)
            return emojis
        except UnicodeError:
            print "Error"


# analyze the data
def analyze_data():

    # Idea 1, analyze data directly using pandas' function
    # tweets_data = []
    # tweets_file = open("tweetsData.json","r")
    # for line in tweets_file:
    #     try:
    #         tweets_data.append(json.loads(line))
    #     except:
    #         continue
    # print "You have ",len(tweets_data)," tweets in the data file"
    # tweets = pd.DataFrame()
    # tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    # tweets['emoji'] = tweets['text'].apply(lambda tweet: extract_emoji(tweet))
    # print tweets['emoji']
    # emojis = tweets['text'].str.findall(u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    #     u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    #     u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    #     u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    #     u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    #     "+")
    # print emojis
    # print tweets['emoji'].value_counts()

    # Idea 2, find out all emojis and put them into a list
    emoji_data = []
    tweets_file = open("tweetsData.json", "r")
    tweet_counter = 0
    for line in tweets_file:
        try:
            emoji_data += extract_emoji(json.loads(line)['text'])
            tweet_counter += 1
        except:
            continue
    print "You have totally", len(emoji_data), " emojis in ",tweet_counter," tweets that contain emoji"
    tweets = pd.DataFrame()
    tweets['emoji'] = emoji_data
    tweets_by_emoji = tweets['emoji'].value_counts()
    print "Here is the result:"
    print tweets_by_emoji
    print "==========Top 5 Emojis========="
    print tweets_by_emoji[:5]
    print "==============================="
    ax = plt.subplot()
    ax.set_xlabel('Emoji',fontsize=15)
    ax.set_ylabel('Number of emoji', fontsize=10)
    try:
        tweets_by_emoji[:5].plot(ax=ax,kind='bar')
        plt.show()
    except:
        print "Error"


def main():

    # analyze_data()
    option = menu()
    if option == '1':
        print "Going to fetch tweets"
        fetch_tweets()
    elif option == '2':
        print "Going to analyze data"
        analyze_data()
    elif option == '3':
        print "Thank you"
        return
    else:
        print "Invalid input"
        menu()


if __name__ == '__main__':
    main()





