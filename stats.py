#counts the number of words in the book
def word_count(bookspam):
    words = bookspam.split()
    return len(words)

#counts the amount of times each individual character appears in the book and returns as a dictionary
def char_count(booksplosion):
    book_chars = list(booksplosion.lower())
    char_dict = {}
    for char in book_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

#sorting key (by count integer)
def sort_on(dict):
    return dict["count"]

#accepts the dictionary provided by char_count and sorts it as a list of dictionaries by count in decending order
def list_sorter(unsorted_mess):
    sorted_mess = []
    for char in unsorted_mess:
        count = unsorted_mess[char]
        sorted_mess.append({"char": char, "count": count})
    sorted_mess.sort(reverse=True, key=sort_on)
    return sorted_mess