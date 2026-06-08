import tkinter as tk

# 円のクラス
class Circle():
  # コンストラクタ
  def __init__(self, x, y, dx, dy, color):
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
    self.color = color
    self.one_before = None

  # 円の移動関数
  def move(self, canvas):
  # 円の描画
    if self.one_before != None:
      canvas.delete(self.one_before)

    self.x = self.x + self.dx
    self.y = self.y + self.dy

    self.one_before = canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20,
    fill = self.color, width = 0)
 
    # 画面端にたどり着いたら向きを変える仕組み x軸
    if self.x >= canvas.winfo_width():
      self.dx = -1
    elif self.x <= 0:
      self.dx = 1
    # 画面端にたどり着いたら向きを変える仕組み y軸
    if self.y >= canvas.winfo_height():
      self.dy = -1
    elif self.y <= 0:
      self.dy = 1

# 円のインスタンスをリスト管理
circles = [
  Circle(400, 300, 1, 1, "red"),
  Circle(200, 100, -1, 1, "blue"),
  Circle(300, 200, 1, -1, "green"),
  Circle(100, 100, -1, -1, "yellow"),
  Circle(150, 150, 1, -1, "orange"),
  Circle(400, 400, -1, 1, "#C77EB5")
]

# ループさせる関数
def loop():
  for circle in circles:
    circle.move(canvas)

  root.after(20, loop)

# ウインドウ作成
root = tk.Tk()
root.geometry("600x400")

# キャンバス作成
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

# canvas作成時のイベントを定義
root.after(10, loop)
root.mainloop()
