import webbrowser
import json

courses = {
    "HM1": {"id": "1896358", "name": "Course A"},
    "LA1": {"id": "1922321", "name": "Course B"},
    "HM2": {"id": "2026012", "name": "Course C"},
    "LA2": {"id": "2076391", "name": "Course D"},
    "GBI": {"id": "1904386", "name": "Course E"}
}

with open("courses.json", "r") as f:
    courses = json.load(f)

s = input()
if "/" in s:
    course, group = s.split("/")
    id = courses[course][group]

else:
    id = courses[s]["id"]

#course = courses["HM1"]["name"]
print(id)

#webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={course}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")