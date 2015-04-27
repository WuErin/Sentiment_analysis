# __author__ = 'Erin'

from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords


def review_to_words(row_review):
    # remove HTML markup
    example1=BeautifulSoup(row_review)

    # use regular expressions to do a find-and-replace   only keep letters
    letters_only=re.sub("[^a-zA-Z]"," ",example1.get_text())

    #convert to lower case
    lower_case=letters_only.lower()

    # split into words
    words=lower_case.split()

    # remove stop words
    words=[w for w in words if not w in stopwords.words("english")]
    return words