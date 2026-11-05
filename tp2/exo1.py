from collections import Counter

text = "NLP is fun!"
characters = list(text)

print("1) Characters:", characters)
print("   Number of characters:", len(characters))


no_spaces = [char for char in characters if char != " "]

print("\n2) Without spaces:", no_spaces)
print("   Number of characters:", len(no_spaces))


def char_frequency(text):
    freq = {}

    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    return freq


sentence = "Natural language processing is fascinating!"
freq = char_frequency(sentence)

print("\n3) freq:", freq)

top_three = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:3]

print("\n4) Three most frequent letters:")
for letter, count in top_three:
    print(f"   {letter!r}: {count}")


def char_frequency2(text):
    return Counter(char for char in text.lower() if char.isalpha())


top_three = char_frequency2(sentence).most_common(3)

print("\n5) Three most frequent letters (Counter):")
for letter, count in top_three:
    print(f"   {letter!r}: {count}")
