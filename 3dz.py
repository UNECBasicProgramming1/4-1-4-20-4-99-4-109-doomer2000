## 4.1
#a = float(input())
#b = float(input())
#
#if a < b:
#    print(b, '>', a)
#elif a > b:
#    print(a, '>', b)
#else:
#    print('числа равны')
#
#
## 4.2
#from math import sin
#
#x = float(input())
#
#y = sin(x) ** 2 if x > 0 else 1 - 2 * sin(x ** 2)
#
#print(y)
#
## 4.3
#from math import sin
#
#x = float(input())
#
#y = sin(x ** 2) if x > 0 else 1 + 2 * (sin(x)) ** 2
#
#print(y)
#
#
## 4.4
#x = float(input())
#
#if x > 4:
#    print(2)
#else:
#    print(1)
#
#
## 4.5
#y = float(input())
#
#if y > 3:
#    print(1)
#else:
#    print(2)
#
#
## 4.6a
#x = float(input())
#
#if x <= 2:
#    y = x
#else:
#    y = 2
#
#print(y)
#
#
## 4.6b
#x = float(input())
#
#if x <= 3:
#    y = -x
#else:
#    y = -3
#
#print(y)
#
#
## 4.7
#from math import sin
#
#x = float(input())
#
#if sin(x) < 0:
#    k = x ** 2
#else:
#    k = abs(x)
#
#if k < x:
#    f = k * x
#else:
#    f = k + x
#
#print(f)
#
#
## 4.8
#from math import sin
#
#x = float(input())
#
#if sin(x) >= 0:
#    k = x ** 2
#else:
#    k = abs(x)
#
#if x < k:
#    f = abs(x)
#else:
#    f = k * x
#
#print(f)
#
#
## 4.9
#a = float(input())
#b = float(input())
#
#maximum = a
#minimum = b
#
#if a < b:
#    maximum = b
#    minimum = a
#
#print(f'maximum = {maximum}, minimum = {minimum}')
#
#
## 4.10
#a = float(input('в км: '))
#b = float(input('в футах: '))
#
#ma = a * 1000
#mb = b * 0.3048
#
#if ma > mb:
#    print(a)
#elif ma < mb:
#    print(b)
#else:
#    print('они равны')
#
#
## 4.11
#v1 = float(input())
#v2 = float(input())
#
#mv1 = v1 * 10 / 36
#
#if mv1 > v2:
#    print(v1)
#elif mv1 < v2:
#    print(v2)
#else:
#    print('они равны')
#
#
## 4.12
#from math import pi
#
#r = float(input('радиус круга: '))
#a = float(input('сторона квадрата: '))
#
#skr = pi * r ** 2
#skv = a ** 2
#
#if skr > skv:
#    print('площадь круга больше')
#elif skr < skv:
#    print('площадь квадрата больше')
#else:
#    print('они равны')
#
#
## 4.13
#v1 = float(input('объем первого: '))
#m1 = float(input('масса первого: '))
#v2 = float(input('объем второго: '))
#m2 = float(input('масса второго: '))
#
#p1 = m1 / v1
#p2 = m2 / v2
#
#if p1 > p2:
#    print('плотность первого больше')
#elif p1 < p2:
#    print('плотность второго больше')
#else:
#    print('они равны')
#
#
## 4.14
#r1 = float(input('сопротивление первого: '))
#u1 = float(input('напряжение первого: '))
#r2 = float(input('сопротивление второго: '))
#u2 = float(input('напряжение второго: '))
#
#i1 = u1 / r1
#i2 = u2 / r2
#
#if i1 > i2:
#    print('ток первого больше')
#elif i1 < i2:
#    print('ток второго больше')
#else:
#    print('они равны')
#
#
## 4.15
#a = float(input())
#b = float(input())
#c = float(input())
#
#d = b ** 2 - 4 * a * c
#
#if d >= 0:
#    print('корни есть')
#else:
#    print('корней нет')
#
#
## 4.16
#from math import sqrt
#
#a = float(input())
#b = float(input())
#c = float(input())
#
#d = b ** 2 - 4 * a * c
#
#if d >= 0:
#    x1 = (-b + sqrt(d)) / (2 * a)
#    x2 = (-b - sqrt(d)) / (2 * a)
#    print(x1, x2)
#else:
#    print('корней нет')
#
#
## 4.17
#year_birth = int(input())
#month_birth = int(input())
#year_now = int(input())
#month_now = int(input())
#
#age = year_now - year_birth
#
#if month_birth > month_now:
#    age -= 1
#
#print(age)
#
#
## 4.18a
#import math
#
#s_circle = float(input('площадь круга: '))
#s_square = float(input('площадь квадрата: '))
#
#r = math.sqrt(s_circle / math.pi)
#a = math.sqrt(s_square)
#
#if 2 * r <= a:
#    print('Круг уместится в квадрате.')
#else:
#    print('Круг не уместится в квадрате.')
#
#
## 4.18b
#import math
#
#s_circle = float(input('площадь круга: '))
#s_square = float(input('площадь квадрата: '))
#
#r = math.sqrt(s_circle / math.pi)
#a = math.sqrt(s_square)
#
#if a * math.sqrt(2) <= 2 * r:
#    print('Квадрат уместится в круге.')
#else:
#    print('Квадрат не уместится в круге.')
#
#
## 4.19
#import math
#
#s_circle = float(input('площадь круга: '))
#s_triangle = float(input('площадь равностороннего треугольника: '))
#
#r = math.sqrt(s_circle / math.pi)
#a = math.sqrt((4 * s_triangle) / math.sqrt(3))
#r_in = a * math.sqrt(3) / 6
#r_out = a * math.sqrt(3) / 3
#
#if r <= r_in:
#    print('а) Круг уместится в треугольнике.')
#else:
#    print('а) Круг не уместится в треугольнике.')
#
#if r_out <= r:
#    print('б) Треугольник уместится в круге.')
#else:
#    print('б) Треугольник не уместится в круге.')
#
#
## 4.20
#x1_1 = float(input('x левого нижнего угла первого прямоугольника: '))
#y1_1 = float(input('y левого нижнего угла первого прямоугольника: '))
#x2_1 = float(input('x правого верхнего угла первого прямоугольника: '))
#y2_1 = float(input('y правого верхнего угла первого прямоугольника: '))
#
#x1_2 = float(input('x левого нижнего угла второго прямоугольника: '))
#y1_2 = float(input('y левого нижнего угла второго прямоугольника: '))
#x2_2 = float(input('x правого верхнего угла второго прямоугольника: '))
#y2_2 = float(input('y правого верхнего угла второго прямоугольника: '))
#
#x_min = min(x1_1, x1_2)
#y_min = min(y1_1, y1_2)
#x_max = max(x2_1, x2_2)
#y_max = max(y2_1, y2_2)
#
#print('Координаты минимального прямоугольника, содержащего оба:')
#print(f'Левый нижний угол: ({x_min}, {y_min})')
#print(f'Правый верхний угол: ({x_max}, {y_max})')
#
#
## 4.99a
#a = float(input())
#b = float(input())
#
#if a > b:
#    print(a)
#if a < b:
#    print(b)
#
#
## 4.99b
#a = float(input())
#b = float(input())
#
#maximum = a
#if a < b:
#    maximum = b
#
#print(maximum)
#
#
## 4.100a
#a = float(input())
#b = float(input())
#
#if a > b:
#    print(f'Большее - {a}, меньшее - {b}')
#if a < b:
#    print(f'Большее - {b}, меньшее - {a}')
#
#
## 4.100b
#a = float(input())
#b = float(input())
#
#maximum = a
#minimum = b
#
#if a < b:
#    maximum = b
#    minimum = a
#
#print(f'Большее - {maximum}, меньшее - {minimum}')
#
#
## 4.101a
#a = float(input())
#b = float(input())
#c = float(input())
#
#print(max(a, b, c))
#
#
## 4.101b
#a = float(input())
#b = float(input())
#c = float(input())
#
#print(min(a, b, c))
#
#
## 4.102a
#a = float(input())
#b = float(input())
#c = float(input())
#d = float(input())
#
#print(max(a, b, c, d))
#
#
## 4.102b
#a = float(input())
#b = float(input())
#c = float(input())
#d = float(input())
#
#print(min(a, b, c, d))
#
#
## 4.103
#a = float(input())
#
#if a >= 0:
#    print(a)
#else:
#    print(-a)
#
#
## 4.104a
#a = float(input())
#b = float(input())
#
#if a < 0:
#    a = -a
#if b < 0:
#    b = -b
#
#p = (a + b) / 2
#print(p)
#
#
## 4.104b
#from math import sqrt
#
#a = float(input())
#b = float(input())
#
#if a < 0:
#    a = -a
#if b < 0:
#    b = -b
#
#p = sqrt(a * b)
#print(p)
#
#
## 4.105
#a = float(input())
#b = float(input())
#
#if a < 0:
#    a = -a
#if b < 0:
#    b = -b
#
#if a > b:
#    a /= 2
#
#print(a)
#
#
## 4.106
#from math import sqrt
#
#a = float(input())
#b = float(input())
#
#if sqrt(b) < a:
#    b *= 5
#
#print(b)
#
#
## 4.107
#a = int(input())
#b = int(input())
#c = int(input())
#
#if a % 2 == 0:
#    print(a)
#if b % 2 == 0:
#    print(b)
#if c % 2 == 0:
#    print(c)
#
#
## 4.108
#a = float(input())
#b = float(input())
#c = float(input())
#
#if a >= 0:
#    a **= 2
#if b >= 0:
#    b **= 2
#if c >= 0:
#    c **= 2
#
#print(a, b, c)
#
#
## 4.109
#a = float(input())
#b = float(input())
#c = float(input())
#
#if 1.6 <= a <= 3.8:
#    print(a)
#if 1.6 <= b <= 3.8:
#    print(b)
#if 1.6 <= c <= 3.8:
#    print(c)