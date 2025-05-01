from stats import word_count
from stats import char_count

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    booktext = get_book_text('./books/frankenstein.txt')
    num_words = word_count(booktext)
    num_chars = char_count(booktext)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()