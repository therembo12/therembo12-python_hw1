class NoMoney(Exception):
    pass


try:
    startMoney = int(input('Введіть суму в грн.'))
    while True:
        if startMoney <= 0:
            raise NoMoney()
        print(f'У вас {startMoney} грн на розваги')
        choset = int(input(
            '1.ГОРКИ СМОРКИ - 15 грн.\n 2.Toilet - 30grn \n 3.FearRoom - 55grn\n 4.Exit \n Choise your :'))

        if choset == 1:
            if startMoney >= 15:
                startMoney -= 15
        elif choset == 2:
            if startMoney >= 30:
                startMoney -= 30
        elif choset == 3:
            if startMoney >= 55:
                startMoney -= 55
        elif choset == 4:
            print(f'Exit у вас залишилось {startMoney} грн')
            break

except ValueError as e:
    print(e)
except NoMoney as e:
    print('No money no honey')
