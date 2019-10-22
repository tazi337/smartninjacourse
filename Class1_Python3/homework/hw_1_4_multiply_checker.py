def multiplication(var1: float, var2: float) -> float:
    result = var1 * var2
    return result


assert multiplication(10, 5) == 50
assert multiplication(1.1, 5) == 5.5
assert multiplication(10.5, 0) == 0

print("Success")
