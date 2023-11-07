due = 50

while due > 0:
    if due > 0:
        print("Amount Due:", due)
        coin = int(input("Insert Coin: "))
        match coin:
            case 25 | 10 | 5:
                due = due - coin
    else:
        break

print("Change Owed:", due * -1)