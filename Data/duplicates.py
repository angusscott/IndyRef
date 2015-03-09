

def dups(readdir):
	dic = {}
	with open(readdir, 'r') as inpt:
		for line in inpt:
			username = line.split('\t')[0]
			try:
				dic[username] +=1
			except KeyError:
				dic[username] = 1

		for x in dic:
			if dic[x]>1:
				print x + ' ' + str(dic[x])
				

if __name__ == '__main__':
	dups('indyRef-tweets-18th-Sept-2014-classified.txt')

