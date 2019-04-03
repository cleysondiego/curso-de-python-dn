var = 1

def soma1(x: int) -> int:
    return x + var

assert soma1(1) == 2
var = 5
assert soma1(1) == 2
