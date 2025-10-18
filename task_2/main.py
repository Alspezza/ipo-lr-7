#Специан Вариант1
import json #Вводим модуль json
exist = 0   #создаем переменную существования, начинаем код
print("Start code: ")
#открываем текстовый файл с содержимым
file = open(r"C:\Users\user\Desktop\Лабы и тп\ИПО\lr7\ipo-lr-7\text.txt" , "r", encoding="utf-8")
#даем переменной content весь текст как список в пайтоне
content = json.load(file)
#вводим код профессии
number = str(input("Введите номер квалификации: "))
#проходимся по всем элементам файла
for item in content:
#цикл который проверяет есть ли в обьекте ключ с названием data.skill и присваиваем переменным нужные для нас значения
    if item.get("model") == "data.skill": 
        fields = item.get("fields", {})
        code = fields.get("code")
        title = fields.get("title")
#если введенный код специальности совпадает, то выводим эту специальность
        if code == number:
            exist = 1
            print("-"*20 +"Найдено"+ "-"*20)
            print(f"{code} >> Название специальности: '{title}'")
            print("-"*50)  
#проверяем существует ли специальность через значение пременной exist и если ее нет то выводим ее отсутствие  
if exist != 1:
    print('-'*20+ "Файл не найден" + '-'*20)
print("End code")
file.close()
