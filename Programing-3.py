def odd_numbers(x):
    odd_numbers = []
    for i in range(1, x + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


def main():
    x = int(input("Enter a number: "))
    print(odd_numbers(x))


if __name__ == "__main__":
    main()
