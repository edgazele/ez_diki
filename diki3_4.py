import tkinter as tk
from tkinter import ttk  
import csv
import codecs

# root window
root = tk.Tk()
root.geometry('800x825')
root.title('EZ English/Russian Dictionary')

# global variables

lists_from_csv = []

# loading dictionary from the file

file = codecs.open("eng_wiki2.csv","r","utf-8") 
csv_reader = csv. reader(file)

for row in csv_reader:
    lists_from_csv.append(row)
    
# some styles

style = ttk.Style(root)
style.configure('Righttab.TNotebook', tabposition='en')

# create a notebook
notebook = ttk.Notebook(root,style='Righttab.TNotebook',width=500, height=820)
notebook.pack(expand=True,anchor='nw')

# create a frame

frame = ttk.Frame(notebook)
frame.pack(fill='both', expand=True)
notebook.add(frame,text='1')

# create a tree

columns = ('#1', '#2')

tree = ttk.Treeview(frame, columns=columns, show='')
tree.column("# 1",width=200)
tree.column("# 2",width=300)

# adding data to the treeview
for words in lists_from_csv:
    tree.insert('', tk.END, values=words)
    tree.pack(fill='both',expand=True)
    
# GUI elements

number_of_pages = len(lists_from_csv)%40
print(number_of_pages)
label = ttk.Label(root,text='Total number of pages:')
label.place(x=550, y=1)

entry = tk.Entry(root)
entry.place(x=550, y=50)

root.mainloop()
