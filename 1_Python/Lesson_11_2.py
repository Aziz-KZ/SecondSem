import collections

pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "Желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}},
    3: {"Саймон": {"Вид питомца": "Кот", "Возраст питомца": 14, "Имя владельца": "Лена"}}
}

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    return pets.get(ID, False)

def pets_list():
    for ID, pet_data in pets.items():
        for name, info in pet_data.items():
            age_suffix = get_suffix(info['Возраст питомца'])
            print(f"ID: {ID}, Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {age_suffix}. Имя владельца: {info['Имя владельца']}.")

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    name = input("Введите кличку питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}}
    print(f"Запись добавлена с ID {new_id}.")

def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if pet:
        for name, info in pet.items():
            age_suffix = get_suffix(info['Возраст питомца'])
            print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {age_suffix}. Имя владельца: {info['Имя владельца']}.")
    else:
        print("Питомец с таким ID не найден.")

def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        species = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner = input("Введите новое имя владельца: ")
        pets[ID] = {name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}}
        print("Информация обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    if ID in pets:
        del pets[ID]
        print("Запись удалена.")
    else:
        print("Питомец с таким ID не найден.")

while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
    if command == 'stop':
        break
    elif command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда.")