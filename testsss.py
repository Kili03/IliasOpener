import keyboard
from tkinter import *

import webbrowser

courses = {
    "HM1" : "1896358",
    "LA1" : "1922321",
    "HM2" : "2026012",
    "LA2" : "2076391",
    "GBI" : "1904386"
}


def open(r, root):
    print("worked")
    print(r)

    #s = input()
    course = courses[r]
    webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={course}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")

    root.destroy()
    


def on_hotkey():
    # Open a Tkinter window
    root = Tk()
    # Add some widgets to the window
    label = Label(root, text="You prefffssed Ctrl+Alt+T!")
    e = Entry(root)
   
    Button(root, text = "open", command=lambda: open(e.get(), root)).pack()
    
    label.pack()
    e.pack()
    root.bind("<Return>", lambda event: open(e.get(), root))
    # Start the main loop
    #root.after(1, lambda: root.focus_force())
    #e.focus()
    root.after(1, lambda: (root.focus_force(), e.focus()))
    root.mainloop()

# Register the hotkey
keyboard.add_hotkey('ctrl+alt+t', on_hotkey)

# Start the event loop
keyboard.wait()