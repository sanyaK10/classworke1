number1 = int(input("Введіть діаметр кола:"))
halva = input("Вам порахувати периметр чи площу?")
match halva :
    case 'площа':
        print(3.14 * number1 / 4)
    case 'периметр':
        print(3.14 * number1)
    
    
