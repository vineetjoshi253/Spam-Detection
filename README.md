# Spam-Detection-Using-Support-Vector-Machines

A spam is a irrelevant or unsolicited message sent over the Internet, typically to a large number of users, for the purposes of advertising, phishing, spreading malware, etc. Needless to say, nobody really finds them usefull and thus their detection is quite cruicial.

In this project I have built a small spam detector using Support Vactor Machine and Bayseian Classifiers. Given below are steps undertaken to achive the task. 
<ul>
  <li><b>Preprocessing of data:</b></br> 
          Redundant words such as 'and','the','of' etc. are removed, as they will play no part in the document classification. </li>
   <li><b>Creating a dictionary of words:</b></br>
          Our goal here is to maintain the frquencies of the words, which will later be used to extract features for SVM.</li>
   <li><b>Feature extraction:</b></br>
          Feature extracion is one of the most cruicial steps in SVM. Our spam detector uses a word count vector of top 5000                         words as a feature. </li>
   <li><b>Training of SVM</b></l>
   <li><b>Testing</b></li>
 </ul>
 
<b>Result:</b>
 The system gave an overall accuracy of 96.18% with a dataset having 702 messages in training set (352 SPAM & 351 Non-Spam) and 260 messages in testing set.

<b>Resources and Reading Materials</b>
<ul>
 <li>https://ieeexplore.ieee.org/document/7282294/</li>
 <li>https://www.ijariit.com/manuscripts/v3i3/V3I3-1608.pdf</li>
 <li>https://machinelearningmastery.com/prepare-text-data-machine-learning-scikit-learn/</li>
  
