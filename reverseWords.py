# Question: Write a function that reverses the words in a given string.
# The words are separated by spaces. Return the resulting reversed string.

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage
print(reverse_words("The quick brown fox"))  # Output: "fox brown quick The"
