import inflect

names = []
names_in = []

while True:
    try:
        new_name = input("Name: ")
        names.append(new_name)
    except EOFError:
        phrase = "Adieu, adieu, to "
        for name in names:
            names_in.append(name)
            if len(names_in) == 1:
                print(phrase + names[0])
                new_phrase = phrase + name
            elif len(names_in) == 2:
                print(f"{phrase}{names[0]} and {names[1]}")
                new_phrase = phrase + names[0] + ", " + name
            elif len(names_in) > 2:
                if name != names[-1]:
                    print(f"{new_phrase}, and {name}")
                    new_phrase = new_phrase + ", " + name
                else:
                    print(f"{new_phrase}, and {name}")

        break
