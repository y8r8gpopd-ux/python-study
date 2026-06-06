# モジュールのインポート
import random
import tkinter as tk
import tkinter.messagebox as tkm


# ボタンが押された時の処理
def ButtonClick():
  b = input_box.get()
  
  # ゲーム部分
  # 正しく入力してもらうまでループ
  check_4 = False

  # check_4というフラグで「4桁」かチェック
  while check_4 == False:
    if len(b) != 4:
      tkm.showinfo("無効", "「4桁」の数字を入力してください！")
    else:

      # 4桁なら数字(0~9)かをチェック
      check_int = True
      for i in range(4):
        # 1文字ずつチェック
        if (b[i] < "0") or (b[i] > "9"):
          # 一文字でもアウトなら入力やり直し
          check_int = False
          tkm.showinfo("無効", "「数字」で入力してください！")
          break

      # 全部クリアで入力ループ脱出
      if check_int == True:
        check_4 = True
  
  # hitの計算
  hit = 0

  # １文字ずつhitの確認（場所まで一致）
  for i in range(4):
    if a[i] == int(b[i]):
      hit += 1

  # blowの計算
  blow = 0


  for i in range(4):
    # 重複してたら次の処理へパス
    if b[i] in b[0:i]:
        continue

    for j in range(4):
      # hit（場所まで一致）でなくかつどこかに数字が含まれているかを変数jで指定して一つずつ確認
      if (int(b[i]) == int(a[j])) and (a[j] != int(b[j])):
        blow += 1
        break

  # hitが4ならゲーム終了
  if hit == 4:
    tkm.showinfo("当たり", "おめでとうございます！")
    root.destroy()
  else:
    history.insert(tk.END, f"{b} ヒット：{hit} / ブロー：{blow} \n")

# ///////////////////////   ゲーム部分ここまで   ////////////////////////////

# 4桁の数字のランダム生成
a = []
for i in range(4):
  a.append(random.randint(0, 9))

# GUIの部分
root = tk.Tk()
root.geometry("600x400")
root.title("ヒット＆ブロー")
label_1 = tk.Label(root, text="4桁の数字を入力してね", font=("helvetica", 14))
label_1.place(x = 20, y = 20)

input_box = tk.Entry(width = 4, font=("Helvetica", 30))
input_box.place(x = 40, y = 60)

history = tk.Text(root, font=("Helevtica", 12))
history.place(x = 400, y = 0, width = 200, height = 400)

# デバッグ用答え表示
# answer = tk.Text(root)
# answer.place(x = 10, y = 350)
# answer.insert(tk.END, a)

button_1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command = ButtonClick)
button_1.place(x = 140, y = 80)
root.mainloop()
