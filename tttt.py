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

print(addToDict)