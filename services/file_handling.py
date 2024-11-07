import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text, start, page_size):
    # Устанавливаем конец страницы как минимум до конца текста
    end = start + page_size
    if end > len(text):
        end = len(text)

    # Срез текста от начального индекса до конечного
    page_text = text[start:end]

    # Находим последний знак препинания в тексте страницы
    punctuation_marks = {',', '.', '!', ':', ';', '?'}
    last_punctuation_index = -1

    for i in range(len(page_text) - 1, -1, -1):
        if page_text[i] in punctuation_marks:
            last_punctuation_index = i
            break

    # Если знак препинания найден, обрезаем текст до него
    if last_punctuation_index != -1:
        page_text = page_text[:last_punctuation_index + 1]

    # Возвращаем текст страницы и его размер в символах
    return page_text, len(page_text)


PAGE_SIZE = 1050  # Размер страницы
book = {}  # Словарь для хранения страниц книги

# Функция, формирующая словарь книги

def prepare_book(path):
    with open(path, encoding='utf-8') as file:
        text = file.read()  # Читаем весь текст книги

    start = 0  # Начальный индекс для извлечения текста
    page_number = 1  # Номер страницы

    while start < len(text):  # Пока есть текст для обработки
        part_text, length = _get_part_text(text, start, PAGE_SIZE)  # Получаем часть текста
        part_text = part_text.lstrip()  # Удаляем лишние символы в начале текста
        book[page_number] = part_text  # Заполняем словарь
        start += length  # Обновляем начальный индекс для следующей страницы
        page_number += 1  # Увеличиваем номер страницы


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
