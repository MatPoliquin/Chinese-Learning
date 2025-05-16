import jieba
from collections import Counter

def count_chinese_words_and_characters_from_file(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Use jieba to cut the text into words
    words = jieba.lcut(text)

    # Filter out any spaces or empty strings, if necessary
    words = [word for word in words if word.strip()]

    # Count total words
    total_words = len(words)

    # Count unique words
    unique_words = len(set(words))

    # Count total characters (excluding spaces and newlines)
    characters = [char for char in text if char.strip()]
    total_characters = len(characters)

    # Count unique characters
    unique_characters = len(set(characters))

    # Count frequency of each word
    word_freq = Counter(words)

    # Get top 100 most common words
    top_100_words = word_freq.most_common(100)

    return total_words, unique_words, total_characters, unique_characters, top_100_words

if __name__ == "__main__":
    file_path = './subtitles/tmnt-tv/tmnt-se01-e01-translation.txt'  # Replace this with your file path
    total_words, unique_words, total_characters, unique_characters, top_100_words = count_chinese_words_and_characters_from_file(file_path)

    print(f"Total number of words: {total_words}")
    print(f"Number of unique words: {unique_words}")
    print(f"Total number of characters: {total_characters}")
    print(f"Number of unique characters: {unique_characters}")
    print("\nTop 100 most frequent words:")
    for word, freq in top_100_words:
        print(f"{word}: {freq}")


