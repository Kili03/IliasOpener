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

print(courses["W22"]["HM1"]["Übungen"])

list = ["W22", "S23"]

s = input("Semester[W22/S23]: ")
if (s.isdigit()):
    s = list[int(s)]
i = 0
list2 = []
for e in courses[s]:
    if e != "id":
        print(f"{e}/{i}")
        list2 += [e]
        i+=1

ss = input("Course: ")
if (ss.isdigit()):
    ss = list2[int(ss)]
i = 0
list3 = []
for e in courses[s][ss]:
    print(f"{e}/{i}")
    list3 += [e]
    i+=1

sss = input("Name: ")
if (sss.isdigit()):
    sss = list3[int(sss)]
id = courses[s][ss][sss]
print(id)


'''s = input("Semester: ")

if "/" in s:
    course, group = s.split("/")
    id = courses[course][group]

else:
    id = courses[s]["id"]

#course = courses["HM1"]["name"]
print(id)

#webbrowser.open_new_tab(f"https://ilias.studium.kit.edu/ilias.php?ref_id={course}&cmdClass=ilrepositorygui&cmdNode=x0&baseClass=ilrepositorygui")'''