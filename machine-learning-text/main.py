import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


filepath_dict = {   "yelp" : "sentiment_analysis\\yelp_labelled.txt",
                    "amazon" : "sentiment_analysis\\amazon_cells_labelled.txt",
                    "imdb" : "sentiment_analysis\\imdb_labelled.txt"}

df_list = []

for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=["sentence", "label"], sep="\t")
    df["source"] = source # additional clumn with the source name
    df_list.append(df)

df = pd.concat(df_list)



for source in df['source'].unique():
    df_source = df[df['source'] == source]
    sentences = df_source['sentence'].values
    y = df_source['label'].values

    sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(sentences_train)

    x_train = vectorizer.transform(sentences_train)
    x_test = vectorizer.transform(sentences_test)

    classifier = LogisticRegression()
    classifier.fit(x_train, y_train)
    score = classifier.score(x_test, y_test)

    print("Accuracy for {} data: {:.4f}".format(source, score))




