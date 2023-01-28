# Функция для определения цифр в строке ввода
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        print(f'Ошибка {ValueError}')
        print('Введено недопустимое значение (не целое число). В следующий раз будьте внимательнее!')
        exit(1)
#        return False

#функция сортировки методом пузырек
def sort_puzirek(numbers_list_mod):
    for i in range(len(numbers_list_mod)):
        for j in range(len(numbers_list_mod) - i - 1):
            if numbers_list_mod[j] > numbers_list_mod[j + 1]:
                numbers_list_mod[j], numbers_list_mod[j + 1] = numbers_list_mod[j + 1], numbers_list_mod[j]
    return numbers_list_mod

#функция бинарного поиска левого и правого элементов
def binary_search(numbers_list_mod, numbers_user, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if numbers_list_mod[middle] == numbers_user:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif numbers_user < numbers_list_mod[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(numbers_list_mod, numbers_user, left, middle - 1)
    else:  # иначе в правой
        return binary_search(numbers_list_mod, numbers_user, middle + 1, right)

#тело программы
#вводим числа
numbers_list = input("Введите последовательность целых чисел через пробел: ")

#проверяем, что введены числа
if is_int(numbers_list):
    print('введены числа:', numbers_list)

# разделяем по разделителю (пробел) и записываем строку целых чисел
numbers_list_mod = [int(x) for x in numbers_list.split()]

numbers_list_mod = sort_puzirek(numbers_list_mod) #отсортирована
print('после сортировки методом пузырек:', numbers_list_mod)
#
numbers_user = input("Введите число для определения индекса: ")
#проверяем, что введено число
if is_int(numbers_user):
     print("введено число ", numbers_user)
     numbers_user = int(numbers_user)

#проверяем есть ли искомое числов списке
if numbers_user not in numbers_list_mod:
     print('Нет такого числа среди введенных. ')
     exit(1)

#вызывается функция бинарного поиска левого и правого элементов
number_index = binary_search(numbers_list_mod, numbers_user, 0, len(numbers_list_mod) - 1)

print("Индекс введенного числа в списке (от 0): ", number_index)

if number_index == 0:
    print(f'число {numbers_user} первое значение в списке, следующее {numbers_list_mod[number_index + 1]}')
elif number_index == int(len(numbers_list_mod)-1):
    print(f'число {numbers_user} последнее значение в списке, предыдущее значение {numbers_list_mod[number_index-1]}')
else:
    print(f'предыдущее значение {numbers_list_mod[number_index-1]}, следующее {numbers_list_mod[number_index + 1]}')
