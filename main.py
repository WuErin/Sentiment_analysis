# __author__ = 'Erin'

from read_files import read_files
from read_files import read_by_line
from review_to_words import review_to_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas
import time

a = time.time()

# get train and test reviews
train_rawdata = read_files("input_data\\labeledTrainData.tsv")
test_rawdata = read_files("input_data\\testData.tsv")

train_cleandata = read_by_line("input_data\\output_train.txt")
test_cleandata = read_by_line("input_data\\output_test.txt")

b = time.time()
print "read files spend" +str(b-a)+"second"

# split reviews to words
# for i in xrange(train_rawdata.shape[0]):
#    train_rawdata["review"][i]=review_to_words(train_rawdata["review"][i])

#for j in xrange(test_rawdata.shape[0]):
#    test_rawdata["review"][j]=review_to_words(test_rawdata["review"][j])

# Creating features from Bag of Words
vectorizer = CountVectorizer(analyzer="word",ngram_range=(1,1),tokenizer = None,preprocessor = None,stop_words = None, max_features=5000)
train_data_features = vectorizer.fit_transform(train_cleandata)
#train_data_features = train_data_features.toarray()


# take a look at the features
# vocab = vectorizer.get_feature_names()
# print vocab

# random forest
# 100 trees
forest = RandomForestClassifier(n_estimators=100)
forest_model = forest.fit(train_data_features,train_rawdata["sentiment"])

# get results
test_data_features = vectorizer.fit_transform(test_cleandata)
result = forest_model.predict(test_data_features)
output = pandas.DataFrame(data={"id":test_rawdata["id"], "sentiment":result})
output.to_csv("output_data\\Bag_of _Words_model.csv",index=False,quoting=3 )