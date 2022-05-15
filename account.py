import yaml
import os
from pprint import pprint


def my_account():

    account = 0

    if os.path.exists('account.yaml'):
        with open('account.yaml', 'r') as f:
            account = int(yaml.safe_load(f))

    def acc_to_yaml():
        with open('account.yaml', 'w') as f:
            yaml.dump(account, f)

    purchase_history = []

    if os.path.exists('purchase_hist.yaml'):
        with open('purchase_hist.yaml', 'r') as f:
            purchase_history.append(yaml.full_load(f))

    def purchase_hist():
        with open('purchase_hist.yaml', 'w') as f:
            yaml.dump(purchase_history, f)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            print('Ваш депозит: ', account)
            deposit = int(input('Введите сумму пополнения: '))
            account += deposit
            acc_to_yaml()
            pass
        elif choice == '2':
            purchase_sum = int(input('Введите сумму покупки: '))
            if purchase_sum >= account:
                print('Суммы на вашем счете не достаточно!')
            else:
                purchase_name = input('Введите название покупки: ')
                account -= purchase_sum
                acc_to_yaml()
                purchase_h = (purchase_name, purchase_sum)
                purchase_history.append(purchase_h)
                purchase_hist()
            pass
        elif choice == '3':
            print(purchase_history)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

