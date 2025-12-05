import sys

def check_silly(num):
    num = str(num)
    if len(num) % 2 == 1:
        return False
    else:
        if num[:len(num)//2] == num[len(num)//2:]:
            return True

sum_invalid = 0
with open(sys.argv[1], 'r') as f_in:
    for lines in f_in:
        ranges = lines.rstrip().split(',')
        for num_range in ranges:
            start, end = [int(x) for x in num_range.split('-')]

            for num in range(start, end+1):
                if check_silly(num):
                    sum_invalid += num

print(sum_invalid)


