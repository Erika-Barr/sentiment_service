import pdb
import tweepy
from textblob import TextBlob

consumerKey = "UV2iAeUsTqdGTUl0ylHNgXYSe"
consumerKeySecret = "gRIdePrzj0zYLlgDIygNos3IyXARVDG0KpQofSt0FtaEn5Ywp0"
accessToken = "772362634582634496-Ky08ZJZE6zBm2WESRxjeHQbCx6LuzE4"
accessTokenSecret = "YJaiA5MzImPHniHTwlnG6ZPrFhacyxrj70x00D70AkRmw"

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def getUserTimeline(handle):
    userTweets = api.user_timeline(screen_name=handle, count=100)
    return userTweets

def sentiment(tweet):
    polarity = TextBlob(tweet.text).sentiment.polarity
    if polarity < 0: return "negative"
    if polarity is 0: return "neutral"
    return "positive"

#'''
def getPercentages(tweets):
    count = {"positive": 0, "neutral": 0, "negative": 0}
    for sentiment in map(lambda tweet: tweet["sentiment"], tweets):
        count[sentiment] += 1
    percentages = {}
    for sentiment in ["positive", "neutral", "negative"]:
        percentages[sentiment] = (count[sentiment]/len(tweets))
    return percentages
#'''

def getSentimentAnalysis(handle):
    tweets = getUserTimeline(handle)    
    analyzed_tweets = {"tweets": [] }
    # calculate sentiments 
    for tweet in tweets:
        analyzed_tweets["tweets"].append( {"text": tweet.text, "username": tweet.user.screen_name, "sentiment": sentiment(tweet)} )
    # calculate sentiment percentages
    percentages = getPercentages(analyzed_tweets["tweets"])
    analyzed_tweets["percentages"] = percentages
    return analyzed_tweets
    
'''
def getOverallPolarity(handle):
    tweets = getUserTimeline(handle)    
    polaritySum = 0
    for tweet in tweets:
        text = TextBlob(tweet.text)       # text -> Textblob object
        polaritySum += text.sentiment.polarity # summation of polarity from tweets
    return polaritySum/len(tweets)
'''

#function calls
handle = "@realDonaldTrump"
#print( list(map(lambda e: e.text, getUserTimeline(handle))) )
#print(getOverallPolarity(handle))
#print(getSentimentAnalysis(handle))
#print( getPercentages( getSentimentAnalysis(handle) ) )
