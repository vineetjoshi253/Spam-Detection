#Spam Detection With Multinomial Bayesian Classifier and Linear Support Vector Machine
#Vineet Joshi
#GEU,Dehradun
"""-------------"""

import numpy as np
from sklearn.metrics import confusion_matrix
from dictn import dictionary_const
from features import features_const
from training import train
from testing1 import test
from testing2 import usertest
#Data Preprocessing
dictionary=[];
train_path='train';
dictionary=dictionary_const(train_path);

#Feature Extraction
features=features_const(train_path,dictionary);

#Training SVM and MultinomialNB
NB,SVM=train(features);

#Testing-Phase1:
test_path='test';
tfeatures=features_const(test_path,dictionary);
result1,result2=test(tfeatures,NB,SVM);
test_labels = np.zeros(260);
test_labels[130:260] = 1;
conf_mat1=confusion_matrix(test_labels,result1);
conf_mat2=confusion_matrix(test_labels,result2);
print("Accuracy of Multinomial Bayesian Classifier :");
print(((conf_mat1[0][0]+conf_mat1[1][1])/(conf_mat1[0][0]+conf_mat1[1][1]+conf_mat1[0][1]+conf_mat1[1][0]))*100);

print("Accuracy of Linear Support Vector Machine :");
print(((conf_mat2[0][0]+conf_mat2[1][1])/(conf_mat2[0][0]+conf_mat2[1][1]+conf_mat2[0][1]+conf_mat2[1][0]))*100);

#Testing-Phase2:
a=input("Enter number of strings to test");
for i in range(0,a):
    teststr = input("Enter a string or message to test.\n");
    with open("1.txt","w") as ut:
        ut.write("\n");
        ut.write("\n");
        ut.write(teststr);

    usertest(dictionary,NB,SVM);
    
    

    
