
import tkinter as tk
mainwindow = tk.Tk()
mainwindow.title("sample window")
heading_label = tk.Label(mainwindow,text="hellow world")
heading_label.pack()
name_fields=tk.Entry(mainwindow)
name_fields.pack()
def takevalueinput():
    name=name_fields.get()
    print(name)
button = tk.Button(mainwindow,text="getvalue",command = lambda:takevalueinput())
button.pack()
mainwindow.mainloop()