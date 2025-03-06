# 1. Створення змінних різних типів
string_var = "Hello, Python!"
integer_var = 42
float_var = 3.14
bool_var = True
list_var = [1, 2, 3]
dict_var = {"name": "Alice", "age": 25}
tuple_var = (4, 5, 6)
none_var = None

# 2. Порівняння значень
print(integer_var > 10)  # Порівняння чисел
print(string_var == "Hello, Python!")  # Порівняння рядків
print(bool_var == False)  # Порівняння булевих значень
print(list_var == [1, 2, 3])  # Порівняння списків
print(dict_var == {"name": "Alice", "age": 25})  # Порівняння словників
print(tuple_var == (4, 5, 6))  # Порівняння кортежів

# 3. Робота з рядками
num_str = 125
num_str = str(num_str)  # Переведення числа в рядок
print(num_str, type(num_str))

message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')  # Заміна символів
print(message)

split_test = 'This is a split test'
split_list = split_test.split()  # Розділення рядка по пробілах
string_join = ' '.join(split_list)  # Об'єднання списку в рядок
print(string_join)

length = len(string_join)  # Визначення довжини рядка
print(length)

# 4. Робота зі списками
list_append = [1, 2, 3]
list_append.append(4)  # Додавання елемента 4
list_append.append(5)  # Додавання елемента 5
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])  # Розширення списку
print(list_extend)

index = list_extend.index(6)  # Визначення індексу елемента 6
print(index)

list_length = len(list_append)  # Визначення довжини списку
print(list_length)

# 5. Робота зі словниками
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test['where'])  # Виведення значень за ключами

print(dict_test.keys())  # Виведення ключів
print(dict_test.values())  # Виведення значень

print(dict_test.items())  # Виведення пар ключ-значення