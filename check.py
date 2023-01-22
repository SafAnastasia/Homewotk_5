total_amount = 0
histori = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет {total_amount}')

    choice = input('Выберите пункт меню')
    if choice == '1':
        sum_1 = int(input("Введите сумму: "))
        total_amount += sum_1
    elif choice == '2':
        sum_1 = int(input("Введите сумму покупки: "))
        if sum_1 > total_amount:
            print("Недостаточно средств")
        else:
            total_amount -= sum_1
            name = input ("Введите название покупки: ")
            histori.append((sum_1, name))
    elif choice == '3':
        print(histori)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')