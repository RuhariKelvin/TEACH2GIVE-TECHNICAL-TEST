'''Write a program that takes an integer as input and returns true if the input is a power of two.'''
def is_power_of_two(n):
    # Check if the number is greater than 0 and the bitwise AND result is 0
    return n > 0 and (n & (n - 1)) == 0

while True:
    # Ask the user to enter the input
    user_input = int(input("Enter an integer: "))

    # Check if the input is a power of two
    if is_power_of_two(user_input):
        print("True")
    else:
        print("False")

    # Ask the user if they want to check another number
    choice = input("Do you want to check another number? (yes/no): ").lower()
    if choice != "yes":
        break
