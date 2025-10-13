#Специан Вариант1
import json
print("Start code: ")
file = open(r"C:\Users\SpetsZak_88\Desktop\lr7\task_2\text.txt", "r", encoding="utf-8")
content = json.load(file)
number = input("Введите номер квалификации: ")
for item in content:
    if item.get("model") == "data.skill" and item.get("specialty") == number:
        print("=============== Найдено ===============")
        print(item["title"])
        
        
 

file.close()
