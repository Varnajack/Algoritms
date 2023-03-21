import math

x1 = int(input("Введите x первой вершины: "))
y1 = int(input("Введите y первой вершины: "))
x2 = int(input("Введите x второй вершины: "))
y2 = int(input("Введите y второй вершины: "))
x3 = int(input("Введите x третьей вершины: "))
y3 = int(input("Введите y третьей вершины: "))

A = math.sqrt( pow((x2 - x1),2) + pow((y2 - y1),2) )
B = math.sqrt( pow((x3 - x2),2) + pow((y2 - y1),2) )
C = math.sqrt( pow((x1 - x3),2) + pow((y1 - y3),2) )

p = ( A + B + C)/2
S = math.sqrt( p*(p - A )*(p - B)*(p - C) )
print("Площадь треугольника равна:", round(S,2), '\t', "Периметр треугольника равен:" ,round((A+B+C),2))