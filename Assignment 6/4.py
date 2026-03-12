from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    word_count = Counter(words)
    total_words = len(words)

    most_common = word_count.most_common(5)
    top_5_count = sum(count for word, count in most_common)

    proportion = (top_5_count / total_words) * 100 if total_words > 0 else 0

    print("Top 5:", dict(most_common))
    print(f"Total number of words: {total_words}")
    print(f"Proportion of 5 most common words: {top_5_count} / {total_words} = {proportion:.2f}%")

text = "I will eat a apple today, after eating it, it tasted verry sweet, I will eat a apple again tomorrow"
word_frequency(text)