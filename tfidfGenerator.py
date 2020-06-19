import math
from pyDataSet import pyDataSet
from textblob import TextBlob
import pickle
import numpy as np

# Output will be the Matrix of TFIDF
bloblist = []


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def idf(word):
    return math.log(len(bloblist) / (1 + n_containing(word)))


def n_containing(word):
    count = 0
    for blob in bloblist:
        if word in blob.words:
            count = count + 1

    return count


def tfidf(word, blob):
    return tf(word, blob) * idf(word)


def GetTFIDF(s):
    Dict = {}
    TFIDFMAtrix = np.zeros(shape=(19733, 8628))
    with open("Dictionary.pickle", "rb") as handle:
        Dict = pickle.load(handle)
        print(len(Dict))

    DaS = None

    with open(s, "rb") as handle:
        DaS = pickle.load(handle)
        for doc in DaS.DocList:
            sen = TextBlob(" ".join(doc.TermList))
            bloblist.append(sen)

    for doc in DaS.DocList:
        for w in doc.TermList:
            dw = Dict[w]
            tif = tfidf(w, TextBlob(" ".join(doc.TermList)))
            print(doc.Id, dw, tif)
            TFIDFMAtrix[doc.Id, Dict[w]] = tif

    with open("TFIDFMAtrix.pickle", "wb") as handle:
        pickle.dump(TFIDFMAtrix, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    GetTFIDF("Dataset.pickle")
