import unittest
from unittest import mock
import request
import sys
sys.path.insert(0, "/Users/EB/Documents/python/sentimentAI")
from sentimentService import *

labeledData = [(-1, "negative"), (0, "neutral"), (1, "positive")]

# ===== sentiment() =====
def test_generator():
    for param in labeledData:
        yield check_sentiment, param[0], param[1]

def check_sentiment(a, b):
        assert sentiment(a) == b

