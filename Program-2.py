def fibonacci(x):
    if x == 1:
        return [1]
    elif x == 2:
        return [1, 3]
    else:
        fibs = [1, 3]
        for i in range(3, x + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])
        return fibs


def main():
    x = int(input("Enter a number: "))
    print(fibonacci(x))


if __name__ == "__main__":
    main()
