def main():
    name = input("What's your name? ")
    hello(name)

# hello function
def hello(to = "world"):
    print(f"hello, {to}")

main()