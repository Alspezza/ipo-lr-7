#Специан Захар 1 Вариант
def item_print(item):  #функция, выводящая всю инфу о рыбе
    print(f"""{"-"*40}
Номер - {item["id"]}
Название - {item['name']}
Латинское название - {item["latin_name"]}
Живет в соленой воде - {item["is_salt_water_fish"]}
Количество подвидов - {item["sub_type_count"]}
{"-"*40}""")
 
def first(content):    #функция первого пункта меню
    for item in content:
            item_print(item)

def second(content):  #функция второго пункта меню
    
    field_id = int(input("Введите id выводимого поля: "))
    for index, item in enumerate(content):
        if item["id"] == field_id:
                print("-"*40)
                print(f"Индекс данного поля в словаре: {index}")
                item_print(item)

def third(content):  #функция третьего пункта меню
    
    content = import_text(content)
    print("Файл успешно изменен, добавления можно посмотреть в 1 пункте меню ")

def fourth(content):  #функция четвертого пункта меню
    
    delete_id = int(input("Введите id удаляемого элемента: "))
    for i,item in enumerate(content):
            if item["id"] == delete_id:
                item_print(item)
                agreement = input("Вы уверены что хотите удалить это поле?").strip().lower()
                if agreement == "да" :
                    del content[i]
                    with open("fish.txt", "w", encoding="utf-8") as file:
                        json.dump(content, file, ensure_ascii = False, indent = 2)
                        print("Файл успешно изменен")
                if agreement == "нет" :
                    print("Удаление отменено")

def fifth(operations):  #функция пятого пункта меню
    print(f"\nВы вышли из меню, количество сделанных операций = {operations}") 
    

import json                                                               #импортируем модуль джсон + переменная для подсчета операций
with open("fish.txt", "r", encoding="utf-8") as file:                     #открываем файл для чтения и делаем из него .json и запихиваем в контент
 content = json.load(file)


def import_text(content):  #фунция которая собирает всю инфу о рыбе и заносит в базу
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
    with open("fish.txt", "w", encoding="utf-8") as file:
        json.dump(content, file, ensure_ascii=False, indent = 2)
    print("Файл сохранен")
    return content

def menu():  #функция меню
  operations = 0
  while True:
   with open("fish.txt", "r", encoding="utf-8") as file:                    #открываем и обновляем инфу о файле для переменной контент
    content = json.load(file)                                           
   print("""                                                                
      1 - Вывести все записи
      2 - Вывести запись по полю
      3 - Добавить запись
      4 - Удалить запись по полю
      5 - Выйти из программы""")
   number = int(input("Введите число исходя из пункта меню: "))             #выводим менюшку
   if number == 1:   
        operations += 1                                                       #если выбрали пункт 1 то выводим всю инфу из базы
        first(content)
                 
   elif number == 2:   
        operations += 1                                                    #если пункт 2 то запрашиваем id и вывовдим поле только с нужным id
        second(content)
                
               
   elif number == 3:   
        operations += 1                                                    #если пункт 3 то с помощью функции import_text вводим новые данные и обновляем значение контент
        third(content)
         
   elif number == 4:        
        operations += 1                                               #если пункт 4 то удаляем элемент по id и сохраняем изменения
        fourth(content)
                                 
   elif number == 5:                                                        #если пункт 5 то просто выходим из меню и выводим количество сделанных операций
    fifth(operations)
    break

   else:
        print("Неверный выбор из пункта меню")

menu()    #вызов функции меню