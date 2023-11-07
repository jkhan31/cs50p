d = {}

while True:
    try:
        item = input().strip().upper()
        d[item] = d[item] + 1
    except KeyError:
        d[item] = 1
        pass
    except EOFError:
        sorted_list = sorted(d)
        sorted_d = {}
        for k in sorted_list:
            sorted_d[k] = d[k]
        for item in sorted_d:
            print(sorted_d[item], item)
        break
