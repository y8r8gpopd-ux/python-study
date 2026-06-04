import random

a = []
for i in range(4):
  a.append(random.randint(0, 9))

print(a)

while True:
  check_4 = False
  while check_4 == False:
    b = input("4桁の数字を入力してね＞")
    if len(b) != 4:
      print("「4桁」の数字を入力してください！")
    else:
      check_int = True
      for i in range(4):
        if (b[i] < "0") or (b[i] > "9"):
          check_int = False
          print("「数字」で入力してください！")
          break
      if check_int == True:
        check_4 = True
      
  hit = 0

  for i in range(4):
    if a[i] == int(b[i]):
      hit += 1

  blow = 0

  for i in range(4):
    if b[i] in b[0:i]:
        continue

    for j in range(4):
      
      if (int(b[i]) == int(a[j])) and (a[j] != int(b[j])):
        blow += 1
        break

  print(f"ヒット：{hit}")
  print(f"ブロー：{blow}")

  if hit == 4:
    print ("おめでとう！")
  break
