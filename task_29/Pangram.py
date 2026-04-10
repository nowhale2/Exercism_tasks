def is_pangram(sentence):
    sentence_lower = sentence.lower()
    
    # Оставляем только буквы английского алфавита и собираем уникальные
    unique_letters = set(char for char in sentence_lower if 'a' <= char <= 'z')
    # Проверяем, что всех букв 26
    return len(unique_letters) == 26
