import keyboard
from tkinter import *
import json

import webbrowser

courses = {
    "HM1" : "1896358",
    "LA1" : "1922321",
    "HM2" : "2026012",
    "LA2" : "2076391",
    "GBI" : "1904386"
}

with open("courses.json", "r") as f:
    courses = json.load(f)

def destroy(root):
    root.destroy()

'''def open(r, root):
    print("worked")
    print(r)

    s = input()
    course = courses[r]
    webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={course}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")

    root.destroy()'''

list = ["W22", "S23"]

def callback(root, sv2, r):
    print(sv2.get())
    sv = sv2.get()

    if len(sv) >= 1:
        s = sv[0]
        if (s.isdigit()):
            s = list[int(s)]
        i = 0
        list2 = []
        rs = ""
        for e in courses[s]:
            if e != "id":
                print(f"{e}/{i}")
                rs += f"{e}/{i}\n"
                list2 += [e]
                i+=1
        r.config(text=rs)

    if len(sv) >= 2:
        ss = sv[1]
        if (ss.isdigit()):
            ss = list2[int(ss)]
        i = 0
        list3 = []
        rs = ""
        for e in courses[s][ss]:
            print(f"{e}/{i}")
            rs += f"{e}/{i}\n"
            list3 += [e]
            i+=1
        r.config(text=rs)

    if len(sv) == 3:
        sss = sv[2]
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
    # Add some widgets to the window
    label = Label(root, text="You prefffssed Ctrl+Alt+T!")
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(root, sv, r))
    e = Entry(root, textvariable=sv)
    r = Label(root, text="W22/0\nS23/1")

   
    #Button(root, text = "open", command=lambda: open(e.get(), root)).pack()
    
    label.pack()
    e.pack()
    r.pack()
    #root.bind("<Return>", lambda event: open(e.get(), root))
    # Start the main loop
    #root.after(1, lambda: root.focus_force())
    #e.focus()
    root.after(1, lambda: (root.focus_force(), e.focus()))
    root.mainloop()
    root.destroy()

# Register the hotkey
keyboard.add_hotkey('ctrl+alt+t', on_hotkey)
# Start the event loop
keyboard.wait()