#Question 4: Capitalize words in a sentence
def capitalize_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Capitalize the first letter of each word and join them back
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words into a sentence
    capitalized_sentence = ' '.join(capitalized_words)

    return capitalized_sentence

# Ask the user to enter the string
user_input = input("Enter a sentence: ")

# Call the function to capitalize the words in the input sentence
result = capitalize_words(user_input)

# Print the capitalized sentence
print("Capitalized sentence:")
print(result)
