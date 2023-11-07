import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        trials = 1
        while True:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x + y):
                score += 1
                break
            elif ans != (x + y) and trials < 3:
                print("EEE")
                trials += 1
            elif ans != (x + y) and trials == 3:
                print("EEE")
                print(f"{x} + {y} = {x+y}")
                break
    print(f"Score: {score}")





def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x < 1 or x > 3:
                raise ValueError
            else:
                return x
        except ValueError:
            pass
        except TypeError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()