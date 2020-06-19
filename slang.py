slangwords = {}
import string
import pickle
from CleanTweet import clean_tweet
from pyDataSet import pyDataSet
from senticnet.senticnet import SenticNet

# Dict = {}
# with open("Dictionary.pickle", "rb") as handle:
#     Dict = pickle.load(handle)
with open("SlangSD/SlangSD.txt", encoding="utf8") as f:
    for line in f:
        split = line.split("\t")
        val = int(split[1])
        key = clean_tweet(split[0])
        slangwords[key] = val
        # print(key, val)

# porvalis = {}
# with open("normwords.pickle", "rb") as handle:
#     porvalis = pickle.load(handle)

# kaggeleSentiment = {}
# with open("SlangSD/new.pickle", "rb") as handle:
#     kaggeleSentiment = pickle.load(handle)


# c = 0
# for w in Dict.keys():
#     if w not in porvalis and w not in slangwords and w not in kaggeleSentiment:
#         print(w)
#         c = c + 1

# print(c)
def Precision(tp, fp):
    return tp / (tp + fp)


def Recall(tp, fn):
    return tp / (tp + fn)


sn = SenticNet()
zeroSen = 0
tp = 0
tn = 0
fp = 0
fn = 0
actT = 0
with open("Dataset.pickle", "rb") as handle:
    pyDS = pickle.load(handle)
    for doc in pyDS.DocList:
        totSen = 0
        for w in doc.TermList:
            try:
                sen = sn.polarity_intense(w)
            except KeyError:
                sen = 0

            # if w in slangwords:
            #     sen = slangwords[w]
            # elif w in kaggeleSentiment:
            #     sen = kaggeleSentiment[w]
            # elif w in porvalis:
            #     sen = porvalis[w]

        totSen = totSen + float(sen)
        doc.Sentiment = totSen
        #  true             positive
        if doc.Class == 1 and totSen < 0.5:
            tp = tp + 1

        elif doc.Class == 0 and totSen > 0:
            tn = tn + 1

        elif doc.Class == 0 and totSen < 0:
            fp = fp + 1
            #  false            negetive
        elif doc.Class == 1 and totSen > 0:
            fn = fn + 1

        if totSen == 0:
            zeroSen = zeroSen + 1

# print(zeroSen)
print(tp, tn, fp, fn)
print(Precision(tp, fp), Recall(tp, fn))


import pickle

# print(slangwords)
# # in open ('------', 'wb') thus wb always as second part!!!


with open("DSwithSentiment.pickle", "wb") as handle:
    pickle.dump(pyDS, handle, protocol=pickle.HIGHEST_PROTOCOL)

