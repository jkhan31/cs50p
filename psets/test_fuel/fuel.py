def main():
        x, y = input("Fraction: ").split("/")
        converted = convert(1/2)
        g = gauge(50)
        print(g)

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    try:
        if x > y:
             raise ValueError
        return round(x / y * 100)
    except ValueError:
         pass
    except ZeroDivisionError:
         pass


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    elif percentage > 1 and percentage < 99:
        return(str(percentage) + "%")

