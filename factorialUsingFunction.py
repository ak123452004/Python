n = int(input("Enter a number: "))
def factorial(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * factorial(f - 1)

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial(n)
    print("Factorial of", n, "is", result)
