import sys
from itertools import izip

def compare(file1, file2):
	total = 0
	same = 0
	with open(file1) as textfile1, open(file2) as textfile2: 
		for ln1, ln2 in izip(textfile1, textfile2):
			ln1 = (ln1.strip()).split('\t')
			ln2 = (ln2.strip()).split('\t')
			total+=1
			if ln1[2] == (ln2[2]):
				same+=1
			else:
				print ln1[1]
				print str(ln1[2]) + ' ' + str(ln2[2])
	print same/(1.0*total)

if __name__ == '__main__':
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	compare(file1, file2)