def count_words():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        print("Ошибка чтения файла")
        return
    
    if not lines:
        print("Файл пустой")
        return
    
    word_counts = []
    for i, line in enumerate(lines, 1):
        words = line.strip().split()
        word_counts.append((i, len(words)))
    
    with open('output.txt', 'w', encoding='utf-8') as f:
        for line_num, count in word_counts:
            f.write(f"Строка {line_num}: {count} слов\n")
    
    for line_num, count in word_counts:
        print(f"Строка {line_num}: {count} слов")

if __name__ == "__main__":
    count_words()