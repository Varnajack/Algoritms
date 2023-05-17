def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

number=int(input("Число: "))
count = 0
for i in range(1, number+1):
    if is_prime(i):
        if (number%i==0):
            count += 1

print('Количество простых сомножителей: ', count)
