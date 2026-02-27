__author__ = "Высоцкая И.Д."
"""Даны действительные числа a, b, c. Удвоить эти числа, если a ≥ b ≥ c, и заменить их абсолютными значениями, если это не так."""
'Главный модуль'

from module_ex37 import * # подключаем модуль с функциями
from tests_ex37 import * # подключаем модуль с тестами

test() # функция с тестами

print("a = ", end="") # вывод на консоль
a = float(input()) # ввод в консоль
print("b = ", end="")
b = float(input())
print("c = ", end="")
c = float(input())
ans = conc_ch(a, b, c)
print("Результат:")
print ("a = ", f"{ans[0]:.2f}") # вывод результата
print ("b = ", f"{ans[1]:.2f}")
print ("c = ", f"{ans[2]:.2f}")