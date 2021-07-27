import tweepy
import time

#ACCOUNT ACCESS
auth = tweepy.OAuthHandler('rO2SyYq2aVihXmL0IwX6nvqgF','txWQka34AhnMFrZRrUiEmTH5617uuZv39keRiTbS0d59XMKtv9')#API KEY, #API KEY SECRET
auth.set_access_token('1420006259097575425-YYtll1EJ2yOZUvi9iF8byaFINowNdh','rBqO5rg7AzTbalzQEVp13DvyomUJz0mRxyybDtsJiKl58')#TOKEN, #SECRET TOKEN

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Business','Marketing' #Keyword(s)
nbTweets = 200 #Limit of Tweets searched

for tweet in tweepy.Cursor(api.search, search).items(nbTweets):
    try:
        tweet.retweet()
        print('Tweet Reposted')
        tweet.favorite()
        print('Tweet liked')
        time.sleep(3) #time between 2 repost & like
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break       