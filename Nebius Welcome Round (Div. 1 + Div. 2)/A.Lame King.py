# 2023/03/13 Math
# https://codeforces.com/contest/1804/problem/A
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  a, b = map(int,input().split())
  a = abs(a)
  b = abs(b)
  # 대각선으로 움직인다.
  fm = min(abs(a), abs(b))
  a -= fm
  b -= fm
  # 자리에 머무르면서 해당 구역으로 이동한다.
  check = max(a, b) * 2 - 1 
  if a + b == 0: # 더 이동하지 않아도 된다면 check는 0으로 한다.
    check = 0
  # 정답 출력
  print(fm * 2 + check)