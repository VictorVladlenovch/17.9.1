#функция сортировки методом 'пузырек'
def sort_puzirek(numbers_list_mod):
    for i in range(len(numbers_list_mod)):
        for j in range(len(numbers_list_mod) - i - 1):
            if numbers_list_mod[j] > numbers_list_mod[j + 1]:
                numbers_list_mod[j], numbers_list_mod[j + 1] = numbers_list_mod[j + 1], numbers_list_mod[j]
    return numbers_list_mod

#функция 'бинарного' поиска левого и правого элементов
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
#вводим числа, проверяем правильность данных, сортируем
what = True
while what:
    try:
        numbers_list = input("Введите последовательность натуральных чисел через пробел: ").split()
    #    print('введено:', numbers_list)

    # разделяем по разделителю (пробел) и записываем строку целых чисел
        numbers_list_mod = [int(x) for x in numbers_list]
    #    print('числа:', numbers_list_mod)
    # сортировка
        numbers_list_mod = sort_puzirek(numbers_list_mod)
        print('после сортировки методом пузырек:', numbers_list_mod)

        numbers_user = input("Введите число для определения индекса: ")
        numbers_user = int(numbers_user)
    #    print("введено число ", numbers_user)
        what = False
    except ValueError:
            print(f'Ошибка {ValueError}')
            print('Введено недопустимое значение.')
            what = input("Повторить ввод чисел? (+ или -): ")
            if what != '+':
                print('До свидания')
                what = False
                exit(1)
            else:
                print('В следующий раз будьте внимательнее!')

#проверяем есть ли искомое число в списке
if numbers_user not in numbers_list_mod:
     print(f'Нет числа {numbers_user} среди чисел последовательности. {numbers_list_mod}')
     if numbers_user < min(numbers_list_mod):
           print(f'число {numbers_user} меньше минимального последовательности. {min(numbers_list_mod)}')
     if numbers_user > max(numbers_list_mod):
           print(f'число {numbers_user} больше максимального последовательности {max(numbers_list_mod)}')
     exit(1)

#вызывается функция бинарного поиска левого и правого элементов
number_index = binary_search(numbers_list_mod, numbers_user, 0, len(numbers_list_mod) - 1)

#определяем место искомого числа в списке
print("Индекс введенного числа в списке (от 0): ", number_index)
#анализ числа в списке
if number_index == 0:
    print(f'число {numbers_user} первое значение в списке, следующее {numbers_list_mod[number_index + 1]}')
elif number_index == int(len(numbers_list_mod)-1):
    print(f'число {numbers_user} последнее значение в списке, предыдущее значение {numbers_list_mod[number_index-1]}')
else:
    print(f'предыдущее значение {numbers_list_mod[number_index-1]}, следующее {numbers_list_mod[number_index + 1]}')
