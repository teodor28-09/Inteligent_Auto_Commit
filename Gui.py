from tkinter import ttk, filedialog
from tkinter import Tk
import tkinter as tk
from logic import AutoCommit


def on_git_select():
    filepath = filedialog.askdirectory()
    print(filepath)

if __name__ == '__main__':

    root = Tk()
    root.title("Git")
    root.geometry("600x500")

    frm = ttk.Frame(root)
    frm.pack(fill=tk.X, padx=6, pady=6)

    #entry = tk.Entry(root)
    #entry.pack(padx=10, pady=10)

    btn_get = tk.Button(frm, text="Select Git Folder",command = on_git_select)
    btn_get.pack(side=tk.LEFT, padx=4)


    root.mainloop()