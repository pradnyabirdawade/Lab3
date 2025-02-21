#Q1 Write a python program to reverse a number using a while loop.

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

num = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(num))

***Output:
Enter a number: 56
Reversed Number: 65

Enter a number: 456
Reversed Number: 654

