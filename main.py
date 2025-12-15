from stats import *

"""
this main function calls get_txt and stores its returned
value in the content variable, then iterates over it to
determine the word count, which is stored in the word_count
variable
"""


def main():
    content, path = get_txt()
    word_count = 0
    for i in content.split():
        word_count += 1

    char_count = num_chars(content)
    sorted_chars = sort_chars(char_count)

    print("===== Fresnel =====")
    print(f"Analyzing text found at {path}")
    print("--- Word Count ---")
    print(f"Found {word_count} total words")
    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
