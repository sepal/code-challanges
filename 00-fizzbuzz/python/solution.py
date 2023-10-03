def fizzbuzz(start: int, end: int) -> list[str]:
    def is_fizz(x): return x % 3 == 0
    def is_buzz(x): return x % 5 == 0
    def is_fizzbuzz(x): return is_fizz(x) & is_buzz(x)

    output = []
    for i in range(start, end + 1):
        if (is_fizzbuzz(i)):
            output.append("FizzBuzz")
        elif is_fizz(i):
            output.append("Fizz")
        elif is_buzz(i):
            output.append("Buzz")
        else:
            output.append(str(i))

    return output
