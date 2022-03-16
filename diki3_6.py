import tkinter as tk
from tkinter import ttk  
import csv
import codecs
from random import randint

# global variables

lists_from_csv = []
chunks = []

# loading dictionary from the file

file = codecs.open("eng_wiki2.csv","r","utf-8") 
csv_reader = csv. reader(file)

for row in csv_reader:
    lists_from_csv.append(row)
    
# root window
root = tk.Tk()
root.geometry('800x825')
root.title('EZ English/Russian Dictionary')

def show_page():
    global result
    result = int(entry.get())

# create a frame

    frame = ttk.Frame(notebook)
    frame.pack(fill='both', expand=True)
    notebook.add(frame,text=str(result))

# create a tree

    columns = ('#1', '#2')

    tree = ttk.Treeview(frame, columns=columns, show='')
    tree.column("# 1",width=200)
    tree.column("# 2",width=300)
 
# create a pages
    chunks = [lists_from_csv[x:x+40] for x in range(0, len(lists_from_csv), 40)]
    
    # adding data to the treeview
    for words in chunks[result-1]:
        tree.insert('', tk.END, values=words)
        tree["displaycolumns"]=('#1','#2')
        tree.pack(fill='both',expand=True)
    
# some styles

style = ttk.Style(root)
style.configure('Righttab.TNotebook', tabposition='en')

# create a notebook
notebook = ttk.Notebook(root,style='Righttab.TNotebook',width=500, height=820)
notebook.pack(expand=True,anchor='nw')

# GUI elements

total_words = len(lists_from_csv)
pages = round(total_words/39)
label_1 = ttk.Label(root,text='Number of pages:'+' '+str(pages))
label_1.place(x=550, y=1)

label_2 = ttk.Label(root,text='Show page:')
label_2.place(x=550, y=30)

entry = tk.Entry(root,width=3)
entry.place(x=550, y=50)

button = ttk.Button(root, text ="Show page", command=show_page)
button.place(x=650, y=50)

def random_page():
    global random_page
    value = randint(1, pages)
    
    label_2 = ttk.Label(root,text='Random page:'+' '+str(value))
    label_2.place(x=550, y=80)

button = ttk.Button(root, text ="Random page generator", command=random_page)
button.place(x=650, y=80)

root.mainloop()


    
    
