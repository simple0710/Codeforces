# 2023/03/03 구현
# https://codeforces.com/contest/1800/problem/A
for _ in range(int(input())):
  N = int(input())
  word = input().upper() # 대문자로 값을 받는다.
  check = ['M','E', 'O', 'W']
  idx = 0
  flag = True
  for i in word:
    if i not in check: # 해당 문자가 MEOW에 속하지 않는경우
      flag = False
      break
    if idx < 3: # 문자가 이어지지 않는 경우
      if i in check[idx+1:]:
        flag = False
        break
    if idx >= 1 and i in check[:idx-1]: # 문자가 이어지지 않는 경우
      flag = False
      break
    if idx < 4 and (i == check[idx]): # 현재 위치에 맞는 알파벳이 온 경우
      idx += 1

  if idx == 4 and flag: # MEOW가 되고 flag가 False가 아니면 'YES'출력
    print('YES')
  else: # 정답이 아니면 'NO' 출력
    print("NO")