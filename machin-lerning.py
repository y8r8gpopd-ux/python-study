import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import filedialog
from PIL import Image, ImageTk

# 前回の画像
before_img = None

# ファイルを開く関数
def ButtonClick():
  global before_img, pimg
  # 開く画像を指定してもらう  
  file_name = filedialog.askopenfilename(filetypes = [("jpgファイル", "*.jpg"), ("pngファイル", "*.png")])
  
  if file_name:
    # 前回の画像があれば削除
    if before_img != None:
      canvas.delete(before_img)

    # 画像読み込み
    img = Image.open(file_name)
    # PhotoImage形式に変換
    pimg = ImageTk.PhotoImage(img)
    # キャンバスに表示
    before_img = canvas.create_image(0, 0, anchor = tk.NW, image = pimg)


# ウインドウ作成
root = tk.Tk()
root.geometry("1024x1024")

# キャンバス作成
canvas = tk.Canvas(root, width = 1024, height = 1024, bg = "white")
canvas.place(x = 0, y = 0)

# ボタン作成
open_button = tk.Button(root, text = "ファイルを開く", font = ("Helvetica", 14), command = ButtonClick)
open_button.place(x = 30, y = 900)

root.mainloop()