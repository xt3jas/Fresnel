"""
this function asks the user for a file path and reads the
file at the destination, returning its content as a string
for future use by other functions
"""
def get_txt(path=None):
    if path is None:
        path = input("Enter the path of your file: ")
    with open(path) as f:
        return f.read(), path

"""
counts the number of characters in the text file and returns
a dictionary containing the character counts
"""
def num_chars(text):
    char_count = {}
    for i in text.lower():
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count


"""
converts character count dictionary to a sorted list of dictionaries
filters out non-alphabetical characters and sorts by count descending
"""


def sort_chars(char_dict):
    def get_num(d):
        return d["num"]

    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=get_num)
    return char_list
