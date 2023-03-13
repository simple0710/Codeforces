# 2023/03/09 Implementation
# https://codeforces.com/contest/1802/problem/A
for _ in range(int(input())):
  N = int(input())
  arr = sorted(list(map(int,input().split())))
  marr = []
  # 음수를 marr에 저장한다.
  while arr[0] < 0:
    marr.append(arr.pop(0))
  # 공차가 1인 등차수열 배열을 생성한다.
  p = list(range(1, len(arr) + 1))
  # 가장 큰 배열이 되려면 p 다음에 수가 내려가야 한다.
  max_arr = p + list(range(max(p) - 1, -1, -1))
  # 가장 작은 배열이 되려면 음수와 번갈아가며 나오다가 p가 나와야 한다.
  min_arr = [1, 0] * len(marr) + list(range(1, len(arr) + 1 - len(marr)))

  # 범위를 N - 1까지만 하고 각각의 정답을 출력한다.
  print(' '.join(map(str, max_arr[:N])))
  print(' '.join(map(str, min_arr[:N])))