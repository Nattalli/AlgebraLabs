from itertools import zip_longest
import copy as cp
import itertools
import functools


a = input('Number 1:')
b = input('Number 2:')


def LongNumber(number):
    long_number = []
    if number[0] == '-':
        number = number[1:]
        long_number.append('-')
    for x in number:
        long_number.append(int(x))
    return long_number


a = LongNumber(a)
b = LongNumber(b)


def AddNumbers(number_1, number_2):
    if (number_1[0] == '-') & (number_2[0] != '-'):
        return longSub(number_1[1:], number_2)
    elif (number_1[0] != '-') & (number_2[0] == '-'):
        return longSub(number_1, number_2[1:])
    elif (number_1[0] == '-') & (number_2[0] == '-'):
        return longAdd(number_1[1:], number_2[1:])
    else:
        return longAdd(number_1, number_2)


def longAdd(number_1, number_2):
    p = 0
    len_1 = len(number_1)
    len_2 = len(number_2)
    i1 = len_1 - 1
    i2 = len_2 - 1
    res = ""
    while True:
        if (i1 < 0) & (i2 < 0):
            break
        if i1 < 0:
            a2 = int(number_2[i2]) + p
            p = a2 // 10
            a2 = a2 % 10
            res = str(a2) + res
            i2 -= 1
            if i2 < 0:
                break
        if i2 < 0:
            a1 = int(number_1[i1]) + p
            p = a1 // 10
            a1 = a1 % 10
            res = str(a1) + res
            i1 -= 1
            if i1 < 0:
                break
        a1 = int(number_1[i1])
        a2 = int(number_2[i2])
        r = a1 + a2 + p
        p = r // 10
        r = r % 10
        res = str(r) + res
        i1 -= 1
        i2 -= 1
    if p > 0:
        res = str(p) + res
    return res


def longSub(number_1, number_2):
    p = 0
    len_1 = len(number_1)
    len_2 = len(number_2)
    i1 = len_1 - 1
    i2 = len_2 - 1
    res = ""
    while True:
        if (i1 < 0) & (i2 < 0):
            break
        if i1 < 0:
            a2 = int(number_2[i2]) + p
            p = a2 // 10
            a2 = a2 % 10
            res = str(a2) + res
            i2 -= 1
            if i2 < 0:
                break
        if i2 < 0:
            a1 = int(number_1[i1]) + p
            p = a1 // 10
            a1 = a1 % 10
            res = str(a1) + res
            i1 -= 1
            if i1 < 0:
                break
        a1 = int(number_1[i1])
        a2 = int(number_2[i2])
        r = a1 - a2 + p
        p = r // 10
        r = r % 10
        res = str(r) + res
        i1 -= 1
        i2 -= 1
    if p > 0:
        res = str(p) + res
    return res


print("Adding: a + b = ")
print(AddNumbers(a, b))


def longSubtract(a, b):
    d = []
    if b[0] == '-':
        return AddNumbers(a, b[1:])
    else:
        d.append('-')
        d.append(*b)
        return AddNumbers(a, d)


print("Subtract: a - b = ")
print(longSubtract(a, b))


def Greater(number_1, number_2):
    if (number_1[0] == '-') & (number_2[0] != '-'):
        return number_2
    elif (number_1[0] != '-') & (number_2[0] == '-'):
        return number_1
    elif (number_1[0] == '-') & (number_2[0] == '-'):
        return longLess(number_1[1:], number_2[1:])
    else:
        return longGreater(number_1, number_2)


def Less(number_1, number_2):
    if (number_1[0] == '-') & (number_2[0] != '-'):
        return number_1
    elif (number_1[0] != '-') & (number_2[0] == '-'):
        return number_2
    elif (number_1[0] == '-') & (number_2[0] == '-'):
        return longGreater(number_1[1:], number_2[1:])
    else:
        return longLess(number_1, number_2)


def longGreater(number_1, number_2):
    global a, b
    if len(number_1) != len(number_2):
        max_len = max(len(number_2), len(number_1))
        if len(number_1) == max_len:
            return number_1
        else:
            return number_2
    else:
        for x in range(len(number_1)):
            a = int(number_1[x])
            b = int(number_2[x])
            if a > b:
                return number_1
            if a < b:
                return number_2
        return number_2


def longLess(number_1, number_2):
    global a, b

    if number_1 != ['0']:
        while number_1[0] == '0':
            number_1 = number_1[1:]

    if number_2 != ['0']:
        while number_2[0] == '0':
            number_2 = number_2[1:]

    if len(number_1) != len(number_2):
        max_len = max(len(number_2), len(number_1))
        if len(number_1) == max_len:
            return number_2
        else:
            return number_1
    else:
        for x in range(len(number_1)):
            a = int(number_1[x])
            b = int(number_2[x])
            if a > b:
                return number_2
            if a < b:
                return number_1
        return number_1


