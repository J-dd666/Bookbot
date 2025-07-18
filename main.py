from stats import num_words
from stats import num_letters
import sys
import os

def main():
    if len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Error: Please provide a file path")
        sys.exit(1)
    book_path = sys.argv[1]
    if not os.path.isfile(book_path):
        print(f"Error: file '{book_path}' does not exist")
        sys.exit(1)
    book_contents = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_contents)} total words")
    print("--------- Character Count -------")
    for item in num_letters(book_contents):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
def get_book_text (book_path):
    with open(book_path) as f:
        contents = f.read()
        return contents
    
main()