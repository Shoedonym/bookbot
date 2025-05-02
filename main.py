import sys
from stats import word_count
from stats import char_count
from stats import list_sorter

#imports book text from file
def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    try:
        book_path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    booktext = get_book_text(book_path)
    num_words = word_count(booktext)
    num_chars = char_count(booktext)
    character_count = list_sorter(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in character_count:
        if character["char"].isalpha() == True:
            print(f"{character["char"]}: {character["count"]}")
    print("============= END ===============")

main()