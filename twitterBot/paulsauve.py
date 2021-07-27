import tweepy
import time

#ACCOUNT ACCESS
auth = tweepy.OAuthHandler('cTSQ5cakn17HusuvtItWEwuJ0','SiZnYughKFmLX3xt59YIFblyeYmbW0XqC0x9MU23A6DvKarNyU')#API KEY, #API KEY SECRET
auth.set_access_token('1420006259097575425-MLaER8Fnnr8b6czUfXmrIJLlCWiVMQ','HnapXyoJVwSX3m50lP87cjN0IZJiHFSr13UdljyiZLHux')#TOKEN, #SECRET TOKEN

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Business','Consuting','Stratégie Consulting'
nbTweets = 500 

for tweet in tweepy.Cursor(api.search, search).items(nbTweets):
    try:
        tweet.retweet()
        print('Tweet Reposted')
        tweet.favorite()
        print('Tweet liked')
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break       