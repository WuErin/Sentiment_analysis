# __author__ = 'Erin'

from sklearn.feature_extraction.text import TfidfVectorizer

s1='this is very good, i think you will like it'
s2='i do not think it very bad, may be we can try again'
ll=[]
ll.append(s1)
ll.append(s2)
vectorizer = TfidfVectorizer(ngram_range=(1, 3),analyzer="word", binary=False)
tfidf = vectorizer.fit_transform(ll).toarray()
print tfidf
print "___________________________"
tt=vectorizer.transform(ll).toarray()
print tt