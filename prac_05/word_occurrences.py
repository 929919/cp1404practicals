"""
Word Occurrences
Estimate: 15 minutes
Actual:
"""
def main():
    """Count occurrences of words in a string and display results in a sorted manner."""
    text = input("Text: ")
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_length = max(len(word) for word in word_counts)

    main()