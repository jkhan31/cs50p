prob = input("Expression: ").strip()
x, y, z = prob.split(" ")

x = float(x)
z = float(z)


match y:
    case "+":
        print(round(x+z,1))
    case "-":
        print(round(x-z,1))
    case "*":
        print(round(x*z,1))
    case "/":
        print(round(x/z,1))
        
