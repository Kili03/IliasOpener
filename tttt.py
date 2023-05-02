import json

with open("courses.json", "r") as f:
    courses = json.load(f)

check = input("Course to add/edit: ")
if check in courses:
    name = input()
    while name != "end":
        if name not in courses[check]:
            id = input()
            courses[check][name] = id
            name = input()
        else:
            print(f"{name} is already there")
            name = input()
  
else:
    b = input(f"Add course {check} [y/n]")
    if b == "y":
        id = input("Course Id: ")
        courses[check] = {"id" : id}

        name = input()
        while name != "end":
            if name not in courses[check]:
                id = input()
                courses[check][name] = id
                name = input()
            else:
                print(f"{name} is already there")
                name = input()

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