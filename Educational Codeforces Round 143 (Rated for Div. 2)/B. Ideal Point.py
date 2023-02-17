# 2023/02/17 Greedy
# https://codeforces.com/contest/1795/problem/B
t = int(input())
for _ in range(t):
	n, k = map(int,input().split())
	s = 0
	e = 0
	for _ in range(n):
		l, r = map(int,input().split())
		# 해당 값과 k가 같으면 +1
		if l == k:
			s += 1
		if r == k:
			e += 1
	# 하나씩 더해졌었다면 YES 출력
	if s > 0 and e > 0:
		print("YES")
	else:
		print("NO")