number1 = int(input("Введіть суму в доларах:"))
value = input("Оберіть валюту, у яку хочете перевести цю суму: євро (EUR), фунти (GBP) або гривні (UAH)")
course = float(input("Введіть курс валюти до долара:"))
all = number1 * course

match value :
    case 'євро':
        print(f'курс євро до долара = {all}')
    case 'фунт':
        print(f'курс фунта до долара = {all}')
    case 'гривня':
        print(f'курс гривні до долара = {all}')