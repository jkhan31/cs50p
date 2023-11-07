import random
import sys

def main():
    level = get_int("Level: ")
    print(level)
    ans = random.randint(1,level)
    while True:
        guess = get_int("Guess: ")
        if guess < ans:
            print("Too small!")
            pass
        elif guess > ans:
            print("Too large!")
            pass
        else:
            sys.exit("Just right!")
            



def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x < 1:
                pass
            else:
                return x
        except ValueError:
            pass

main()