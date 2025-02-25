import tkinter as tk
from tkinter import font

root = tk.Tk()
fonts = list(font.families())

for f in fonts:
    print(f)

root.destroy()
