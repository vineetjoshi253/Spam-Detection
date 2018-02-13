import numpy as np
from testing1 import test

def usertest(dictionary,NB,SVM):
    features=np.zeros((1,3000));
    dID=0;
    with open("1.txt") as f:
        for i,line in enumerate(f):
            if i==2:
                words=line.split()
                for word in words:
                    wID = 0;
                    for j,w in enumerate(dictionary):
                        if w[0]==word:
                            wID=j;
                            features[dID,wID]=words.count(word)
        dID=dID+1
    result1,result2=test(features,NB,SVM);

    if result2==1:
        print("SPAM");
    else:
        print("HAM");
