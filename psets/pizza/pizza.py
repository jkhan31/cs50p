import sys
from tabulate import tabulate

def main():
    check_args()
    check_csv()
    print_table()


def check_args():
    # check for 1 command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def check_csv():
    try:
        # check for csv file
        if ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1]) as file:
                return
    except FileNotFoundError:
        sys.exit("File does not exist")

def print_table():
    # create list of rows
    table = []
    with open(sys.argv[1]) as file:
        for line in file:
            table.append(line.rstrip().split(","))

    # print table grid
    print(tabulate(table,headers="firstrow",tablefmt="grid"))


if __name__ == "__main__":
    main()