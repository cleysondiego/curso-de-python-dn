var = 1

def soma2(x: int) -> int:
    global var
    var += 1
    return x + var

assert soma2(2) == 4
assert soma2(2) == 4
