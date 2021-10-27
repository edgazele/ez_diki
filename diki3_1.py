# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:48:10 2021

@author: edzel
"""

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


#      self.buttonForget = tk.Button(self.root,
#                          text = 'Click to hide Label',
#                          command=lambda: self.label.pack_forget())
hide_rows_button = tk.Button(root, text ="Hello")

# create a notebook
notebook = ttk.Notebook(root,style='Righttab.TNotebook')
notebook.pack(pady=10,expand=True,anchor='nw')

# create frames
frame1 = ttk.Frame(notebook, width=500, height=820)
frame2 = ttk.Frame(notebook, width=500, height=820)
frame3 = ttk.Frame(notebook, width=500, height=820)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='1')
notebook.add(frame2, text='2')
notebook.add(frame3, text='3')

# columns
columns = ('#1', '#2','#3')


tree = ttk.Treeview(frame1, columns=columns, show='')
tree.column("# 1",width=200)
tree.column("# 2",width=150)
tree.column("# 3",width=300)

file = codecs.open("eng_wiki2.csv","r","utf-8") 
csv_reader = csv. reader(file)
lists_from_csv = []

n=0
for row in csv_reader:
    lists_from_csv.append(row)
    print(lists_from_csv[n])
    n=n+1

# adding data to the treeview
for words in lists_from_csv:
    tree.insert('', tk.END, values=words)

tree.pack(fill='both',expand=True)
hide_rows_button.pack(anchor='ne')

root.mainloop()
