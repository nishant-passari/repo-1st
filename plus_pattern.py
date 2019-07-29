import sys


def pattern(n):
    for i in range(1, n + 1):
        if i != (n // 2) + 1:
            for j in range(n // 2):
                print(" ", end='')
            print("*")
        else:
            for i in range(n):
                print("*", end='')
            print()


pattern(int(sys.argv[1]))

