import re
import math
from collections import Counter

# helper functions

def get_words(text):
# cleans and tokenizes words from the text"
    text = re.sub(r'[^\w\s]', '', text)

def get_sentences(text):
    # Split by period, exclamation, or question mark
    raw_sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings and strip whitespace
    return [s.strip() for s in raw_sentences if s.strip()]

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

'''
Function to calculate the Shannon Entropy of the text. 
A higher score would mean the text is more complex and a lower score would mean that the text is simpler to comprhehnd.
'''
def calc_entropy(text):
    if not text: return 0
    prob_dist = Counter(text)
    total_len = len(text)
    entropy = 0
    for count in prob_dist.values():
        p = count / total_len
        entropy -= p * math.log2(p)
    return entropy



