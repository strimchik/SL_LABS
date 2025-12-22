import csv

def read_csv_file(filename='1.csv'):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []

def print_key_value(data):
    if not data:
        print("Нет данных для отображения")
        return
    
    for i, row in enumerate(data, 1):
        print(f"\nКнига #{i}:")
        for key, value in row.items():
            print(f"  {key} → {value}")

def find_oldest_newest_book(data):
    if not data:
        return None, None
    
    oldest = min(data, key=lambda x: int(x['Year']))
    newest = max(data, key=lambda x: int(x['Year']))
    return oldest, newest

def calculate_total_pages(data):
    if not data:
        return 0
    
    total = sum(int(book['Pages']) for book in data)
    return total

def calculate_average_price(data):
    if not data:
        return 0
    
    prices = [float(book['Price'].replace(',', '.')) for book in data]
    average = sum(prices) / len(prices)
    return average

def count_books_by_genre(data):
    if not data:
        return {}
    
    genre_count = {}
    for book in data:
        genre = book['Genre']
        genre_count[genre] = genre_count.get(genre, 0) + 1
    
    return genre_count

def main():
    data = read_csv_file()
    
    if not data:
        print("Программа завершена из-за отсутствия данных")
        return
    
    print("СОДЕРЖИМОЕ ФАЙЛА 1.CSV:")
    print_key_value(data)
    
    
    print("АНАЛИЗ КНИГ:")
    
    oldest, newest = find_oldest_newest_book(data)
    if oldest and newest:
        print(f"Самая старая книга: '{oldest['Title']}' ({oldest['Year']} год)")
        print(f"Самая новая книга: '{newest['Title']}' ({newest['Year']} год)")
    
    total_pages = calculate_total_pages(data)
    print(f"Общее количество страниц во всех книгах: {total_pages}")
    
    avg_price = calculate_average_price(data)
    print(f"Средняя цена книги: {avg_price:.2f}")
    
    genre_stats = count_books_by_genre(data)
    print("\nКоличество книг по жанрам:")
    for genre, count in genre_stats.items():
        print(f"  {genre}: {count} книг")

if __name__ == "__main__":
    main()