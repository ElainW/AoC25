import sys
from math import sqrt

def find_length_divisor(num):
    divisors = set()
    num = str(num)
    divisors.add(1)
    for i in range(2, int(sqrt(len(num))) + 1):
        if len(num) % i == 0:
            divisors.add(i)
            divisors.add(len(num)//i)
    return divisors


def check_silly(num, divisor):
    num = str(num)
    if len(num) == 1:
        return False
    if len(num) % divisor != 0:
        return False
    else:
        if (num[:divisor]) * (len(num)//divisor) == num:
            return True


invalid_set = set()
with open(sys.argv[1], 'r') as f_in:
    for lines in f_in:
        ranges = lines.rstrip().split(',')
        for num_range in ranges:
            start, end = [int(x) for x in num_range.split('-')]

            for num in range(start, end+1):
                divisors = find_length_divisor(num)
                # print(num, divisors)
                for div in divisors:
                    if check_silly(num, div):
                        print(num, div)
                        invalid_set.add(num)

print(invalid_set)
print(sum(invalid_set))


