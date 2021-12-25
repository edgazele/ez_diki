import tkinter as tk
from tkinter import ttk  
import csv
import codecs

# root window
root = tk.Tk()
root.geometry('800x825')
root.title('EZ English/Russian Dictionary')

style = ttk.Style(root)
style.configure('Righttab.TNotebook', tabposition='en')

# create a notebook
notebook = ttk.Notebook(root,width=500, height=820)
notebook.pack(expand=True,anchor='nw')

lists_from_csv = []
columns = ('#1', '#2')

file = codecs.open("eng_wiki2.csv","r","utf-8") 
csv_reader = csv. reader(file)

for row in csv_reader:
    lists_from_csv.append(row)

tree = ttk.Treeview(notebook, columns=columns, show='')
tree.column("# 1",width=200)
tree.column("# 2",width=300)

# adding data to the treeview
for words in lists_from_csv:
    tree.insert('', tk.END, values=words)
    tree.pack(fill='both',expand=True)
    
entry = tk.Entry(root)
entry.pack(pady=200)

root.mainloop()
