'''Write a program to generate the Fibonacci sequence up to 100.'''
#Write a program to generate the Fibonacci sequence up to 100.
def fibonacci_sequence():
    # Initialize the first two numbers of the Fibonacci sequence
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence up to 100
    while fib_sequence[-1] + fib_sequence[-2] <= 100:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

# Call the function to generate the Fibonacci sequence
fib_sequence = fibonacci_sequence()

# Print the Fibonacci sequence
print("Fibonacci sequence up to 100:")
print(fib_sequence)
'''Write a program to generate the Fibonacci sequence up to 100.'''
#Write a program to generate the Fibonacci sequence up to 100.
def fibonacci_sequence():
    # Initialize the first two numbers of the Fibonacci sequence
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence up to 100
    while fib_sequence[-1] + fib_sequence[-2] <= 100:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

# Call the function to generate the Fibonacci sequence
fib_sequence = fibonacci_sequence()

# Print the Fibonacci sequence
print("Fibonacci sequence up to 100:")
print(fib_sequence)
