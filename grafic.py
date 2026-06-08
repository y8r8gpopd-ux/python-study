import tkinter as tk

# 円を辞書で管理
circles = [
  {"x": 400, "y": 300, "one_before": None, "dx": 1, "dy": 1, "color": "red"},
  {"x": 200, "y": 100, "one_before": None, "dx": -1, "dy": 1, "color": "green"},
  {"x": 100, "y": 200, "one_before": None, "dx": 1, "dy": -1, "color": "blue"}
]

def move():
  # 関数外から読み込み
  global circles

  # 各円の描画
  for circle in circles:
    if circle["one_before"] != None:
      canvas.delete(circle["one_before"])

    circle["x"] = circle["x"] + circle["dx"]
    circle["y"] = circle["y"] + circle["dy"]

    circle["one_before"]= canvas.create_oval(circle["x"] - 20, circle["y"] - 20, circle["x"] + 20, circle["y"] + 20,
    fill = circle["color"], width = 0)
 
    # 画面端にたどり着いたら向きを変える仕組み x軸
    if circle["x"] >= canvas.winfo_width():
      circle["dx"] = -1
    elif circle["x"] <= 0:
      circle["dx"] = 1
    # 画面端にたどり着いたら向きを変える仕組み y軸
    if circle["y"] >= canvas.winfo_height():
      circle["dy"] = -1
    elif circle["y"] <= 0:
      circle["dy"] = 1

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
