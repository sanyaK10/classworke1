number1 = int(input("Введіть час ,що минув з почтаку дня у секундах:"))
hefu = input("Вам порахувати час ,що залишився у секундах,хвилинах,або годинах?")
in_seconds = 86400 - number1
match hefu:
    case 'секундах':
        print(in_seconds)
    case 'хвилинах':
        print(60 / in_seconds)
    case 'годинах':
        print(360/ in_seconds)