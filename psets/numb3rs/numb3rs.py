import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        numbers = []
        if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
            numbers = ip.split(".")
            for n in numbers:
                if int(n) <0 or int(n) > 255:
                    return False
            return True
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False




if __name__ == "__main__":
    main()