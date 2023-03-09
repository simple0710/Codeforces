# 2023/03/03 구현
# https://codeforces.com/contest/1800/problem/B
from collections import defaultdict

for _ in range(int(input())):
  N, K = map(int,input().split())
  word = sorted(list(input()))
  group = defaultdict(int)
  key = set()
  for i in word: # 문자의 개수를 구한다.
    group[i] += 1
    key.add(i.upper())
  res = 0
  for i in key:
    p = chr(ord(i) + 32)
    low = min(group[p], group[i])
    if p in group.keys(): # 만약 p가 group에 있는 경우 최대 쌍의 개수를 더한다.
      res += low
      group[p] -= low
      group[i] -= low
  # K번 변하게 할 수 있으므로, 탐색 후 쌍을 더 만들어 낼 수 있다면 값을 더한다.
  for i in group.values(): 
    if i >= 2 and K: # 2개 이상이고, K의 횟수가 남아 있는 경우
      new = i // 2
      if new > K:
        res += K
        K = 0
      else:
        K -= new
        res += new
  # 정답 출력
  print(res)