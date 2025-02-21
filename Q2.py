# Write a python program to check whether a number is palindrome or not? 

def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + digit  # Append digit to reversed number
        num //= 10  # Remove the last digit from num
    
    return original_num == reversed_num

# Input from user
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


 ***Output:
Enter a number: 5
5 is a palindrome.

Enter a number: 34
34 is not a palindrome.
***

