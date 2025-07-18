import collections

def num_words(book_contents):
    words = 0
    for word in book_contents.split():
        words += 1
    return words
def num_letters(book_contents):
    sorted_letters = []
    counts = collections.Counter(book_contents.lower())
    for character, amount in counts.most_common():
        if character.isalpha():
            sorted_letters.append({"char":character,"num":amount})
    return sorted_letters