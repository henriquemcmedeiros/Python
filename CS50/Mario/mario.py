from cs50 import get_int

# Mario.c em Python


def main():
    while True:
        n = get_int("Height: ")
        if n <= 8 and n >= 1:
            break

    for i in range(n):
        for j in range(n):
            if (i + j >= n - 1):
                print("#", end="")
            else:
                print(" ", end="")
        print("")

main()
