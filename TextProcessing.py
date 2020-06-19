import nltk as nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

cmn_abbrs = {
    "r": "are",
    "u": "you",
    "ur": "your",
    "y": "why",
    "dat": "that",
    "da": "the",
    "dem": "them",
    "dems": "Democrat",
}


def removeNumber(word):
    result = "".join([i for i in word if not i.isdigit()])
    return result


def CheckNumber(w):
    try:
        int(w)
        return True
    except ValueError:
        return False


def TextProcess(w):

    w = w.strip()

    # Blank Word

    if len(w) < 3:
        return ""

    # Check Number
    if CheckNumber(w):
        return ""

    # remove numbers from string
    w = removeNumber(w)

    # to lower Case
    w = w.lower()

    if w.startswith("haha"):
        return "ha"

    if w.endswith("haha"):
        return "ha"

    # Expand Common Abbreviations
    if w in cmn_abbrs:
        w = cmn_abbrs[w]

    w = str(TextBlob(w).correct())
    # w=
    stop_words = set(stopwords.words("english"))

    if w in stop_words:
        return ""

    lemma = WordNetLemmatizer()
    w = lemma.lemmatize(w, "v").lower()

    return w


# lemma.lemmatize('indulgence', pos="v").lower()

