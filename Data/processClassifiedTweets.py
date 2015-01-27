from nltk.corpus import stopwords
import itertools
from math import log
stop = stopwords.words('english')
stop.remove('no')
stop = stop + ['#indyref','rt']

def processClassifiedTweets(readdir, writediryes, writedirno):
	with open(readdir, 'r') as inpt, open(writediryes, 'w') as output_yes, open(writedirno, 'w')as output_no:
		for line in inpt:
			if line.split()[-1] == 'y':
				tweet = line.split('\t')[1].strip().lower().split()
				tweet = ' '.join([word for word in tweet if word not in stop])
				output_yes.write( tweet + '\n')
			elif line.split()[-1] == 'n':
				tweet = line.split('\t')[1].strip().lower().split()
				tweet = ' '.join([word for word in tweet if word not in stop])
				output_no.write( tweet + '\n')
			else:
				pass

def processClassifiedTweetsUsers(readdir, writediryes, writedirno):
	with open(readdir, 'r') as inpt, open(writediryes, 'w') as output_yes, open(writedirno, 'w')as output_no:
		for line in inpt:
			if line.split()[-1] == 'y':
				tweet = line.split('\t')[0].strip()
				output_yes.write( tweet + '\n')
			elif line.split()[-1] == 'n':
				tweet = line.split('\t')[0].strip()
				output_no.write( tweet + '\n')
			else:
				pass


def phraseoverlap(yestweetsdir, notweetsdir):
	with open(yestweetsdir, 'r') as yes_inpt, open(notweetsdir, 'r') as no_inpt:
		key_words = []
		yes_tweets = []
		no_tweets = []
		for line in yes_inpt:
			yes_tweets.append(line.split())
		for line in no_inpt:
			no_tweets.append(line.split())

		numberofyes = len(yes_tweets)
		numberofno = len(no_tweets)
		numberofvoteyesinyes = sum([1 for tweet in yes_tweets if ('#yesscotland') in tweet])
		numberofvoteyesinno = sum([1 for tweet in no_tweets if ('#yesscotland') in tweet])
		print 'Number of YES tweets: '+str(numberofyes)
		print 'Number of NO tweets: '+str(numberofno)
		print 'Number of #voteyes in YES tweets: ' + str(numberofvoteyesinyes)
		print 'Number of #voteyes in NO tweets: ' + str(numberofvoteyesinno)

# def dicecoefficient(docs):
# 	synonymscountstuples = {}
# 	synonymscountsindiv = {}
# 	for doc in docs:
# 		for st, nd in itertools.combinations(doc, 2)
# 			try:
# 				synonyms[(st, nd)] = synonyms[(st, nd)] +1
# 			except KeyError:
# 				try:
# 					synonyms[(nd, st)] = synonyms[(nd, st)] +1
# 				except KeyError:
# 					synonyms[(st, nd)] = 1

# 	synonyms = {}
# 	for tupl in synonymscounts:

# if __name__ == '__main__':
	# processClassifiedTweets('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-yes.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-no.txt')
	# phraseoverlap('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-yes.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-no.txt')
	# processClassifiedTweetsUsers('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-yes-users.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-no-users.txt')
