# Question 6: Vowels counting
def count_vowels(sentence):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Convert the sentence to lowercase to make the comparison case-insensitive
    sentence = sentence.lower()

    # Count the number of vowels in the sentence
    vowel_count = sum(1 for char in sentence if char in vowels)

    return vowel_count

# Ask the user to enter a sentence
user_input = input("Enter a sentence: ")

# Call the function to count the vowels in the input sentence
result = count_vowels(user_input)

# Print the number of vowels in the sentence
print("Number of vowels in the sentence:", result)
