import stats


def main():

    try:
        content, path = stats.get_txt()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    words = stats.get_words(content)
    sentences = stats.get_sentences(content)

    if not words:
        print("Error: No words found. Please check the fix for 'get_words' in stats.py.")
        return

    print(f"\n{'=' * 15} FRESNEL REPORT {'=' * 15}")
    print(f"Analyzing: {path}")
    print(f"Word Count: {len(words)}")
    print(f"Sentence Count: {len(sentences)}")
    print("-" * 46)

    print("\n[I. STYLOMETRIC FINGERPRINT]")

    entropy = stats.calc_entropy(content)
    print(f"Shannon Entropy:      {entropy:.4f}")

    ttr = stats.calc_ttr(words)

    burstiness = stats.calc_brst(sentences)
    print(f"Burstiness Score:     {burstiness:.4f}")

    try:
        grade = stats.readability(sentences, words)
        print(f"Flesch-Kincaid Grade: {grade}")
    except Exception as e:
        print(f"Readability Error:    {e}")

    print("\nPunctuation Profile:")
    punc_map = stats.punc_freq(content)
    for mark, count in punc_map.items():
        if count > 0:
            print(f"  {mark}: {count}")

    print("\n[II. PSYCHOLINGUISTIC PROFILE]")

    senses = stats.sensory_immersion(words)
    print(
        f"Sensory Words:        Visual({senses['visual']}), Auditory({senses['auditory']}), Tactile({senses['tactile']})")

    ego = stats.pronouns(words)
    print(f"Pronoun Usage:        I/Me({ego['I/Me']}) vs We/Us({ego['We/Us']})")
    modals = stats.modal_verbs(words)
    print(f"Confidence/Modals:    Necessity({modals['necessity']}) vs Possibility({modals['possibility']})")

    print("\n[III. VERIFICATION]")
    try:
        consistency = stats.check_auth(words)
        print(f"Internal Consistency: {consistency:.4f}")
        if consistency > 0.9:
            print("  -> Likely consistent authorship")
        else:
            print("  -> Possible inconsistencies detected")
    except Exception as e:
        print(f"Consistency Error:    {e}")

    print(f"\n{'=' * 15} END REPORT {'=' * 15}\n")


if __name__ == "__main__":
    main()