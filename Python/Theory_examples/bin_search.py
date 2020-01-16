def binarySearch():
    begin = int(input("The number will be between _ and _\n"))
    end = int(input())
    value = int(input("What value will you input?\n"))
    guesses = 0

    while True:
        guesses += 1
        mid = int((begin + end) / 2)

        if mid > value:
            end = mid - 1
        elif mid < value:
            begin = mid + 1
        else:
            break

    print(guesses)


if __name__ == "__main__":
    binarySearch()
