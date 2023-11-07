month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            #print("m =",m,"d =",d,"y =",y)
        elif "," in date:
            m, d, y = date.split(" ")
            m = month_list.index(m) + 1
            m = int(m)
            d = int(d.replace(",",""))
            y = int(y)
            #print("m =",m,"d =",d,"y =",y)
        elif "," not in date:
            pass
        else:
            pass

        if int(d) > 31 or int(d) < 1:
            pass
        elif int(m) > 12 or int(m) < 1:
            pass
        else:
            print(f"{y}-{m:02}-{d:02}")
            break
    except KeyError:
        pass
    except ValueError:
        pass
    except TypeError:
        pass
    except NameError:
        pass


#check_date("9/8/1636")
#check_date("September 8, 1636")
#check_date("10/9/1701")
#check_date("October 9, 1701")
#check_date("9/8/1636")
#check_date("23/6/1912")
#check_date("10 December, 1815")
#check_date("October/9/1701")
#check_date("1/50/2000")
#check_date("September 8 1636")