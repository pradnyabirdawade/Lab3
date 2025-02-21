#Q3 Write a python program finding the factorial of a given number using a while loop.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    while n > 0:
        result *= n
        n -= 1
    
    return result

# Taking user input
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

***Output
Enter a number: 45
Factorial of 45 is 119622220865480194561963161495657715064383733760000000000

Enter a number: 12
Factorial of 12 is 479001600
***
