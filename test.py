# __author__ = 'Erin'
import pandas
import sys
from review_to_words import preprocessor
from random import *
from count_tfidf import count_tfidf
import nltk
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn import svm

reload(sys)
sys.setdefaultencoding("utf-8")
raw_data = pandas.read_csv("input_data\\labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

# generate test data index
a = Random();a.seed(1)
test_index = a.sample(range(raw_data.shape[0]),5000)

# data preprocessing
train_data = []
test_data = []
train_senti = []
test_senti = []
# outfile=open("output_data\\testoutput.txt","w+")
# outfile.write(test_data+'\n')
# outfile.close()
for i in xrange(raw_data.shape[0]):
    review=preprocessor(raw_data["review"][i])
    if i in test_index:
        test_data.append(review)
        test_senti.append(raw_data["sentiment"][i])
    else:
        train_data.append(review)
        train_senti.append(raw_data["sentiment"][i])
print("1")
# generate matrix
train_tfidf = count_tfidf(train_data)
test_tfidf = count_tfidf(test_data)
print("2")

# Naive Bayes in sklearn package
clf = MultinomialNB()
clf.fit(train_tfidf,train_senti)
test_predicted = clf.predict(test_tfidf.toarray())
print(np.mean(test_senti==test_predicted))


# SVM method in sklearn package
# clf = svm.SVC(kernel="rbf", C = 1)
# clf.fit(train_tfidf,train_senti)
# test_predicted = clf.predict(test_tfidf.toarray())
# print(np.mean(test_senti==test_predicted))


# use NB in nltk package
# def change_to_dict(dataset):
#     data_dict = {}
#     i = 0
#     for word in list(dataset):
#         data_dict[i] = word
#         i+=1
#     return data_dict
#
# train=[]
# test=[]
# count_train=0
# count_test=0
# for j in xrange(raw_data.shape[0]):
#     if j in test_index:
#         tfidf_split1 = change_to_dict(test_tfidf[count_test])
#         test.append((tfidf_split1,raw_data["sentiment"][j]))
#         count_test=count_test+1
#     else:
#         tfidf_split2 = change_to_dict(train_tfidf[count_train])
#         train.append((tfidf_split2,raw_data["sentiment"][j]))
#         count_train=count_train+1
#
# classifier = nltk.NaiveBayesClassifier.train(train)
# accuracy = nltk.classify.accuracy(classifier,test)
# print accuracy