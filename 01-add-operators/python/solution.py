
operators = ["*",  "/", "+", "-",]


def splitNumber(n: int) -> list[int]:
    str_n = list(str(n))
    return [int(x) for x in str_n]


def test_operation(digits: list[int], operator: str):

    if operator == "+":
        res = 0
        for x in digits:
            res += x
        return res
    elif operator == '-':
        res = 0
        for x in digits:
            res -= x
        return res
    elif operator == '*':
        res = 1
        for x in digits:
            res *= x
        return res
    elif operator == '*':
        res = 1
        for x in digits:
            res /= x
        return res
    return 0


def addOperators(source: int, target: int):
    digits = splitNumber(source)

    solutions = []
    for op in operators:
        if test_operation(digits, op) == target:
            str_digits = [str(x) for x in digits]
            operation_string = op.join(str_digits)
            solutions.append(operation_string)

    return solutions


print(addOperators(123, 6))
