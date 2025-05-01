def word_count(bookspam):
    words = bookspam.split()
    return len(words)

def char_count(booksplosion):
    book_chars = list(booksplosion.lower())
    char_dict = {}
    for char in book_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
