import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    user_input = re.search(r"^([1-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-2]?):?([0-5][0-9])? (AM|PM)",s)
    start_time = ""
    end_time = ""
    if user_input:
        values = user_input.groups()
        # print(values)
        start_time = convert_time(values[0],values[1],values[2])
        end_time = convert_time(values[3],values[4],values[5])
        return (f"{start_time} to {end_time}")
    else:
        raise ValueError

def convert_time(hr,min,ampm):
    if ampm == "PM":
        if int(hr) <12:
            hr = int(hr) + 12
    elif int(hr) == 12:
        hr = 0
    if min == None:
        min = "00"
    return(f"{int(hr):02}:{min}")


if __name__ == "__main__":
    main()