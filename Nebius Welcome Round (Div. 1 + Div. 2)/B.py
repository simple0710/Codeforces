# 2023/03/13 Greedy
# https://codeforces.com/contest/1804/problem/B
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  # 환자, 팩 용량, 백신 수명, 최대 기다리는 순간
  n, k, d, w = map(int,input().split())
  arr = list(map(int,input().split()))
  s = k # 현재 용량
  op = arr[0] # 개봉한 시점
  res = 1
  for p in arr:
    # 팩이 남았고, 팩을 개봉한 시점 + 수명 >= 환자 대기 시간
    if s and op + d >= p - w:
      s -= 1
      continue
    # 새로운 팩 개봉
    s = k - 1
    op = p
    res += 1
  # 정답 출력
  print(res)

