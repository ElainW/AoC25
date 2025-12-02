import sys

num = 50
prev_num = 50
count = 0
prev_count = 0
click = 0


def add(a, b, count):
    return (a+b)%100, count+abs((a+b)//100)


def subtract(a, b, count):
    if a == 0:
        return (-b) % 100, count+b//100
    elif (a-b) % 100 == 0:
        return 0, count+abs(a-b)//100+1
    elif a < b:
        return (a-b)%100, count+abs((a-b))//100+1
    elif a > b:
        return a-b, count
    else:
        sys.exit(a, b, count)


with open(sys.argv[1]) as f_in:
    for lines in f_in:
        click = int(lines.rstrip()[1:])
        if lines[0] == "L":
            num, count = subtract(num, click, count)
        elif lines[0] == "R":
            num, count = add(num, click, count)
        else:
            sys.exit("Not defined action")

        print(lines.rstrip(), prev_num, num, count-prev_count)
        prev_count = count
        prev_num = num

print(count)