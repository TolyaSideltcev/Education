def test (*params):
    print(*params)
test("Hello", 4, False)

def recursion(number):
    if number == 1:
        return number
    else:
        return number * recursion(number - 1)

print(recursion(5))