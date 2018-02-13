import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

def test(tfeatures,model1,model2):
    test_labels = np.zeros(260);
    test_labels[130:260] = 1;
    result1 = model1.predict(tfeatures);
    result2 = model2.predict(tfeatures);

    return result1,result2;
