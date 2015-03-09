import sys
import os
def readintweets(readdir, writedir):
	os.system('cls' if os.name == 'nt' else 'clear')
	filelength = file_len(writedir)
	count = filelength 
	prevuser = ''
	prevtweet = ''
	repeat = 1
	#y is yes, n is no u is unknown/undetermined
	with open(readdir, 'r') as inpt, open(writedir, 'a+') as outpt:
		#filelength = sum(1 for line in outpt)
		for number, line in enumerate(inpt):
			if number < filelength:
				outpt.flush()
			else:
				count += 1
				username, tweet = line.split('\t')
				if prevuser == '':
					prevuser = username.strip()
					prevtweet = tweet.strip()
				elif prevuser == username:
					print prevtweet + '\n'
					prevtweet = tweet.strip()
					prevuser = username.strip()
					repeat +=1
				else:
					print prevtweet + '\n'
					var = getinput()
					for x in range(0,repeat):
						outpt.write(prevuser.strip() + '\t'+prevtweet.strip() +'\t'+ var.strip() + '\n')
						outpt.flush()
					prevtweet = tweet.strip()
					prevuser = username.strip()
					os.system('cls' if os.name == 'nt' else 'clear')
					print 'Tweet Number: ' + str(count) + '\n'
					repeat = 1
		print prevtweet
		var = getinput()
		for x in range(0,repeat):
			outpt.write(prevuser.strip() + '\t'+prevtweet.strip() +'\t'+ var.strip() + '\n')
			outpt.flush()
				

def file_len(fname):
	try:
		num_lines = sum(1 for line in open(fname, 'r'))
	except IOError: 
		f = open(fname, 'a+')
		f.close()
		num_lines = 0
	return num_lines

def getinput():
	allowableInput = ['y','n','u']
	while True:
		var = raw_input("Please classify as y, n or u: ")
		if var == 'q':
			sys.exit(0)
		elif var not in allowableInput:
			print 'Not allowable input'
		else:
			return var

if __name__ == '__main__':
	readintweets(test.txt, 'outtest.txt')
