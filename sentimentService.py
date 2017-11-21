import tweepy
from textblob import TextBlob

consumerKey = 'UV2iAeUsTqdGTUl0ylHNgXYSe'
consumerKeySecret = 'gRIdePrzj0zYLlgDIygNos3IyXARVDG0KpQofSt0FtaEn5Ywp0'
accessToken = '772362634582634496-Ky08ZJZE6zBm2WESRxjeHQbCx6LuzE4'
accessTokenSecret = 'YJaiA5MzImPHniHTwlnG6ZPrFhacyxrj70x00D70AkRmw'

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def getUserTimeline(handle):
    userTweets = api.user_timeline(screen_name=handle, count=3)
    return userTweets

def getOverallPolarity(handle):
    tweets = getUserTimeline(handle)    
    polaritySum = 0
    for tweet in tweets:
        text = TextBlob(tweet.text)       # text -> Textblob object
        polaritySum += text.sentiment.polarity # summation of polarity from tweets
    return polaritySum/len(tweets)

#function calls
#print(getUserTimeline('@realDonaldTrump'))
#print(getOverallPolarity('@realDonaldTrump'))

