import webbrowser

courses = {
    "HM1" : "1896358",
    "LA1" : "1922321",
    "HM2" : "2026012",
    "LA2" : "2076391",
    "GBI" : "1904386"
}
s = input()
course = courses[s]
webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={course}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")