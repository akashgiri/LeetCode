"""
https://www.hackerearth.com/zh/practice/algorithms/greedy/
basics-of-greedy-algorithms/practice-problems/algorithm/
mathison-and-the-funny-substring-b3f58587/
"""
from collections import Counter

def fun_count(a):
	if len(set(a)) == len(a):
		return 1
	lc = 0
	d = {}
	for i,v in enumerate(a):
		if v in d:
			#print("inside if")
			d[v][1] = a.index(v, max(d[v][0],d[v][1])+1)
			if d[v][1] - d[v][0] + 1 > lc:
				lc = d[v][1] - d[v][0] + 1
		else:
			d[v] = [a.index(v), -1]

	#print(d)
	return lc

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	print(fun_count(a))

"""
def fun_count(a):
	s = sorted(a)
	c = Counter(a)
	lc = 0
	d = {}
	for i,v in enumerate(s):
		if c[v] < 2:
			continue
		else:
			if v in d:
				#print("inside if")
				d[v][1] = a.index(v, max(d[v][0],d[v][1])+1)
			else:
				d[v] = [a.index(v), -1]

	for i,v in d.items():
		if d[i][1] - d[i][0] + 1 > lc:
			lc = d[i][1] - d[i][0] + 1

	#print(d)

	return lc

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	print(fun_count(a))
"""