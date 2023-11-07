import sys

def main():
    check_total_args()
    check_valid_file()
    file_line_counter()


# Check if only 1 valid python file
def check_total_args():
    # check for 1 command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


# check if python file
def check_valid_file():
    while True:
        try:
            file_name = sys.argv[1]
            if ".py" not in file_name:
                sys.exit("Not a Python file")
            else:
                with open(sys.argv[1]) as file:
                    return
        except FileNotFoundError:
            sys.exit("File does not exist")


# open file, count lines, print number of lines
def file_line_counter():
    line_count = 0

    # puts lines in a list
    with open(sys.argv[1]) as file:
        lines = file.readlines()

    for line in lines:
        #count docstring
        if line.strip().startswith("__"):
            line_count += 1
            pass
        # skip comment
        elif line.lstrip().startswith("#"):
            pass
        # skip blank line
        elif line.isspace():
            pass
        #count line
        else:
            line_count += 1

    print(line_count)


if __name__ == "__main__":
    main()