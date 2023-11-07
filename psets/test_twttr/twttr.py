def main():
    w = shorten(input("Input: ").strip())
    print(w)


def shorten(word):
    newstr = ""
    for letter in word:
        match letter.lower():
            case "a"|"e"|"i"|"o"|"u":
                continue
            case _:
                newstr = newstr+letter
    return newstr

    if __name__ == "__main__":
        main()