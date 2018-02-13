import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

def train(features):
    train_label=np.zeros(702);
    train_label[351:701]=1;
    model1=MultinomialNB()
    model2=LinearSVC()
    model1.fit(features,train_label);
    model2.fit(features,train_label);

    return model1,model2;
    
