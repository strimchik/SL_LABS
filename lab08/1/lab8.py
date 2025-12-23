import requests
import json

def get_countries():
    url = "https://restcountries.com/v3.1/region/asia"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except:
        print("Ошибка при получении данных")
        return None

def filter_countries(countries):
    result = []
    for country in countries:
        population = country.get('population', 0)
        if population <= 30000000:
            continue
        
        area = country.get('area', 0)
        density = round(population / area, 2) if area > 0 else 0
        
        country_data = {
            'name': country.get('name', {}).get('common', 'Unknown'),
            'capital': country.get('capital', ['Unknown'])[0],
            'area': area,
            'population': population,
            'density': density,
            'flag': country.get('flags', {}).get('png', '')
        }
        result.append(country_data)
    
    return result

def save_json(data, filename='countries.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Сохранено в {filename}")
    except:
        print("Ошибка сохранения файла")

def download_flag(url, name):
    if not url:
        return False
    
    try:
        response = requests.get(url)
        filename = f"flag_{name.replace(' ', '_')}.png"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Флаг {name} скачан")
        return True
    except:
        return False

def show_top(data, count=5):
    sorted_data = sorted(data, key=lambda x: x['density'], reverse=True)
    top = sorted_data[:count]
    
    print("\nТоп стран по плотности населения:")
    for i, country in enumerate(top, 1):
        print(f"{i}. {country['name']} - {country['density']} чел/км²")
    
    return top

def main():
    print("Анализ азиатских стран")
    
    countries = get_countries()
    if not countries:
        return
    
    filtered = filter_countries(countries)
    print(f"Найдено стран: {len(filtered)}")
    
    save_json(filtered)
    
    top_countries = show_top(filtered, 5)
    
    print("\nСкачивание флагов:")
    for country in top_countries:
        download_flag(country['flag'], country['name'])

if __name__ == "__main__":
    main()