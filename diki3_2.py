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
notebook = ttk.Notebook(root,style='Righttab.TNotebook')
notebook.pack(pady=10,expand=True,anchor='nw')
##########################################################################
# create frames and add frames to notebook
frame = []
show_page = 1
for i in range(0,show_page+1):
    frame.append(i)

    frame[i] = ttk.Frame(notebook, width=500, height=820)
#    frame2 = ttk.Frame(notebook, width=500, height=820)
#    frame3 = ttk.Frame(notebook, width=500, height=820)

    frame[i].pack(fill='both', expand=True)
#    frame2.pack(fill='both', expand=True)
#    frame3.pack(fill='both', expand=True)

    notebook.add(frame[i],text=i)
    notebook.hide(frame[i])
#    notebook.add(frame2, text='2')
#    notebook.add(frame3, text='3')
############################################################################
notebook.add(frame[show_page],text=show_page)

# columns
columns = ('#1', '#2','#3')

tree = ttk.Treeview(frame[1], columns=columns, show='')
tree.column("# 1",width=200)
tree.column("# 2",width=150)
tree.column("# 3",width=300)

file = codecs.open("eng_wiki2.csv","r","utf-8") 
csv_reader = csv. reader(file)
lists_from_csv = []

n=0
for row in csv_reader:
    lists_from_csv.append(row)
    n=n+1

# adding data to the treeview
for words in lists_from_csv:
    tree.insert('', tk.END, values=words)

tree.pack(fill='both',expand=True)


root.mainloop()
