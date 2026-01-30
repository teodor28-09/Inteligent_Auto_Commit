from tkinter import ttk, filedialog,messagebox
from tkinter import Tk
import tkinter as tk
from logic import AutoCommit

repo_path = None
INTERVAL = 1000

def on_git_select():
    global repo_path
    repo_path = filedialog.askdirectory()
    print(repo_path)
    if repo_path:
        lbl_path.config(text=repo_path)

def auto_check():
    if not repo_path:
        return

    git = AutoCommit(repo_path)
    git.auto_commit()

    root.after(INTERVAL, auto_check)

def on_start():
    if not repo_path:
        messagebox.showerror("Error", "No folder selected")
        return

    messagebox.showinfo("Started", "Auto tracking started")
    auto_check()

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

    btn_start = tk.Button(frm, text="Start Tracking", command=on_start)
    btn_start.pack(side=tk.LEFT, padx=4)

    lbl_path = tk.Label(root, text="No folder selected", wraplength=550, fg="gray")
    lbl_path.pack(pady=10)



    root.mainloop()