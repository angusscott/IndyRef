from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.cross_validation import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
def importData(datadirectory):
	categories = ['n','u', 'y']

	data = load_files(datadirectory,categories=categories, shuffle=True, random_state=42, encoding='utf-8') 

	X_train, X_test, y_train, y_test = cross_validation.train_test_split(data.data, data.target, test_size = 0.4, random_state=0)
	# count_vect = CountVectorizer()
	# X_train_vec = count_vect.fit_transform(X_train)
	# X_test_vec = count_vect.fit_transform(X_test)
	# clf = svm.SVC(kernel='linear', C=1).fit(X_train_vec, y_train)
	# clf.score(X_test_vec, y_test) 

	text_clf = Pipeline([('vect', TfidfVectorizer()), ('clf', MultinomialNB())])
	print text_clf.named_steps['clf']
	print str(cross_val_score(text_clf, data.data,data.target )) + ' Tfidf NB'
	#array([ 0.62376238,  0.57      ,  0.6122449 ])
	text_clf = Pipeline([('vect', CountVectorizer()),('clf', MultinomialNB()),]) 
	print str(cross_val_score(text_clf, data.data,data.target )) + ' CountVec NB'                                         #array([ 0.56435644,  0.5       ,  0.57142857])
	clf = Pipeline([('vect', CountVectorizer()), ('svm', LinearSVC())])                        
	print str(cross_val_score(clf, data.data,data.target )) + ' CountVec SVM'
	#array([ 0.55445545,  0.48      ,  0.54081633])
	clf = Pipeline([('vect', TfidfVectorizer()), ('svm', LinearSVC())])                    
	print str(cross_val_score(clf, data.data,data.target )) + ' Tfidf SVM'
	#array([ 0.62376238,  0.57      ,  0.6122449 ])

if __name__ == '__main__':
	print 'Hashtags'
	importData('/Users/angusscott/University/4thyear/4th Year Project/Data/UsersHashtags/')
	print 'Tweets'
	importData('/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweetsClass/') 