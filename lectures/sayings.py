def main():
    hello("world")
    goodbye("world")

# prints hello, name
def hello(name):
    print(f"hello, {name}")

# prints goodbye, name
def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()