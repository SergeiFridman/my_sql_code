# Списки (dict)

# cars = {
#     "Tesla Model 3": {"engine": "Electric", "power": 283},
#     "BMW 3 Series": {"engine": "Gasoline", "power": 255},
#     "Audi A6": {"engine": "Diesel", "power": 201},
#     "Toyota Corolla": {"engine": "Gasoline", "power": 139},
#     "Nissan Leaf": {"engine": "Electric", "power": 147}
# }
#
# models = list(cars.keys())
#
# # Выводим список моделей с номерами
# print("Выберите модель автомобиля:")
# for i, model in enumerate(models, 1):
#     print(f"{i}. {model}")
#
# # Цикл для ввода корректного номера
# while True:
#     try:
#         choice = int(input("Введите номер (1-5): "))
#         if 1 <= choice <= len(models):
#             break  # корректный номер, выходим из цикла
#         else:
#             print("Некорректный номер, попробуйте снова.")
#     except ValueError:
#         print("Введите число от 1 до 5!")
#
# # Вывод выбранной модели
# selected = models[choice - 1]
# specs = cars[selected]
# print(f"\n{selected}: {specs['power']} л.с., {specs['engine']}")

# Списки (массивы)
models = ["Tesla Model 3", "BMW 3 Series", "Audi A6", "Toyota Corolla", "Nissan Leaf"]
powers = [283, 255, 201, 139, 147]
engines = ["Electric", "Gasoline", "Diesel", "Gasoline", "Electric"]

# Выводим список моделей с номерами
print("Выберите модель автомобиля:")
for i, model in enumerate(models, 1):
    print(f"{i}. {model}")

# Цикл для ввода корректного номера
while True:
    try:
        choice = int(input("Введите номер (1-5): "))
        if 1 <= choice <= len(models):
            break
        else:
            print("Некорректный номер, попробуйте снова.")
    except ValueError:
        print("Введите число от 1 до 5!")

# Вывод выбранной модели
index = choice - 1
print(f"\n{models[index]}: {powers[index]} л.с., {engines[index]}")