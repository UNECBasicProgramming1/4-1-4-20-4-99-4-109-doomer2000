## 4.1
#a = float(input())
#b = float(input())
#print(f"{a} больше, {b} меньше" if a > b else f"{b} больше, {a} меньше")
#
## 4.2
#import math
#
#x = float(input())
#y = math.sin(x) ** 2 if x > 0 else 1 - 2 * math.sin(x ** 2)
#print(f"y = {y}")
#
## 4.3
#import math
#
#x = float(input())
#y = math.sin(x ** 2) if x > 0 else 1 + 2 * math.sin(x) ** 2
#print(f"y = {y}")
#
## 4.4
#x = float(input())
#y = float(input())
#print(
#    "во вторую" if x > 4 and y > 0
#    else "в первую" if x < 4 and y > 0
#    else "ни в одну из них"
#)
#
## 4.5
#x = float(input())
#y = float(input())
#print(
#    "в первую" if x > 0 and y > 3
#    else "во вторую" if x > 0 and y < 3
#    else "ни в одну из них"
#)
#
## 4.7
#import math
#
#x = float(input())
#a = math.sin(x)
#k = x ** 2 if a > 0 else abs(x)
#f = k * x if k < x else k + x
#print(f"f = {f}")
#
## 4.8
#import math
#
#x = float(input())
#a = math.sin(x)
#k = abs(x) if a < 0 else x ** 2
#f = abs(x) if x < k else k * x
#print(f"f = {f}")
#
## 4.9
#a, b = map(float, input().split())
#print(
#    f"{a} — максимум, {b} — минимум" if a > b
#    else f"{b} — максимум, {a} — минимум"
#)
#
## 4.10
#km = float(input("Введите километры: "))
#funt = float(input("Введите футы: "))
#funt_m = funt * 0.3048
#
#print(
#    "в километрах меньше" if km > funt_m
#    else "в футах меньше" if funt_m > km
#    else "они равны"
#)
#
## 4.11
#v1 = float(input("Введите скорость в км/ч: "))
#v2 = float(input("Введите скорость в м/с: "))
#
#v1_ms = v1 * (5 / 18)
#print(
#    "в км/ч больше" if v1_ms > v2
#    else "в м/с больше" if v2 > v1_ms
#    else "они равны"
#)
#
## 4.12
#import math
#
#r = float(input("Введите радиус круга: "))
#a = float(input("Введите сторону квадрата: "))
#
#s_kv = a ** 2
#s_kr = math.pi * r ** 2
#
#print("площадь квадрата больше" if s_kv > s_kr else "площадь круга больше")
#
## 4.13
#m1 = float(input("Введите массу 1: "))
#m2 = float(input("Введите массу 2: "))
#v1 = float(input("Введите объём 1: "))
#v2 = float(input("Введите объём 2: "))
#
#p1 = m1 / v1
#p2 = m2 / v2
#print("плотность 1 больше" if p1 > p2 else "плотность 2 больше")
#
## 4.15–4.16
#a, b, c = map(float, input("Введите a, b, c: ").split())
#d = b ** 2 - 4 * a * c
#
#if d > 0:
#    x1 = (-b + d ** 0.5) / (2 * a)
#    x2 = (-b - d ** 0.5) / (2 * a)
#    print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")
#elif d == 0:
#    x = -b / (2 * a)
#    print(f"Уравнение имеет один корень: x = {x}")
#else:
#    print("Корней нет")
#
## 4.17
#god_roj = int(input("Год рождения: "))
#mes_roj = int(input("Месяц рождения: "))
#god = int(input("Текущий год: "))
#mes = int(input("Текущий месяц: "))
#
#age = god - god_roj if mes_roj <= mes else god - god_roj - 1
#print(f"Возраст: {age}")
#
## 4.18
#import math
#
#s_kv = float(input("Введите площадь квадрата: "))
#s_kr = float(input("Введите площадь круга: "))
#
#a = s_kv ** 0.5
#r = (s_kr / math.pi) ** 0.5
#
#if r < a / 2:
#    print("Круг уместится внутри квадрата, квадрат в круге — нет")
#else:
#    print("Круг не уместится внутри квадрата, квадрат уместится в круге")
#
## 4.19
#import math
#
#s_tr = float(input("Введите площадь треугольника: "))
#s_kr = float(input("Введите площадь круга: "))
#
#r = (s_kr / math.pi) ** 0.5
#a = ((4 * s_tr) / math.sqrt(3)) ** 0.5
#r_vpis = a * (3 ** 0.5) / 6
#r_opis = a * (3 ** 0.5) / 3
#
#if r <= r_vpis:
#    print("Круг уместится в треугольнике")
#else:
#    print("Круг не уместится в треугольнике")
#
#if r_opis <= r:
#    print("Треугольник уместится в круге")
#else:
#    print("Треугольник не уместится в круге")
#
## 4.20 
#
#
## 4.99(a)
#a, b = map(float, input("Введите a и b: ").split())
#print("a больше b" if a > b else "b больше a" if b > a else "равны")
#
## 4.100
#a, b = map(float, input("Введите a и b: ").split())
#print(f"a наибольшее, b наименьшее" if a > b else f"b наибольшее, a наименьшее")
#
## 4.101(a)
#a, b, c = map(float, input("Введите a, b, c: ").split())
#if a > b and a > c:
#    print("a наибольшее")
#elif b > a and b > c:
#    print("b наибольшее")
#else:
#    print("c наибольшее")
#
## 4.101(b)
#a, b, c = map(float, input("Введите a, b, c: ").split())
#if a < b and a < c:
#    print("a наименьшее")
#elif b < a and b < c:
#    print("b наименьшее")
#else:
#    print("c наименьшее")
#
## 4.102(a)
#a, b, c, d = map(float, input("Введите a, b, c, d: ").split())
#max_val = max(a, b, c, d)
#print(f"Наибольшее число: {max_val}")
#
## 4.102(b)
#a, b, c, d = map(float, input("Введите a, b, c, d: ").split())
#min_val = min(a, b, c, d)
#print(f"Наименьшее число: {min_val}")
#
## 4.103
#x = float(input("Введите x: "))
#print(f"Результат: {(x * 2) * 0.5}")
#
## 4.104
#import math
#
#a, b = map(float, input("Введите a и b: ").split())
#a = (a * 2) * 0.5
#b = (b * 2) * 0.5
#print(f"Среднее арифметическое: {(a + b) / 2}")
#print(f"Среднее геометрическое: {math.sqrt(a * b)}")
#
## 4.105
#a, b = map(int, input("Введите a и b: ").split())
#a = a / 2 if abs(a) > abs(b) else a
#print(f"Результат: {a}")
#
## 4.106
#a, b = map(int, input("Введите a и b: ").split())
#b = b * 5 if math.sqrt(b) < a else b
#print(f"Результат: {b}")
#
## 4.107
#a, b, c = map(int, input("Введите a, b, c: ").split())
#for val in (a, b, c):
#    if val % 2 == 0:
#        print(f"Чётное: {val}")
#
## 4.108
#a, b, c = map(float, input("Введите a, b, c: ").split())
#for val in (a, b, c):
#    if val > 0:
#        print(f"Квадрат положительного числа {val}: {val ** 2}")
#
## 4.109
#a, b, c = map(float, input("Введите a, b, c: ").split())
#for val in (a, b, c):
#    if 1.6 < val < 3.8:
#        print(f"Число в диапазоне (1.6, 3.8): {val}")
#
## 4.110
#a, b, c = map(float, input("Введите a, b, c: ").split())
#k = sum(1 for x in (a, b, c) if x < 0)
#print(f"Количество отрицательных чисел: {k}")
