from tkinter import *

root = Tk()
root.geometry("400x250")

frame = Frame(root, width=400, height=250, background="#202124", padx=25, pady=25)
frame.propagate(False)

l = Label(frame, text="This is for testing really cool designs",background="#202124", foreground="white", font = ("Roboto", 10, "normal"))
eframe = Frame(frame, highlightthickness=1, highlightcolor="white", highlightbackground="white")
ed = Entry(eframe, bd = 0, font = ("Roboto", 10, "normal"), background="#202124", foreground="white")
ed.config(highlightthickness=5, highlightbackground="#202124", highlightcolor="#202124", insertbackground="white", insertwidth=1, insertontime=500, insertofftime=500)
l2 = Label(frame, text="Nice, aren't they\nHai\nÜbungsblätter", font = ("Roboto", 10, "normal"), background="#202124", foreground="white")
l2.config(justify="left")

frame.pack()
l.pack()
eframe.pack(padx=5, pady=5)
ed.pack()
l2.place(x=100, y=60)
#l2.pack()

root.mainloop()