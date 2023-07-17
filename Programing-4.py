def get_multiples(numbers, multiples):
    counts = {}
    for number in numbers:
        for multiple in multiples:
            if number % multiple == 0:
                if multiple in counts:
                    counts[multiple] += 1
                else:
                    counts[multiple] = 1
    return counts


def main():
    numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counts = get_multiples(numbers, multiples)
    print(counts)


if __name__ == "__main__":
    main()
