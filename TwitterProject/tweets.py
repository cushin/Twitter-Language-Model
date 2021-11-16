import os
import tweepy as tw
import pandas as pd
import sys

consumer_key= 'KnUlN9kEQ7gJdDiVp8oNE1Wg2'
consumer_secret= 'mRtOVvdiZIzqwdxebqo47WmOBGBvWjIwtZvufDU2E84vlm5QV4'
access_token= '1027293645676769280-2heVzKV4eDN7LDv0Udtk8VkE8Ubj9m'
access_token_secret= '6RdwPKQbgIX75EcsI3eovdsqhtomqUgsHWo4Lwa1lOwnM'

new_search = "kanye -filter:retweets -filter:comments"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


tweets = tw.Cursor(api.search,
                   q=new_search,
                   lang="en",
                   since='2020-01-01').items(1000)
                   
all_tweets = [tweet.text for tweet in tweets]
output = open("tweets.txt", "wb")
for tweet in all_tweets:
    output.write(tweet.encode("utf-8"))
    output.write("\n".encode("utf-8"))
output.close()
