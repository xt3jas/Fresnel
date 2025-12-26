import re
import math
from collections import Counter
from statistics import variance


# helper functions

def get_words(text):
# cleans and tokenizes words from the text"
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().split()

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
    def syllables(words):
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
'''
calculates how many pronouns (ego graph) are there in a text
'''

def pronouns(words):
    first_person = {"i", "me", "my", "mine", "myself"}
    collective = {"we", "us", "our", "ours", "ourselves"}
    second_person = {"you", "your", "yours"}
    counts = {"I/Me": 0, "We/Us": 0, "You": 0}
    for w in words:
        if w in first_person:
            counts["I/Me"] += 1
        elif w in collective:
            counts["We/Us"] += 1
        elif w in second_person:
            counts["You"] += 1
    return counts

'''
counts modal verbs as a way of assessing confidence in the text
'''
def modal_verbs(words):
    necessity = {"must", "should", "always", "will", "shall"}
    possibility = {"might", "could", "maybe", "perhaps", "possibly"}
    counts = {"necessity": 0, "possibility": 0}
    for w in words:
        if w in necessity:
            counts["necessity"] += 1
        elif w in possibility:
            counts["possibility"] += 1
    return counts

"""
checks whether the author wrote the entire text by themselves or whether
they used some sort of ghostwriter/AI assistance in between the text. done by
determining the cosine similarity between excerpts of the text.
"""

def check_auth(words):
    mid = len(words) // 2
    first_half = words[:mid]
    second_half = words[mid:]
    target_words = {"the" , "and", "is", "in", "to", "of", "a", "that", "it", "on"}

    def get_vec(w_list):
        c = Counter(w_list)
        return [c[t] for t in target_words]
    vec1 = get_vec(first_half)
    vec2 = get_vec(second_half)

    # to calculate hte cosine similarity
    dot_prod = sum(a*b for a, b, in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a*a for a in vec1))
    mag2 = math.sqrt(sum(b*b for b in vec2))

    if mag1 * mag2 == 0: return 0
    return dot_prod / (mag1 * mag2)




