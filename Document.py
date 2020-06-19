class Doc:
    def __init__(self, DocId, Terms, Class=0, Sentiment=0):
        self.Id = DocId
        self.TermList = Terms
        self.Sentiment = Sentiment
        self.Class = Class