def longEqual(number_1, number_2):
    equal = False
    for x in range(len(number_1)):
        if number_2[x] != number_1[x]:
            equal = False
            break
        else:
            equal = True
    return equal


print("Greater number: ")
print(*Greater(a, b))

print("Less number: ")
print(*Less(a, b))

print("Equal: ")
print(longEqual(a, b))


def longMultiply(number_1, number_2):
    res = LongNumber('0')
    while not longEqual(number_2, ['0']):
        res = AddNumbers(res, number_1)
        number_2 = longSub(number_2, ['1'])
    return res


print("Multiplying: a * b = ")
print(longMultiply(a, b))


def longDivide(number_1, number_2):
    a = number_2
    b = LongNumber('0')
    if number_1 == number_2:
        return ['1']
    while Less(number_1, a) == a:
        number_1 = longSubtract(number_1, number_2)
        b = longAdd(b, ['1'])
        if Less(number_1, a) == number_1:
            break
    if number_1 == number_2:
        b = longAdd(b, ['1'])
        number_1 = ['0']
    return b, number_1


print("Dividing: a / b = ")
print(longDivide(a, b))


def Pow(number_1, number_2):
    a = LongNumber('1')
    while Less(number_2, ['0']) == ['0']:
        a = longMultiply(a, number_1)
        number_2 = longSubtract(number_2, ['1'])
        if longEqual(number_2, ['0']) or longEqual(number_2, ['0', '0']):
            break
    return a


print('Input new a and b for pow:')
a = input()
b = input()

print("Pow: a ^ b = ")
print(Pow(a, b))


def Abs(number):
    if number[0] == '-':
        return number[1:]
    else:
        return number


print("For abs:")

a = Abs(LongNumber(input('Input first number:')))
b = Abs(LongNumber(input('Input second number:')))

print("Adding: a + b = ")
print(AddNumbers(a, b))

print("Subtract: a - b = ")
print(longSubtract(a, b))

print("Multiplying: a * b = ")
print(longMultiply(a, b))

print("Dividing: a / b = ")
print(longDivide(a, b))


print('Input new a and b for pow:')
a = LongNumber(input())
b = LongNumber(input())
a = Abs(a)
b = Abs(b)

print("Pow: a ^ b = ")
print(Pow(a, b))


def longSqrt(number):
    if number == ['0']:
        return number
    else:
        x = number
        a = False
        while not a:
            num = number
            c = longDivide(x, number)
            number_1 = AddNumbers(number, c)
            number = longDivide(number_1, ['2'])
            number = number[0]
            for x in number:
                if number[0] == ['0']:
                    number = number[1:]
            k = longSubtract(num, number)
            if Less(k, ['1']) == k:
                a = True
        return number


a = LongNumber(input('Enter new number for finding [sqrt(a)]'))
print(longSqrt(a))


def GCD(a, b):
    while min(a, b) > 0:
        if a >= b:
            a %= b
            continue
        if b > a:
            b %= a
            continue
    return max(a, b)


def firstStep(a, b, c):
    while a > c:
        a = a - c
    d = GCD(a, c)
    if b % d != 0:
        print("Here is no solutions")
        return 0
    else:
        a = a//d
        b = b//d
        c = c//d

        solutions = []
        solutions.append(0)
        solutions.append(1)
        count = 0
        while c > 1:
            q = c // a
            solutions.append(q*solutions[-1] + solutions[-2])
            count += 1
            c %= a
            a, c = c, a

        return (-1**count*solutions[count]*b)%c, c


print("input a, b, c:")
a = int(input())
b = int(input())
c = int(input())

print("Solution for the one equation:")
print(firstStep(a, b, c))

print("Let`s try to find a solution for two equations")
print("input a, b, c:")
a = int(input())
b = int(input())
c = int(input())


print("input a1, b1, c1:")
a1 = int(input())
b1 = int(input())
c1 = int(input())


def secondStep(a, b, c, a1, b1, c1):
    gcd = GCD(c, c1)
    if gcd == "1":
        return
    else:
        if b % gcd == b1 % gcd:
            new = firstStep(1, b % gcd, gcd)
            c //= gcd
            c1 //= gcd
            b %= c
            b1 %= c1
            return new
        else:
            print("This system have no solutions!")


print("Solution for system:")
print(secondStep(a, b, c, a1, b1, c1))
