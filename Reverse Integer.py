# Question 5: Reverse Integer
def reverse_integer(num):
    # Convert the absolute value of the integer to a string
    reversed_num = int(str(abs(num))[::-1])

    # Adjust the sign if the original number was negative
    if num < 0:
        reversed_num *= -1

    return reversed_num

# Ask the user to enter an integer
user_input = int(input("Enter an integer: "))

# Call the function to reverse the integer
result = reverse_integer(user_input)

# Print the reversed integer
print("Reversed integer:", result)

