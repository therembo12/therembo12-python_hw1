try:
    revolutions = float(input("Enter Mars revolutions: "))
    earthRevolutions = round(686 * revolutions / 365, 1)
    if revolutions <= 0:
        raise ValueError
    print(f'This period corresponds to {earthRevolutions} Earth years')
except ValueError:
    print('\nERROR! Incorrect data. Only positive numbers can be entered.')