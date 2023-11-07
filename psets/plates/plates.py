def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

punc = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"

def is_valid(s):
    # check if min 2 characters and max 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # check if all characters are letters
    elif s.isalpha():
        return True

    # check if first 2 characters are letters
    elif s[0:2].isnumeric():
        return False

    # check if numbers used in middle of plate
    elif s[-1].isalpha():
        for chars in s:
            if chars.isnumeric():
                return False
            else:
                continue

    else:
        nums = ""
        for chars in s:
            # extract numbers from plate
            if chars.isnumeric():
                nums = nums + chars
            # check for punctuation
            elif chars in punc:
                return False
            else:
                continue

        # check if numbers from plate starts with 0
        if nums[0] == "0":
            return False
        
        # check if number is middle or pass all requirements
        else:
            return s.endswith(nums)


if __name__ == "__main__":
    main()