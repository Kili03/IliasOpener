import keyboard
from tkinter import *
import json
from time import sleep

import webbrowser

#https://github.com/Kili03/IliasOpener/blob/424fe43231d77e5e14da10a97ab48daa39afa919/testsss.py#L8



with open("courses.json", "r") as f:
    courses = json.load(f)

list = []
for course in courses:
    list += [course]
    

def callback(root, sv2, r, entry):
    print(sv2.get())
    sv = sv2.get()
    pos = []
    for i in range(len(sv)):
        if sv[i] == "/":
            pos += [i]
    layer = len(pos)

    if layer >= 0:
        s = sv
        if len(pos) >= 1:
            s = sv[:pos[0]]
        if (s.isdigit()):
            s = list[int(s)]
        i = 0
        list2 = []
        rs = ""
        for e in courses[s]:
            if e != "id":
                #print(f"{e}/{i}")
                rs += f"{e}/{i}\n"
                list2 += [e]
                i+=1
        #sv2.set(sv + "/")
        if layer == 0:
            entry.insert(END, "/")
        r.config(text=rs)

    if layer >= 1:
        ss = sv[pos[0]+1:]
        if len(pos) >= 2:
            ss = sv[pos[0]+1:pos[1]]
        if (ss.isdigit()):
            ss = list2[int(ss)]
        i = 0
        list3 = []
        rs = ""
        if (type(courses[s][ss]) != type({})):
            id = courses[s][ss]
            webbrowser.open_new_tab(id)
            root.quit()
        for e in courses[s][ss]:
            #print(f"{e}/{i}")
            rs += f"{e}/{i}\n"
            list3 += [e]
            i+=1
        if layer == 1:
            entry.insert(END, "/")
        r.config(text=rs)

    if layer == 2:
        sss = sv[pos[1]+1:]
        if len(pos) >= 3:
            sss = sv[pos[1]+1:pos[2]]
        if (sss.isdigit()):
            sss = list3[int(sss)]
        id = courses[s][ss][sss]
        if len(id) > 10:
            webbrowser.open_new_tab(id)
        else:
            webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={id}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")
        root.quit()
        #sv2.set("")
        
        

def on_hotkey():
    # Open a Tkinter window
    root = Tk()
    root.title("Ilias Opener")
    root.geometry("400x250")

    frame = Frame(root, width=400, height=250, background="#202124", padx=25, pady=25)
    frame.propagate(False)
    
    eframe = Frame(frame, highlightthickness=1, highlightcolor="white", highlightbackground="white")
    
    l2frame = Frame(frame, background="blue", width=154, height=110)
    l2frame.config(highlightthickness=1, highlightcolor="white", highlightbackground="white", background="#202124")
    l2frame.propagate(False)
    
    # Add some widgets to the window
    label = Label(frame, text="Enter Page Code to open",background="#202124", foreground="white", font = ("Roboto", 10, "normal"))
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(root, sv, r, e))
    e = Entry(eframe, textvariable=sv, bd = 0, font = ("Roboto", 10, "normal"), background="#202124", foreground="white")
    e.config(highlightthickness=5, highlightbackground="#202124", highlightcolor="#202124", insertbackground="white", insertwidth=1, insertontime=500, insertofftime=500)

    y = ""
    i = 0
    for year in courses:
        y += f"{year}/{i}\n"
        i += 1

    #r = Label(l2frame, text=y)
    r = Label(l2frame, text=y, font = ("Roboto", 10, "normal"), background="#202124", foreground="white")
    r.config(justify="left", )
   
    #Button(root, text = "open", command=lambda: open(e.get(), root)).pack()
    
    frame.pack()
    label.pack()
    eframe.pack(padx=5, pady=5)
    e.pack()
    l2frame.place(x=98, y=58)
    r.place(x=0, y=0)
    #root.bind("<Return>", lambda event: open(e.get(), root))
    # Start the main loop
    #root.after(1, lambda: root.focus_force())
    #e.focus()
    root.after(1, lambda: (root.focus_force(), e.focus()))
    root.mainloop()
    try:
        root.destroy()
    except TclError:
        print("Window closed")

# Register the hotkey
#on_hotkey()
keyboard.add_hotkey('ctrl+alt+t', on_hotkey)
# Start the event loop
keyboard.wait()