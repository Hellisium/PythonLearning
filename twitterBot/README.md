# :bird: twitterBot
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/for-robots.svg)](https://forthebadge.com)

## Description

tweetBot allows to browse the list of keywords added in parameter and to : 

- Retweet a few tweets who have some specifics keywords 
- Like those tweets :arrow_up:

## Goals 

This little script is an exercise to increase the visibility of a twitter account for purely marketing purposes.

## Imports 
Add the library called "Tweepy" 
```python
pip install Tweepy



import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

``` 
:bird: [Twitter](https://twitter.com/PierreDelmas12) 
:books: [Library](https://docs.tweepy.org/en/stable/index.html)
