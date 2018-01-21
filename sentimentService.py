from functools import wraps
import pdb
import pickle
import re
from setupCreds import *
import tweepy
from textblob import TextBlob

consumerKey = TWITTER_KEY
consumerKeySecret = TWITTER_SECRET
accessToken = TWITTER_ACCESS_TOKEN
accessTokenSecret = TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
GET_TEST_DATA = False 
TEST_DATA = "tests/test_data.pickle"

def cache(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        r = f(*args, **kwargs)
        if GET_TEST_DATA:
            with open(TEST_DATA, "wb+") as e:
                pickle.dump(r, e)
        return r
    return wrapped

def load_cache():
    pickle.load(open(TEST_DATA, "rb"))

@cache
def getUserTimeline(handle, count=10):
    userTweets = api.user_timeline(screen_name=handle, count=count)
    return userTweets
print(getUserTimeline("@realDonalTrump", count=100))


def getPolarity(tweet):
    return TextBlob(tweet).sentiment.polarity

def sentiment(polarity):
    if polarity < 0: return "negative"
    if polarity == 0: return "neutral"
    return "positive"

def getPercentages(tweets):
    count = {"positive": 0, "neutral": 0, "negative": 0}
    for sentiment in map(lambda tweet: tweet["sentiment"], tweets):
        count[sentiment] += 1
    percentages = {}
    for sentiment in ["positive", "neutral", "negative"]:
        percentages[sentiment] = (count[sentiment]/len(tweets))
    return percentages

def clean(tweet):
    return ' '.join(re.sub("(@[\w\d]+)|(\W \t)|(\w+:\/\/\S+)", " ", tweet).split())

def getSentimentAnalysis(handle):
    tweets = getUserTimeline(handle, count=100)    
    analyzed_tweets = {"tweets": [] }
    # calculate sentiments 
    for tweet in tweets:
        analyzed_tweets["tweets"].append( {"text": tweet.text, "username": tweet.user.screen_name, "sentiment": sentiment(getPolarity(clean(tweet.text)))} ) 
    # calculate sentiment percentages
    percentages = getPercentages(analyzed_tweets["tweets"])
    analyzed_tweets["percentages"] = percentages
    return analyzed_tweets
    
#demo usage
#handle = "@tastytrade"
#print(getSentimentAnalysis(handle))
