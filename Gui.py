from tkinter import ttk, filedialog,messagebox
from tkinter import Tk
import tkinter as tk

from logic import notify
from logic import AutoCommit

repo_path = None
flag = False
after_id = None
INTERVAL = 1000

def on_git_select():
    global repo_path
    repo_path = filedialog.askdirectory()
    #label for path
    if repo_path:
        lbl_path.config(text=repo_path)

def auto_check():
    global after_id
    if not repo_path:
        return

    git = AutoCommit(repo_path)
    committed = git.auto_commit()

    if committed:
        notify("Git Auto Commit", "Changes committed successfully")

    after_id = root.after(INTERVAL, auto_check)

def on_button_toggle():
    global flag,after_id

    if not repo_path:
        messagebox.showerror("Error", "No folder selected")
        return

    if not flag:#start
        flag = True
        btn_start.config(text="Stop Tracking")
        lbl_status.config(text="Status: Tracking", fg="green")
        auto_check()
    else:
        flag = False

        if after_id:
            root.after_cancel(after_id) #closing the cycle
            after_id = None
        btn_start.config(text="Start Tracking")
        lbl_status.config(text="Status: Stopped", fg="red")

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

    btn_start = tk.Button(frm, text="Start Tracking", command=on_button_toggle)
    btn_start.pack(side=tk.LEFT, padx=4)

    lbl_path = tk.Label(root, text="No folder selected", wraplength=550, fg="gray")
    lbl_path.pack(pady=10)

    lbl_status = tk.Label(root, text="Status: Stopped", fg="red")
    lbl_status.pack(pady=5)



    root.mainloop()