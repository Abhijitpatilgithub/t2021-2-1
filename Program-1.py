class Calculator:

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


def main():
    a = 10
    b = 5
    operation = "multiply"

    calculator = Calculator(a, b, operation)

    if operation == "add":
        print(calculator.add())
    elif operation == "subtract":
        print(calculator.subtract())
    elif operation == "multiply":
        print(calculator.multiply())
    elif operation == "divide":
        print(calculator.divide())


if __name__ == "__main__":
    main()
