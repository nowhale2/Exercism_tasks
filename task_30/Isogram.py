def is_isogram(string):
    text_lower = string.lower()
    
    # Оставляем только буквы (английские и русские)
    letters_only = [char for char in text_lower if char.isalpha()]
    
    # Собираем уникальные буквы
    unique_letters = set(letters_only)
    # Если количество букв равно количеству уникальных — повторов нет
    return len(letters_only) == len(unique_letters)
