import pytest
import re


# Функція для підрахунку слів і речень
def count_words_and_sentences(text):
    words = re.split(r'[\s,;:]+', text.strip())
    words = [word for word in words if word]  # Видаляємо порожні елементи

    # Для розділення на речення враховуємо крапку, знак оклику, питання та троє крапок
    sentences = re.split(r'(?<=[.!?…])\s+', text.strip())
    sentences = [sentence for sentence in sentences if sentence]  # Видаляємо порожні елементи

    return len(words), len(sentences)


# Фікстура для створення тестових даних
@pytest.fixture
def sample_text():
    return "Привіт, світ! Це тестовий файл. Він містить три речення... Чи все працює?"


# Параметризовані тести
@pytest.mark.parametrize("text, expected_words, expected_sentences", [
    ("Одна пропозиція.", 2, 1),
    ("Дві пропозиції! Ось ще одна?", 5, 2),
    ("Слово", 1, 1),
    ("", 0, 0),
    ("Перше речення... Друге речення? Третє речення!", 6, 3)
])
def test_count_words_and_sentences(text, expected_words, expected_sentences):
    words_count, sentences_count = count_words_and_sentences(text)
    assert words_count == expected_words, f"Expected {expected_words}, got {words_count}"
    assert sentences_count == expected_sentences, f"Expected {expected_sentences}, got {sentences_count}"


# Тестування з використанням фікстури
def test_with_sample_text(sample_text):
    words_count, sentences_count = count_words_and_sentences(sample_text)
    print(f"Кількість слів: {words_count}")
    print(f"Кількість речень: {sentences_count}")
    assert words_count == 12
    assert sentences_count == 4  # Очікуємо 4 речення