import json

def read_json_file(filename='1.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['users']

def find_users_by_surname_prefix(data, prefix):
    prefix = prefix.lower()[:3]
    return [user for user in data if user['surname'].lower().startswith(prefix)]

def calculate_average_age(data):
    ages = [user['age'] for user in data]
    return sum(ages) / len(ages)

def count_users_by_language(data):
    languages = {}
    for user in data:
        lang = user['language']
        languages[lang] = languages.get(lang, 0) + 1
    return languages

def save_filtered_data(data, filename='out.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def main():
    data = read_json_file()
    
    
    prefix = input("Введите начало фамилии(3 буквы): ")
    found_users = find_users_by_surname_prefix(data, prefix)
    
    print(f"\nНайдено пользователей: {len(found_users)}")
    for user in found_users:
        print(f"{user['surname']} {user['name']}, возраст: {user['age']}, язык: {user['language']}")
    
    avg_age = calculate_average_age(data)
    print(f"\nСредний возраст пользователей: {avg_age:.1f}")
    
    lang_stats = count_users_by_language(data)
    print("\nКоличество пользователей по языкам:")
    for lang, count in lang_stats.items():
        print(f"  {lang}: {count}")
    
    filtered_data = {
        'found_users': found_users,
        'average_age': avg_age,
        'languages': lang_stats,
        'total_users': len(data)
    }
    
    save_filtered_data(filtered_data)
    print(f"\nОтфильтрованные данные сохранены в out.json")

if __name__ == "__main__":
    main()