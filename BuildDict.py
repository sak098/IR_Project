import re
import json
import pickle
from CleanTweet import clean_tweet
from nltk.tokenize import word_tokenize
from TextProcessing import TextProcess
from pyDataSet import pyDataSet

WordDict = {}


def BuildDictionary():
    with open("Dataset.pickle", "rb") as handle:
        DS = pickle.load(handle)
        wordId = -1
        for doc in DS.DocList:
            words = doc.TermList
            for word in words:
                if word not in WordDict:
                    print(word)
                    WordDict[word] = wordId = wordId + 1
        print(wordId)


if __name__ == "__main__":
    BuildDictionary()
    with open("Dictionary.pickle", "wb") as handle:
        pickle.dump(WordDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
