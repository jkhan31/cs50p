def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = float(d.removeprefix("$"))
    # print("d = ", d)
    # print("dollar type = ", type(d))
    return float(d)

def percent_to_float(p):
    # TODO
    p = float(p.removesuffix("%")) / 100
    # print("p = ", p)
    # print("percent type = ", type(p))
    return float(p)

main()