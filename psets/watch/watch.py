import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'.+https?://(?:www\.)?youtube.com/embed/([a-zA-Z0-9]+).+',s):
        return (f"https://youtu.be/{matches.group(1)}")
    else:
        return None

if __name__ == "__main__":
    main()