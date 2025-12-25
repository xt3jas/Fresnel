import re
import math
from collections import Counter
from statistics import variance


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

""""
Function to calculate the Lexical Diversity of the text.
A higher score will indicate richer vocab whereas a lower score would indicate more repition. 
"""
def calc_ttr(words):
    if not words: return 0
    unique_words = set(words)
    return len(unique_words) / len(words)


"""
burstiness index calc. basically, the std deviation of sentences is calculated.
high std_dev means more dynamic text whereas low std_dev means more monotone or boring text
"""

def calc_brst(sentences):
    if not sentences: return 0
    lengths = [len(s.split()) for s in sentences]
    mean_len = sum(lengths) / len(lengths)
    variance = sum((l - mean_len) ** 2 for l in lengths) / len(lengths)
    return math.sqrt(variance)


"""
punctuation frequence analyses how often does the text
use a certain punctuation mark. provides a concise breakdown of this
"""
def punc_freq(text):
    marks = {
        "Commas" : text.count(','),
        "Periods" : text.count('.'),
        "Exclamation Marks" : text.count('!'),
        "Question Marks" : text.count('?'),
        "Semicolons" : text.count(';'),
        "Colons" : text.count(':'),
        "Dashes" : text.count('-')
    }
    return marks

"""
calculates the readability of any text using the Flesh-Kincaid formula
"""
def readability(sentences, words):
    if not sentences or not words: return 0
    def syllabes(words):
        return len(re.findall(r'[aeiouy]+', words))
        total_syllables = sum(count_syllables(w) for w in words)
        avg_sentence_len = len(words) / len(sentences)
        avg_syllables_per_word = total_syllables / len(words)

        grade = 0.39 * avg_sentence_len + 11.8 * avg_syllables_per_word - 15.59
        return round(grade, 2)


'''
calculates how immersive the text is by taking note of sensory words
'''


def sensory_immersion(words):
    visual = {"see", "look", "bright", "dark", "blue", "red", "shiny", "vision"}
    auditory = {"hear", "listen", "loud", "quiet", "sound", "noise", "whisper"}
    tactile = {"touch", "feel", "rough", "smooth", "hard", "soft", "cold", "hot"}
    counts = {"visual": 0, "auditory": 0, "tactile": 0}
    for w in words:
        if w in visual:
            counts["visual"] += 1
        elif w in auditory:
            counts["auditory"] += 1
        elif w in tactile:
            counts["tactile"] += 1
    return counts










