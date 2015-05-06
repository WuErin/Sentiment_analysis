# __author__ = 'Erin'

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def count_tfidf(data):
    vectorizer = TfidfVectorizer(ngram_range=(1,2),analyzer="word", binary=False, max_features=5000)
    tfidf = vectorizer.fit_transform(data)
    # vectorizer = CountVectorizer(analyzer="word",ngram_range=(1,3),tokenizer = None,preprocessor = None,stop_words = None,max_features=100)
    # train_data_features = vectorizer.fit_transform(data)
    return tfidf
