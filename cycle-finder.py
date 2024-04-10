from collections import defaultdict

idx = defaultdict(lambda :-1)
n = 1
i = 0
while 1:
	i += 1
	n = int(str(2*n).replace('00', ''))
	if idx[n] != -1:
		print(f"cycle found!!! Period: {i-idx[n]}, Starts with {n} at n={i}")
		break
	idx[n] = i
	if i % 10000000 == 0:
		print(f"the program has been running for {i} iterations and no cycle has been found so far")
