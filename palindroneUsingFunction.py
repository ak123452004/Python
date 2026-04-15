def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return original == reverse
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(n, "is a Palindrome Number")
else:
    print(n, "is not a Palindrome Number")
