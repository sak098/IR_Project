import re
import json
from CleanTweet import clean_tweet
from nltk.tokenize import word_tokenize
from TextProcessing import TextProcess
from Document import Doc
import pickle


class pyDataSet:
    def __init__(self, pathName):
        self.DocList = []
        self.EnDict = []
        with open("ENDict.pickle", "rb") as handle:
            self.EnDict = pickle.load(handle)
        docNo = 0
        with open(pathName) as f:
            for line in f:
                j_content = json.loads(line)
                tweet = clean_tweet(j_content["content"])
                cl = int(j_content["annotation"]["label"][0])

                words = word_tokenize(tweet)
                filtered = []

                for w in words:
                    w = TextProcess(w)
                    if w == "" or w not in self.EnDict:
                        continue

                    filtered.append(w)

                if len(filtered) == 0:
                    continue

                print("Doc", docNo, ":", filtered, " :", cl)
                doc = Doc(docNo, filtered, cl)
                self.DocList.append(doc)
                docNo = docNo + 1


if __name__ == "__main__":
    # DS = pyDataSet("Dataset.json")
    # import pickle

    # with open("Dataset.pickle", "wb") as handle:
    #     pickle.dump(DS, handle, protocol=pickle.HIGHEST_PROTOCOL)

    import pickle

    with open("DSwithSentiment.pickle", "rb") as handle:
        DS_w_Senti = pickle.load(handle)
        DS_SENTI_CLASS_Dict = {}
        for d in DS_w_Senti.DocList:
            DS_SENTI_CLASS_Dict[d.Id] = (d.Sentiment, d.Class)
            print(DS_SENTI_CLASS_Dict[d.Id])
        with open("DS_Senti_Class.pickle", "wb") as handle:
            pickle.dump(DS_SENTI_CLASS_Dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
