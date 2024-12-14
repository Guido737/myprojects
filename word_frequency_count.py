import string
from collections import Counter

stop_words = set([
    'он', 'бою', 'на', 'всегда', 'в', 'для', 'о', 'по', 'это', 'или', 'быть', 'забыл', 'добавить', 'подсказку', 'потому', 'что', 'опилки', 'вместо', 'мозгов'
])



def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text.lower()

def count_words(file_path, top_n=5):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(top_n)
    
    print(f"Top {top_n} catchwords:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
        
file_path = 'file name or file path' 
count_words(file_path, top_n=5)

