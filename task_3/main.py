#Специан Захар 1 Вариант
def item_print(item):
    print(f"""{"-"*40}
Номер - {item["id"]}
Название - {item['name']}
Латинское название - {item["latin_name"]}
Живет в соленой воде - {item["is_salt_water_fish"]}
Количество подвидов - {item["sub_type_count"]}
{"-"*40}""")


import json
file = open(r"C:\Users\user\Desktop\Лабы и тп\ИПО\lr7\ipo-lr-7\task_3\fish.txt", "r", encoding="utf-8")
content = json.load(file)


def import_text(content):
    print("| Вводите по порядку нужные данные |")
    new_id = int(input("Введите новое id для рыбы: "))
    for item in content:
        if item["id"] == new_id:
            print("Данное id уже существует")
            return content
    new_name = input("Введите название рыбы: ")
    new_latin_name = input("Введите латинское название рыбы: ")
    water_input = input("Рыба живет в соленой воде?(true / false): ")
    if water_input == "true":
        new_is_salt_water_fish = True
    elif water_input == "false":
        new_is_salt_water_fish = False
    else:
        print("Неправильно введена пресноводность рыбы")
        return content
    new_sub_type_count = int(input("Введите колво подвидов рыбы: "))
    new_field = {
    "id": new_id,
    "name": new_name,
    "latin_name": new_latin_name ,
    "is_salt_water_fish": new_is_salt_water_fish ,
    "sub_type_count": new_sub_type_count
    }
    content.append(new_field)
    with open(r"C:\Users\user\Desktop\Лабы и тп\ИПО\lr7\ipo-lr-7\task_3\fish.txt", "w", encoding="utf-8") as file:
        json.dump(content, file, ensure_ascii=False, indent = 2)
    print("Файл сохранен")


print("""1 - Вывести все записи
      2 - Вывести запись по полю
      3 - Добавить запись
      4 - Удалить запись по полю
      5 - Выйти из программы""")
number = int(input("Введите число исходя из пункта меню: "))
match number:
    case 1:
        for item in content:
            item_print(item)
    case 2:
        field_id = int(input("Введите id выводимого поля: "))
        for index, item in enumerate(content):
            if item["id"] == field_id:
                print("-"*40)
                print(f"Индекс данного поля в словаре: {index}")
                item_print(item)
    case 3:
         import_text(content)


    case _:
        print("Неверный выбор из пункта меню")
file.close()
