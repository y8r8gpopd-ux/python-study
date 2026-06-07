import tkinter as tk

# ひとつ前の円をフラグで管理
circle = None

x = 400
y = 300

dx = 1
dy = 1

# クリックした場所に円の作成
def move():
  # 関数外から読み込み
  global circle, x, y, dx, dy

  # 描画した円が残っていたら削除
  if circle != None:
    canvas.delete(circle)
  
  # 座標を移動させるdx,dy
  x += dx
  y += dy

  # 円の描画
  circle = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "red", width = 0)

  # 画面端にたどり着いたら向きを変える仕組み x軸
  if x >= canvas.winfo_width():
    dx = -1
  elif x <= 0:
    dx = 1
  # 画面端にたどり着いたら向きを変える仕組み y軸
  if y >= canvas.winfo_height():
    dy = -1
  elif y <= 0:
    dy = 1

  # move関数繰り返し
  root.after(20, move)


  
# ウインドウ作成
root = tk.Tk()
root.geometry("600x400")

# キャンバス作成
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

# canvasにクリック時のイベントを定義
root.after(10, move)
root.mainloop()
