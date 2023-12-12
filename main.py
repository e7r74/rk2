import requests
import json

class Fruit:
    def __init__(self, name, family, order, nutrition):
        self.name = name
        self.family = family
        self.order = order
        self.nutrition = nutrition

    def __str__(self):
        return f"{self.name} - Family: {self.family}, Order: {self.order}, Nutrition: {self.nutrition}"

def get_fruits_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: Невозможно получить данные. Код статуса: {response.status_code}")
        return None

def create_fruit_objects(fruits_data):
    fruits = []
    for fruit_data in fruits_data:
        fruit = Fruit(
            name=fruit_data['name'],
            family=fruit_data['family'],
            order=fruit_data['order'],
            nutrition=fruit_data['nutrition']
        )
        fruits.append(fruit)
    return fruits

def save_fruits_to_file(fruits, filename):
    with open(filename, 'w') as file:
        data_to_save = []
        for fruit in fruits:
            fruit_data = {
                'name': fruit.name,
                'family': fruit.family,
                'order': fruit.order,
                'nutrition': fruit.nutrition
            }
            data_to_save.append(fruit_data)
        json.dump(data_to_save, file, indent=4)

def read_fruits_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data


api_url = "https://www.fruityvice.com/api/fruit/all"
fruits_data = get_fruits_data(api_url)

if fruits_data:
    
    fruits = create_fruit_objects(fruits_data)

    
    save_fruits_to_file(fruits, 'fruits_data.json')
    print("Данные о фруктах сохранены в файл 'fruits_data.json'.")

    
    read_data = read_fruits_from_file('fruits_data.json')
    print("\nДанные о фруктах прочитаны из файла 'fruits_data.json':")
    for item in read_data:
        print(item)
else:
    print("Невозможно продолжить без данных.")
