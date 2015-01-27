import nltk
import string
import re
def getProtowords(readdir):
	yestweets  = []
	notweets = []
	unktweets = []
	with open(readdir, 'r') as inpt:
		for status in inpt:
			status = status.strip()
			username, tweet, classification = status.split('\t')
			tweet = tweet.lower()
			tweet = re.sub(r'(?![A-Za-z0-9#\s]).', ' ',tweet)
			if classification == 'y':
				yestweets += tweet.split()
			elif classification == 'n':
				notweets += tweet.split()
			else:
				unktweets += tweet.lower().split()
	yesprotoscores = sorted(getProtoscores(yestweets, notweets, unktweets), key=lambda tupl:tupl[0], reverse = True)[:100]
	noprotoscores = sorted(getProtoscores(notweets, yestweets, unktweets), key=lambda tupl:tupl[0], reverse = True)[:100]
	print yesprotoscores
	print '\n' + '\n'
	print noprotoscores

def getProtoscores(classtweets, alternativeclasstweets, unktweets):
	tuplewordscores = []
	for word in list(set(classtweets)):
		countinclass = classtweets.count(word)
		if countinclass > 2:
			countoutclass = alternativeclasstweets.count(word) + unktweets.count(word)
	
			score = countinclass*1.0 /(countinclass+countoutclass)
			tuplewordscores.append((score, word))
	return tuplewordscores

if __name__ == '__main__':
	getProtowords('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt')
	


