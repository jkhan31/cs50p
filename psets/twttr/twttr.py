str = input("Input: ").strip()
newstr = ""
for letter in str:
    match letter.lower():
        case "a"|"e"|"i"|"o"|"u":
            continue
        case _:
            newstr = newstr+letter
print(newstr)