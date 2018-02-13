# Spam-Detection-Using-Support-Vector-Machines

A spam is a irrelevant or unsolicited message sent over the Internet, typically to a large number of users, for the purposes of advertising, phishing, spreading malware, etc. Needless to say, nobody really finds them usefull and thus their detection is quite cruicial.

In this project I have built a small spam detector using Support Vactor Machine and Bayseian Classifiers. Given below are steps undertaken to achive the task. 
<ul>
  <li><b>Preprocessing of data:</b></br> 
          Redundant words such as 'and','the','of' etc. are removed, as they will play no part in the document classification. </li>
   <li><b>Creating a dictionary of words:</b></br>
          Our goal here is to maintain the frquencies of the words, which will later be used as a feature for SVM.</li>
   <li><b>Feature extraction:</b></br>
          Feature extracion is one of the most cruicial steps in SVM. Our spam detector uses a word count vector of top 5000                         words as a feature. </li>
   <li><b>Training of SVM</b></li>
   <li><b>Testing</b></li>
   
 </ul>
