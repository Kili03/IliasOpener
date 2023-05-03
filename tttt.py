import json

with open("courses.json", "r") as f:
    courses = json.load(f)

list = ["W22", "S23"]

s = input("Semester[W22/S23]: ")
if (s.isdigit()):
    s = list[int(s)]
check = input("Course to add/edit: ")
if check in courses[s]:
    name = input("Name: ")
    while name != "end":
        if name not in courses[s][check]:
            id = input("ID: ")
            if len(id) > 10:
                id = id[47:54]
            courses[s][check][name] = id
            name = input("Name: ")
        else:
            print(f"{name} is already there")
            name = input("Name: ")
  
else:
    b = input(f"Add course {check} [y/n]")
    if b == "y":
        id = input("Course Id: ")
        if len(id) > 10:
            id = id[47:54]
        courses[s][check] = {"id" : id}
        name = input("Name: ")
        while name != "end":
            if name not in courses[s][check]:
                id = input("ID: ")
                if len(id) > 10:
                    id = id[47:54]
                courses[s][check][name] = id
                name = input("Name: ")
            else:
                print(f"{name} is already there")
                name = input("Name: ")

    else:
        print(f"didn't add course {check}")



with open("courses.json", "w") as f:
    json.dump(courses, f)


'''
names = []
codes = []

name = input()
while (name != "end"):
    url = input()
    code = url[47:54]
    print(code)
    names += [name]
    codes += [code]
    name = input()

addToDict = ",\n"
for i in range(len(names)):
    n = names[i]
    c = codes[i]
    if i < len(names) - 1:
        addToDict += f"    \"{n}\" : \"{c}\",\n"
    else:
        addToDict += f"    \"{n}\" : \"{c}\""

print(addToDict)'''