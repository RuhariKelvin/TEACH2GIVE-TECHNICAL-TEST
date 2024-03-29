'''Question 1: Write a program that prints the numbers from 1 to 100. 
  But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
 For numbers which are multiples of both three and five print “FizzBuzz”.'''
def fizzbuzz():
    # I iterate through the numbers from 1 to 100
    for i in range(1, 101):
        # I check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
      # Call the function to execute the FizzBuzz logic
    fizzbuzz()

if __name__ == "__main__":
    main()