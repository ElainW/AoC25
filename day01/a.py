import sys

num = 50
count = 0
click = 0


def add(a, b):
    if a+b >= 0 and a+b <= 99:
        return a+b
    elif a+b < 0:
        return add(a+100, b)
    else:
        return add(a-100, b)


def subtract(a, b):
    if a-b >= 0 and a-b <= 99:
        return a-b
    elif a-b < 0:
        return subtract(a+100, b)
    else:
        return subtract(a-100, b)


with open(sys.argv[1]) as f_in:
    for lines in f_in:
        click = int(lines.rstrip()[1:])
        if lines[0] == "L":
            num = subtract(num, click)
        elif lines[0] == "R":
            num = add(num, click)
        else:
            sys.exit("Not defined action")
        print(num)
        if num == 0:
            count += 1

print(count)