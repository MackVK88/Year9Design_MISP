from tkinter import *
master = Tk()
master.config(background="black")
label = Label(master, text="Hockey Pool")
label.config(background="black")
label.config(foreground="white")
label.pack()
button = Button(master, text="QUIT", fg="red", command=quit)
button.pack(side=BOTTOM)
listbox = Listbox(master)
listbox.config(background="black")
listbox.config(foreground="white")
listbox.pack()
listbox.insert(END, "Top 10 Goal scorers 2017-2018")
lst = [["Alex Ovechkin",49], ["Patrik Laine", 44], ["William Karlsson", 43], ["Evegeni Malkin", 42], ["Eric Staal", 42], ["Connor McDavid", 41], ["Tyler Seguin", 40], ["Anders Lee", 40], ["Nikita Kucherov", 39], ["Nathan MacKinnon", 39]]
for item in lst:
    listbox.insert(END, item[0] + "-" + str(item[1]))

mainloop()