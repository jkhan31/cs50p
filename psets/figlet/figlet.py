import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

while True:
    try:
        # if zero command-line arguments, output text in a random font
        if len(sys.argv) == 1:
            s = input("Input: ")
            f = random.choice(font_list)
            figlet.setFont(font = f)
            print(figlet.renderText(s))
            break
        # if two command-line arguments, output text in specific font
        elif len(sys.argv) == 3:
            flag = sys.argv[1]
            f = sys.argv[2]
            if (flag == "-f" or flag == "--font") and f in font_list:
                s = input("Input: ")
                figlet.setFont(font = f)
                print(figlet.renderText(s))
                break
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    except EOFError:
        break
