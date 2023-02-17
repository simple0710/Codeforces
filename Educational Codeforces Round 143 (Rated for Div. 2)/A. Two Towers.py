# 2023/02/17 Brute Force
# https://codeforces.com/contest/1795/problem/A
T = int(input())

def check(a, b): # 해당 배열이 올바르게 구성 됐는지 확인한다.
  for i in range(len(a)-1):
    if a[i] == a[i+1]:
      return False
  for i in range(len(b)-1):
    if b[i] == b[i+1]:
      return False
  return True

for _ in range(T):
  N1, N2 = map(int,input().split())
  arr1 = list(input())
  arr2 = list(input())
  ans1 = False
  ans2 = False
  # 한쪽에 블록을 최대한 몰아본 후 확인해본다.
  while len(arr2) > 1 and arr1[-1] != arr2[-1]:
    arr1.append(arr2.pop())
  ans1 = check(arr1, arr2)

  while len(arr1) > 1 and arr2[-1] != arr1[-1]:
    arr2.append(arr1.pop())
  ans2 = check(arr1, arr2)
  # ans1과 ans2 중에 하나라도 True인 경우 YES 출력
  if ans1 or ans2: 
    print("YES")
  else:
    print("NO")

# 다른 사람 풀이
"""
for _ in range(int(input())):
  a,b = map(int,input().split())
  s = input()+input()[::-1]
  x = False
  for i in range(a+b-1):
    if s[i]==s[i+1]:
      if x == True:
        print("NO")
        break
      x = True
  else:
    print("YES")
"""
