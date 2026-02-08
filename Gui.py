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

        git = AutoCommit(repo_path)
        branches = git.get_branches()

        branch_combo["values"] = branches
        if branches:
            branch_combo.current(0)


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
        git = AutoCommit(repo_path)

        if use_branch_var.get():
            branch = branch_var.get()
            git.checkout(branch)

        sync = git.sync()
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

def on_commit():
    if not repo_path:
        return
    message = entry.get()

    if not message:
        messagebox.showerror("Error", "No commit message entered")
        return

    git = AutoCommit(repo_path)
    committed = git.manual_commit(message)

    if committed:
        notify("Git Manual Commit", "Changes committed successfully")

if __name__ == '__main__':

    root = Tk()
    root.title("Git")
    root.geometry("600x500")

    # Global variable GUI
    branch_var = tk.StringVar()
    use_branch_var = tk.BooleanVar()

    frm = ttk.Frame(root)
    frm.pack(fill=tk.X, padx=6, pady=6)

    frm1 = ttk.Frame(root)
    frm1.pack(fill=tk.X, padx=6, pady=6)

    frm2 = ttk.Frame(root)
    frm2.pack(fill=tk.X, padx=6, pady=6)


    btn_get = tk.Button(frm, text="Select Git Folder",command = on_git_select)
    btn_get.pack(side=tk.LEFT, padx=4)

    lbl_branch = tk.Label(frm1, text="Branch:")
    lbl_branch.pack(side=tk.LEFT, padx=4)

    branch_combo = ttk.Combobox(frm1, textvariable=branch_var, state="readonly", width=25)
    branch_combo.pack(side=tk.LEFT, padx=4)

    chk_branch = tk.Checkbutton(frm1,text="Use selected branch",variable=use_branch_var)
    chk_branch.pack(side=tk.LEFT, padx=6)

    btn_start = tk.Button(frm, text="Start Tracking", command=on_button_toggle)
    btn_start.pack(side=tk.LEFT, padx=4)


    lbl_commit = tk.Label(frm2, text="Commit Message:")
    lbl_commit.pack(side=tk.LEFT, padx=4)

    entry = tk.Entry(frm2)
    entry.pack(side = tk.LEFT, padx=4)

    btn_commit = tk.Button(frm2, text="Manual Commit", command=on_commit)
    btn_commit.pack(side=tk.LEFT, padx=4)

    lbl_path = tk.Label(frm, text="No folder selected", wraplength=550, fg="gray")
    lbl_path.pack(pady=10)

    lbl_status = tk.Label(frm, text="Status: Stopped", fg="red")
    lbl_status.pack(pady=5)


    root.mainloop()