right = 0 # - переменные счетчиков правильных ответов
wrong = 0 # - переменные счетчиков неправильных ответов
age = 1
answer = 1
while age:
    age = int(input("Год рождения Джони Деппа? "))
    if age == 1963:
        print(True)
        right += 1  # - счетчик правильных ответов
    else:
        print(False)
        wrong += 1  # - счетчик неправильных ответов
    age = int(input("Год рождения Мадонны? "))
    if age == 1958:
        print(True)
        right += 1  # - счетчик правильных ответов
    else:
        print(False)
        wrong += 1  # - счетчик неправильных ответов
    age = int(input("Год рождения Дженифер Лопес? "))
    if age == 1969:
        print(True)
        right += 1  # - счетчик правильных ответов
    else:
        print(False)
        wrong += 1  # - счетчик неправильных ответов
    age = int(input("Год рождения Бритни Спирс? "))
    if age == 1981:
        print(True)
        right += 1  # - счетчик правильных ответов
    else:
        print(False)
        wrong += 1  # - счетчик неправильных ответов
    age = int(input("Год рождения Мерлина Менсона? "))
    if age == 1969:
        print(True)
        right += 1  # - счетчик правильных ответов
    else:
        print(False)
        wrong += 1  # - счетчик неправильных ответов
        print("Общее количество ответов: ", right + wrong)
        print("Из них правильных: ", right)
        print("Из них не правильных: ", wrong)
        print("Процентр правильный ответов: ", right * 100 / (right + wrong))
        print("Процент неправльных ответов: ", wrong * 100 / (right + wrong))
        answer = str(input("Хотите ли начать сначала? "))
        if answer == "нет":
            exit()

