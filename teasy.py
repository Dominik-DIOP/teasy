import tkinter as tk
window = tk.Tk()


def makeWindow(width, height, title):
    window.title(str(title))
    window.geometry(str(width) + 'x' + str(height))


def textbox(x, y, w, h, command):
    e1 = tk.Entry(window, show=None, font=('Arial', 14))
    e1.place(x=x, y=x, width=w, height=h)


def loop():
    window.mainloop()
