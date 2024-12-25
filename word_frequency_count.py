import string
from collections import Counter

stop_words = set([
    'он', 'бою', 'на', 'всегда', 'в', 'для', 'о', 'по', 'это', 'или', 'быть', 'забыл', 'добавить', 'подсказку', 'потому', 'что', 'опилки', 'вместо', 'мозгов'
])

def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text.lower()

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def filter_words(text, stop_words):
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
    return filtered_words

def count_word_frequencies(filtered_words):
    word_counts = Counter(filtered_words)
    return word_counts

def print_most_common_words(word_counts, top_n=5):
    most_common_words = word_counts.most_common(top_n)
    print(f"Top {top_n} catchwords:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

def main(file_path, top_n=5):
    text = read_file(file_path)
    if text:
        cleaned_text = clean_text(text)
        filtered_words = filter_words(cleaned_text, stop_words)
        word_counts = count_word_frequencies(filtered_words)
        print_most_common_words(word_counts, top_n)
    
file_path = 'file name or file path' 
main(file_path, top_n=5)

