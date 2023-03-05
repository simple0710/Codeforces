# 2023/03/03 Greedy
# https://codeforces.com/contest/1800/problem/D
for _ in range(int(input())):
  N = int(input())
  word = input()
  res = 0
  for i in range(1, len(word)-1):
    res += word[i-1] != word[i+1]
  # 정답 출력
  print(res+1)