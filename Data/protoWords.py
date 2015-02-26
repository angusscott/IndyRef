import nltk
import string
import re
import os 
import pickle


def getProtowords(invindex, usrclass):
	userclass = {}
	dirs = get_immediate_subdirectories(usrclass)
	for classif in dirs:
		print classif
		inpt = [f for f in os.listdir(usrclass+classif+'/') if os.path.isfile(os.path.join(usrclass+classif+'/',f))]
		for user in inpt:
			userclass[user] = classif

	invertedindex = pickle.load(open(invindex, 'rb'))
	y = []
	n = []
	u = []
	for classif in dirs:
		for word in invertedindex:
			print word
			if word[0] != '@':
				if len(invertedindex[word]) > 20:
					score = sum([1 for x in invertedindex[word] if userclass[x.split('/')[-1]] == classif])/(1.0*len(invertedindex[word]))
					eval(classif).append((word, score))
				else:
					pass
			else:
				pass
		

	yesprotoscores = sorted(y, key=lambda tupl:tupl[1], reverse = True)[:100]
	noprotoscores = sorted(n, key=lambda tupl:tupl[1], reverse = True)[:100]
	unkprotoscores = sorted(u, key=lambda tupl:tupl[1], reverse = True)[:100]
	print yesprotoscores
	print '\n' + '\n'
	print noprotoscores
	print '\n' + '\n'
	print unkprotoscores
def getProtoscores(classtweets, alternativeclasstweets, unktweets):
	tuplewordscores = []
	for word in list(set(classtweets)):
		countinclass = classtweets.count(word)
		if countinclass > 5:
			countoutclass = alternativeclasstweets.count(word) + unktweets.count(word)
	
			score = countinclass*1.0 /(countinclass+countoutclass)
			tuplewordscores.append((score, word))
	return tuplewordscores


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

if __name__ == '__main__':
	getProtowords('/Users/angusscott/University/4thyear/4th Year Project/Data/tweetindex.p','/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweetsClass/' )
	


