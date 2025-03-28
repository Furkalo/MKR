import re

def count_words_and_sentences(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        words = re.split(r'[\s,;:]+', text)
        words = [word for word in words if word]

        sentences = re.split(r'(?<=[.!?…])\s+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        return len(words), len(sentences)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None, None

if __name__ == "__main__":
    filename = input("Введіть назву файлу: ")
    word_count, sentence_count = count_words_and_sentences(filename)
    if word_count is not None and sentence_count is not None:
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")