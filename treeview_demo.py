"""A tiny ttk.Treeview tour — the third widget the cleanroom audit named and
shipped. Runs in cleanroom's virtual tkinter and on a real PC
(python treeview_demo.py).

Two trees, the two shapes the corpus uses:
1. a `show="headings"` table — columns, heading()/column() titles and widths,
   insert()/item()/delete() driven by buttons, selection() answering real
   iids after a row click;
2. a default tree-mode outline — the #0 column, parent= hierarchies, open=
   items, click the ▸/▾ toggle to expand and collapse.
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("treeview demo")
root.geometry("560x360")

# 1 — a headings table (the Dvlv/YEDDA shape)
cols = ("name", "done", "time")
tree = ttk.Treeview(root, columns=cols, show="headings", height=6)
tree.heading("name", text="task", anchor="w")
tree.heading("done", text="done?", anchor="center")
tree.heading("time", text="pomodoros", anchor="center")
tree.column("name", width=260, anchor="w")
tree.column("done", width=80, anchor="center")
tree.column("time", width=110, anchor="center")
tree.pack(fill="x", padx=10, pady=(10, 4))

status = tk.Label(root, text="click a row, then act on the selection")
status.pack()


def refresh_status():
    sel = tree.selection()
    if sel:
        item = tree.item(sel[0])
        status.config(text="selected: " + str(item["values"][0]) +
                      " (iid " + str(sel[0]) + ")")
    else:
        status.config(text="nothing selected — click a row")


n = {"i": 0}


def add():
    n["i"] += 1
    tree.insert("", "end", values=("task %d from the button" % n["i"], "no", "0:00"))
    refresh_status()


def mark_done():
    sel = tree.selection()
    if not sel:
        status.config(text="nothing selected — click a row first")
        return
    values = list(tree.item(sel[0], "values"))
    values[1] = "yes"
    tree.item(sel[0], values=values)          # the PySimpleGUI update shape
    refresh_status()


def remove():
    sel = tree.selection()
    if not sel:
        status.config(text="nothing selected — click a row first")
        return
    tree.delete(*sel)
    refresh_status()


row = tk.Frame(root)
row.pack(pady=2)
tk.Button(row, text="insert() a task", command=add).pack(side="left", padx=4)
tk.Button(row, text="item() mark done", command=mark_done).pack(side="left", padx=4)
tk.Button(row, text="delete() selected", command=remove).pack(side="left", padx=4)

for name, done_flag, spent in [("plan the sprint", "no", "1:00"),
                               ("ship the widget", "no", "0:00"),
                               ("verify in cleanroom", "no", "0:00")]:
    tree.insert("", "end", values=(name, done_flag, spent))

# 2 — a tree-mode outline (the pygubu shape: parent=, open=, #0)
outline = ttk.Treeview(root, height=5)
plan = outline.insert("", "end", text="sprint plan", open=True)
outline.insert(plan, "end", text="the audit names the blocker")
sub = outline.insert(plan, "end", text="ship ttk.Treeview", open=True)
outline.insert(sub, "end", text="shim: insert/heading/column/selection/item")
outline.insert(sub, "end", text="renderer: a real table with an outline column")
outline.insert("", "end", text="next: the table decides again")
outline.pack(fill="x", padx=10, pady=(8, 6))

root.mainloop()
