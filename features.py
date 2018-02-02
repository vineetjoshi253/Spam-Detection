import os
import numpy as np
#Function to extract features from the training set.
def features_const(train_path,dictionary):
    files=[os.path.join(train_path,f) for f in os.listdir(train_path)];
    features=np.zeros((len(files),3000))
    dID=0;
    for fil in files:
        with open(fil) as f:
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

    return features;
