a = list(map(int, input('Введите x1, y1, r1 (через пробел): ').split()))
b = list(map(int, input('Введите x2, y2, r2 (через пробел): ').split()))

distance = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if distance == 0:
    print("a > b" if a[2] > b[2] else "b > a")
elif distance < (a[2] + b[2]) ** 2:
    print("a^b")
else:
    print("a|b")