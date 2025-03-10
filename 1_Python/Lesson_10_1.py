pets = {}

species = input("Введите вид питомца: ")
name = input("Введите кличку питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

if age % 10 == 1 and age % 100 != 11:
    age_word = "год"
elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
    age_word = "года"
else:
    age_word = "лет"

pets[name] = {
    "Вид питомца": species,
    "Возраст питомца": age,
    "Имя владельца": owner
}

pet_name = list(pets.keys())[0]
pet_info = list(pets.values())[0]

print(f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_info['Возраст питомца']} {age_word}. Имя владельца: {pet_info['Имя владельца']}.")

print(pets)