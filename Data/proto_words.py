import nltk
import string
def getProtowords(readdir):
	yestweets  = []
	notweets = []
	unktweets = []
	with open(readdir, 'r') as inpt:
		for status in inpt:
			status = status.strip()
			username, tweet, classification = status.split('\t')
			if classification == 'y':
				yestweets += tweet.lower().split()
			elif classification == 'n':
				notweets += tweet.lower().split()
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
		if countinclass > 1:
			countoutclass = alternativeclasstweets.count(word) + unktweets.count(word)
	
			score = countinclass*1.0 /(countinclass+countoutclass)
			tuplewordscores.append((score, word))
	return tuplewordscores

if __name__ == '__main__':
	getProtowords('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt')
	


