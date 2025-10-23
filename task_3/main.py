#Специан Захар 1 Вариант
def item_print(item):                                                      #функция, выводящая всю инфу о рыбе
    print(f"""{"-"*40}
Номер - {item["id"]}
Название - {item['name']}
Латинское название - {item["latin_name"]}
Живет в соленой воде - {item["is_salt_water_fish"]}
Количество подвидов - {item["sub_type_count"]}
{"-"*40}""")
 
import json                                                               #импортируем модуль джсон + переменная для подсчета операций
operations = 0 

with open("fish.txt", "r", encoding="utf-8") as file:                     #открываем файл для чтения и делаем из него .json и запихиваем в контент
 content = json.load(file)


def import_text(content):                                                 #фунция которая собирает всю инфу о рыбе и заносит в базу
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

while True:                                                                #бесконечный цикл чтоб менюшка не пропадала
  with open("fish.txt", "r", encoding="utf-8") as file:                    #открываем и обновляем инфу о файле для переменной контент
   content = json.load(file)                                               
  print("""                                                                
      1 - Вывести все записи
      2 - Вывести запись по полю
      3 - Добавить запись
      4 - Удалить запись по полю
      5 - Выйти из программы""")
  number = int(input("Введите число исходя из пункта меню: "))             #выводим менюшку
  if number == 1:                                                          #если выбрали пункт 1 то выводим всю инфу из базы
        operations += 1
        for item in content:
            item_print(item)
        
            
  elif number == 2:                                                       #если пункт 2 то запрашиваем id и вывовдим поле только с нужным id
        operations += 1
        field_id = int(input("Введите id выводимого поля: "))
        for index, item in enumerate(content):
            if item["id"] == field_id:
                print("-"*40)
                print(f"Индекс данного поля в словаре: {index}")
                item_print(item)
                
               
  elif number == 3:                                                       #если пункт 3 то с помощью функции import_text вводим новые данные и обновляем значение контент
         operations += 1
         content = import_text(content)
         print("Файл успешно изменен, добавления можно посмотреть в 1 пункте меню ")
         
  elif number == 4:                                                       #если пункт 4 то удаляем элемент по id и сохраняем изменения
        operations += 1
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
                
                    
                    
                    
  elif number == 5:                                                        #если пункт 5 то просто выходим из меню и выводим количество сделанных операций
    operations += 1
    print(f"\nВы вышли из меню, количество сделанных операций = {operations}") 
    break

  else:
        print("Неверный выбор из пункта меню")                             #если цифра введена не из пункта меню то выводим об этом сообщение
