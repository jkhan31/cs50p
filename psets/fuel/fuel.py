while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        val = round(x / y * 100)
        if x > y:
            pass
        elif val >= 99:
            print("F")
            break
        elif val <= 1:
            print("E")
            break
        else:
            print(str(val) + "%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


