import webbrowser

courses = {
    "HM1": {"id": "1896358", "name": "Course A"},
    "LA1": {"id": "1922321", "name": "Course B"},
    "HM2": {"id": "2026012", "name": "Course C"},
    "LA2": {"id": "2076391", "name": "Course D"},
    "GBI": {"id": "1904386", "name": "Course E"}
}


s = input()
course = courses["HM1"]["name"]
print(course)

#webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={course}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")