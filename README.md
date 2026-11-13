# treeview-demo

A tiny `ttk.Treeview` tour — the third widget the [cleanroom coverage audit](https://github.com/amanvicky/cleanroom) named as its top blocker (5 of the 20 most-starred tkinter repos use it; the call-site dump that scoped the widget is in the sprint commit).

Two trees, the two shapes the corpus uses:

- **a `show="headings"` table** — `heading()`/`column()` titles, widths and anchors; `insert()` adds rows, a row click updates the widget's real selection state, `selection()`/`item()` answer it (including the Dvlv shape `item(tree.selection())`), `item(iid, values=...)` edits in place, `delete(*sel)` removes;
- **a default tree-mode outline** — the `#0` column, `parent=` hierarchies, `open=` items, and a ▸/▾ toggle that expands and collapses (double-click works too).

The honest line: `<<TreeviewSelect>>` callbacks stay outside the subset — `bind()` is counted, as the audit's own table says. Selection *state* is real; the click *callback* is not.

Runs as-is in [cleanroom](https://amanvicky.github.io/cleanroom/) (open the shelf and pick **treeview-demo** — both trees render live in the app screen) and on a real PC:

```
python treeview_demo.py     # needs Tk — ships with the standard Python installer
```
