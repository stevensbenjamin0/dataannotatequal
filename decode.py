def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store message words
    message_words = []

    # Iterate over each line of the file
    for line in lines:
        # Split the line into number and word
        number, word = line.strip().split()
        # Convert number to integer
        number = int(number)
        # Add the word to message_words list if its index is equal to the number
        if len(message_words) == number - 1:
            message_words.append(word)

    # Join the message words into a single string and return
    return ' '.join(message_words)

# Example usage:
decoded_message = decode("coding_qual_input")
print(decoded_message)
