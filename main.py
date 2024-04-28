# Comment
#print("Hello Python", 5.5, sep=", ", end=".")
#("\n") # Пропуск між рядками коду (1 або безліч)
#print("\t") # Відступ від краю (АБЗАЦ)
#print('John\'s book')
#print("John\"s book")
#input("Enter number:")

#num = 5
#(num)
#number = 10
#print(number)

#num = int(input ("Enter num: "))

# ==, !=, <, >, <=, >=
#if num >= 55:
    #print("Yes")
    #if num == 100:
        #print("Num is 100")
        #else:
# print("Else")

# Цикл for
#for i in range(-5, 16, 5): # -5 - від, 16 - до, 5 - діапазон циклу перевірки
    #print("El:", i)

#print("\n\n")

#word = 'Some text'
#for i in word: # перевірка тексту
    #if i == 'm':
        #print('Літера m є у слові')

# Цикл while
#i = 100
#while i >= 10:
    #print(i)
    #i -= 10

# Практичне використання
#work = True
#while work:
    #user_input = input("Enter word STOP: ")
    #if user_input == 'STOP':
        #work = False

#print("While loop is done")

# Оператори в циклах
#for i in range(1, 11):
    #if i % 2 == 0:
        #continue
    #if i == 7:
        #break
    #print(":El:", i)


# Else в циклі
#for i in "Hello world":
    #if i == 'm':
        #print("Done")
        #break
#else:
    #print("Not found")

# Списки з даними
#nums = [5, 7, -4, 5.45, 6, 6] # Значення розташовані по індексу (від 0)
#nums[0] = 34.34
#print(nums[3])
#nums2 = [5, 7, 3, [5, "Text", True]]
#print(nums2[-2])
#nums.append(45) # Додати значення в кінець списку
#nums.insert(1, False) #False = 0, True = 1 # Додати значення по індексу
#nums.extend(nums2) # Додавання списків
#nums.sort()
#nums.pop(1) # Видалення значення із списку по індексу
#nums.remove(34.34) # Видалення певного значення із списку
#nums.clear()

#print(nums.count(6)) # Знайти кількість певних значень у списку
#print(len(nums)) # Дізнитись довжину списку
#print(nums2)

# Списки та цикли
#nums = [5, 7, -4, 5.45, 6, 6]
#for el in nums:
    #res = el ** 2
    #print(res)

# Практичне використання
#user_count_hobby = int(input("Enter hobby number: "))
#i = 0
#hobby = []
#while i < user_count_hobby:
    #text = "Enter hobby" + str(i + 1) + ": "
    #hobby.append(input(text))
    #i +=1
#print(hobby)

# Робота з текстом
#word = list('itproger') #list - Перетворення тексту в список # Всі функції для списків підходять і для тексту!
#word [0] = 'I'
#word.append('!')
#result = ''.join(word) # join - з'єднання
#print(result) # .upper() всі символи у верхній регістр, .lower() всі символи у нижній регістр, .capitalize() всі перші символи будь яких слів у верхній регістр
# print(result. isupper()) - Перевірка чи всі символи у верхньому регістрі
# print(result. islower()) - Перевірка чи всі символи у нижньму регістрі

#text = 'football,basketball,skate,drive'
#hobbies = text.split(',')

#for i in range(0, len(hobbies)):
#    hobbies[i] = hobbies[i].capitalize()
#result = ",".join(hobbies)
#print(result)

# Індекси та зрізи
#lis = [5, 3, True, "Some", [5, 4]]
#print(lis[:-4:-1])

# Кортежи ті самі списки, але ми не можемо змінювати їх
#nums = [5, 6]
#data = tuple(nums) # tuple переклад кортеж, перетворення списків у кортеж
#print(data)

#Словники
#person = {'name': 'Alex', 'age': 15, 5:12, True: 'Folse', (3, 5): 45} # Перший спосіб створення словника.
#person[5] = 'Five' # У будь який момент коду можемо замінити значення словника.
#print(person[5]) #Звернення до словника не за індексом а за ключем
#person1 = dict(name='Alex', age=15) #Другий спосіб створення словника.
#print(person1['age'])

#for key, values in person.items(): # Цикл який перебирає як ключі так і значення
    #print(key, values, sep=" - ")

#for el in person.keys(): # Цикл який перебирає лише ключі, або (person.volues(): цикл який перебирає лише значенння)
    #print(el)

# person.clear() = видалення (очищення) словника.
# print(person.get('name')) = print(person['name']) Звернення до словника.
# person.pop(5) - Видалення елементу із словника по ключу
#person['bio'] = 'Text' # Додавання елементів до словника

#Великий словник
# people = {
#   'user_1': {
#     'name': 'John',
#       'age': 27,
#       'address': ('Seattle', 'Some streat', 6635),
#       'grades': {'math': 5, 'physics': 2}
#   }
   #'user_2': {
#       'surname': 'Doe',
#       'name': 'Alex'
#   }#   }#print(people['user_1'])

# Створення функції
#def name():                      def - cтворення свої функцій, name - назва функції, все решта це тіло функції
    #print("Hello", end="")
    #print("!")

#Робота з файлами
#data = input("Hobby: ")
#file = open('data/myfile.txt', 'r') # 'w' - Запис інформації у файл, з видаленням попередніх записів;
# 'r' - зчитування, читання файлу; 'a' - Додавання тексту до існуючого '+' - створення нового файлу;
#file.write(data + '\n')
#print(file.read())
#file.close()


# Обробка винятків
#num = None

#while num == None:
    #try:
        #num = int(input("Enter num:"))
        #num += 5
        #print(num)
    #except ValueError:
        #print("Ви ввели щось не так")
    #except SyntaxError:
        #print('Перевірте код на коректність')
    #else:
        #print('Ви молодець!')


# Менеджер With...as самостійно закриває файл після роботи з ним
#try:
    #with open('data/myfile.txt', 'r', encoding='utf-8') as file: # encoding='utf-8' - Використовується для коректної обробки тексту українською.
        #print(file.read())

#тут буде нова функція!
