def calculation(first_number, second_number, operations):
    try:
        if operations == "+":
            return first_number + second_number
        elif operations == "-":
            return first_number - second_number
        elif operations == "*":
            return first_number * second_number
        elif operations == "/":
            if second_number == "0":
                return("Деление на ноль невозможно") 
            return first_number / second_number
        else:
            return("Неверная операция")
    except Exception as e:
        return(f"Произошла ошибка {e}")

try:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    operations = (input("Введите операцию: +, -, *, / "))
    result = calculation(first_number, second_number, operations)
    print(f"Результат равен: {result}")
except ValueError:
    print("Ошибка, введите корректное число.")
except KeyboardInterrupt:
    print("Ошибка, программа прервана пользователем.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
