"""
Калькулятор

"""
try:
   print("-"*50, "\n", "Результат: ", eval(input("Введите математическое выражение (напр. 2+2*5):\n")))
except ValueError:
    print("Необходимо вводить числовые значения")
except ZeroDivisionError:
    print("На ноль делить нельзя")
except Exception:
    print("Ошибка")