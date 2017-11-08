"""
https://www.hackerearth.com/practice/algorithms/
greedy/basics-of-greedy-algorithms/practice-problems/
algorithm/minimum-flips/description/
"""

def min_count(s, k):
	l = len(s)
	if s == '1' * l:
		return 0
	out = list(s)
	count = 0
	for i in range(l-k+1):
		if out[i] == '1':
			#out = out[0:i] + '1' + out[i:]
			continue
		else:
			count += 1
			out[i:i+k] = ['0' if x == '1' else '1' for x in out[i:i+k]]

	if ''.join(out) == '1' * l:
		return count
	else:
		return -1

if __name__ == "__main__":
	t = int(input())
	for _ in range(t):
		s,k = list(map(str, input().split()))
		k = int(k)
		print(min_count(s,k))
