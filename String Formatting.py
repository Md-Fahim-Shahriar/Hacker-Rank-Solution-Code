def print_formatted(number):
    x = len("{0:b}".format(number))
    # print(x)
    for i in range(1, number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}x} {0:{w}b}".format(i,w = x).upper())

number = int(input())
print_formatted(number)