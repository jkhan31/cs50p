import sys
import csv

def main():
    students = []
    f1 = ""
    f2 = ""

    # validate command-line arguments
    check_args()
    check_before_file()

    # assign filenames
    f1 = sys.argv[1]
    f2 = sys.argv[2]

    copy_student_data(f1,students)
    create_new_csv(f2, students)


# check for 2 command-line arguments
def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_before_file():
    try:
        # check for csv file
        if ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1]) as file:
                return
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def copy_student_data(csv1, students):
    with open(csv1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].strip().split(",")
            students.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})
    return


def create_new_csv(csv2, students):
    with open(csv2, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for s in students:
            writer.writerow({"first": s["first"], "last": s["last"], "house": s["house"]})
    return

if __name__ == "__main__":
    main()