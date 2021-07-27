import tweepy
import time

#Accès au compte tweeter
auth = tweepy.OAuthHandler('9hlV3L2CWhuzBxTMC5iyZuoZ1','e5xbjUCRUHAwdAO2x6sRGXcim73tcwRhMULM3slBLwKhfTOreW')
auth.set_access_token('1420006259097575425-iaRYNp1JV1HfsrdshvEUnTiHMhv7k5','fnLRpbrMSOCJYgDLkgi1BKoI1H7Ocoj1qsxuuktqTSitJ')

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