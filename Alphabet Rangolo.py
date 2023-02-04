N = int(input())

for i in range (1, N+3, 2):
    ascivalue = 97 + (i-1)
    print(chr(ascivalue).center(N*N, '-'))
