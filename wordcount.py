# put your code here.

# Opens file


# Read each line in file


def get_word_counts(text):
    """Count letter occurrences. Return dict of {word:count}."""

    text = open(text)
    word_counts = {}

    for line in text:
        list_of_words = line.rstrip().split()

        for word in list_of_words:
            word_counts[word] = word_counts.get(word, 0) + 1

            quantity = word_counts[word]
            print word, quantity


get_word_counts("test.txt")
