# __author__ = 'Erin'

from bs4 import BeautifulSoup
import re
import nltk.stem
import count

def preprocessor(row_review):
    global emoticons_replaced
    data=BeautifulSoup(row_review).get_text()
    data = data.lower()
    for k in count.emo_repl_order:
        data = data.replace(k, count.emo_repl[k])
    for r, repl in count.re_repl.iteritems():
        data = re.sub(r, repl, data)
    data = data.replace('\'s ','')
    data = re.sub("[^a-z]"," ",data)
    newdata =" ".join(data.split())

    # english_stemmer = nltk.stem.SnowballStemmer('english')
    # newdata = " ".join([english_stemmer.stem(w) for w in data.split()])

    return newdata

    # method 1
    # example1=BeautifulSoup(row_review)
    # letters_only=re.sub("[^a-zA-Z]"," ",example1.get_text())
    # lower_case=letters_only.lower()
    # words=lower_case.split()
    # words=[w for w in words if not w in stopwords.words("english")]

    # method 2
    # data1=BeautifulSoup(row_review).get_text()
    # data1=data1.lower()
    # data1=data1.replace('n\'t',' not').replace('does\'nt','does not').replace('i\'m','').replace('\'ve ','').\
    #     replace('\'s ','').replace('\'re ','').replace('\'ll ',' will').replace('\'d ','')
    # data1=data1.replace('&','and')
    # data1=re.sub(r'\d+','num',data1)
    # data1=re.sub("[^a-z]"," ",data1)
    # newdata=" ".join(data1.split())
