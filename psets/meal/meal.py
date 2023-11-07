def main():
    t = input("What time is it? ").strip().lower()
    time = convert(t)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >=18 and time <= 19:
        print("dinner time")


def convert(time):
    if time.endswith(" a.m."):
        hhmm = time.removesuffix(" a.m.").split(":")
        hours = int(hhmm[0])
        min = int(hhmm[1])
        minToHours = float(min / 60)
        return hours + minToHours
    elif time.endswith(" p.m."):
        hhmm = time.removesuffix(" p.m.").split(":")
        hours = int(hhmm[0]) + 12
        min = int(hhmm[1])
        minToHours = float(min / 60)
        return hours + minToHours
    else:
        hhmm = time.split(":")
        hours = int(hhmm[0])
        min = int(hhmm[1])
        minToHours = float(min / 60)
        return hours + minToHours


if __name__ == "__main__":
    main()