import tweepy
import time

#Accès au compte tweeter
auth = tweepy.OAuthHandler('KBnjLfAcKbb4t2B5yNabLrUib','4kT5dmBUh6W7kt7VwACT5Q0CFBz9hep28gqtUVVCT9vpG7pFVV')
auth.set_access_token('1420006259097575425-BIJ2L4tGBY9Z7epooDkPLZTOTD7DwP','Cdb1ot6mDEHP3PHKd6mnujR1Lf2U0uK3dCISdc3trX8vt')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user.screen_name)