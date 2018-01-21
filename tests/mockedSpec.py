import unittest
from unittest.mock import patch
import tweepy
import sys
sys.path.insert(0, "/Users/EB/Documents/personal_projects/sentiment_service")
from sentimentService import *

def load_cache():
    pickle.load(open("test_data.pickle", "rb"))
DATA = load_cache()

# ===== getUserTimeline() =====

response = lambda e: "Tweepy: Twitter user timeline for {}".format(e)

class getUserTimelineMock(unittest.TestCase):
    #@patch.object(tweepy.API, "user_timeline", return_value=response("@realDonaldTrump"))
    #@patch('getUserTimeline', side_effect=load_cache())
    @patch.object(tweepy.API, "user_timeline",side_effect=load_cache())
    def test_getUserTimeline(self, patched_function):
        assert len(getSentimentAnalysis('mocked_handle')["tweets"]) == 100


if __name__ == "__main__":
    unittest.main()

#self.assertEqual(getUserTimeline("@realDonaldTrump"), "Tweepy: Twitter user timeline for @realDonaldTrump" )
