import os
from collections import Counter

#Function to make a dictionary of words from the given dataset. 
def dictionary_const(train_path):
    emails=[os.path.join(train_path,f) for f in os.listdir(train_path)]
    wordset = []
    for mail in emails:
        with open(mail) as m:
            for i,line in enumerate(m):
                if i==2:
                    words=line.split();
                    wordset=wordset + words;
    dictionary = Counter(wordset);
    
    #Removing non words and non frequent elements.
    remove=list(dictionary.keys());
    
    for item in remove:
        if item.isalpha()==False:
            del dictionary[item];
        elif len(item)==1:
            del dictionary[item];

    dictionary=dictionary.most_common(3000);
    return dictionary;
    
    
