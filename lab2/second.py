import random as rand


def GCD(a, b):
    while min(a, b) > 0:
        if a >= b:
            a %= b
            continue
        if b > a:
            b %= a
            continue
    return max(a, b)


def custom_func(number, number_2):
    return (number * number + 1) % number_2


def factorization(number):
    a, b = 2, 2
    t = 0
    while t <= 1:
        a = custom_func(a, number)
        b = custom_func(custom_func(b, number), number)
        t = GCD(abs(b - a), number)
    return t


# stage 1 - factorization with pollard po-alg
print('factorization with pollard po-alg')
print(factorization(8051))


def euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = euclid(b, a % b)
        x = yy
        y = xx - (a / b) * yy
        return d, x, y


def xab(x, a, b, G, H, P, Q):
    sub = x % 3
    if sub == 0:
        x = x * G % P
        a = (a + 1) % Q
    elif sub == 1:
        x = x * H % P
        b = (b + 1) % Q
    else:
        x = x * x % P
        a = a * 2 % Q
        b = b * 2 % Q
    return x, a, b


def logarithm(G, H, P):
    Q = (P - 1) / 2
    x = G * H
    a, b = 1, 1
    X = x
    A = a
    B = b
    for i in range(1, P):
        x, a, b = xab(x, a, b, G, H, P, Q)
        X, A, B = xab(X, A, B, G, H, P, Q)
        X, A, B = xab(X, A, B, G, H, P, Q)
        if x == X:
            break
    nom = a - A
    denom = B - b
    res = (euclid(denom, Q)[1] * nom) % Q
    return res + Q


# stage 2 - logarithm with pollard po-alg
print('logarithm with pollard po-alg')
print(logarithm(2, 11, 59))


def euler(n):
    result = n
    i = 2
    while i ** 2 < n:
        while n % i == 0:
            n /= i
            result -= result / i
        i += 1
    if n > 1:
        result -= result / n
    return result


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n + 1):
        if i * i <= n and n % i == 0:
            return False
    return True


def mobius(N):
    if N == 1:
        return 1
    p = 0
    for i in range(1, N + 1):
        if N % i == 0 and isPrime(i):
            if N % (i * i) == 0:
                return 0
            else:
                p = p + 1
    if p % 2 != 0:
        return -1
    else:
        return 1


# step 3 - euler and mobius
print('euler and mobius')
print(euler(30))
print(mobius(10))


def residue(a, p):
    for x in range(p):
        if (x * x) % p == a:
            return True
    return False


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    elif p == 3:
        if a == 0:
            return 0
        elif a == 1:
            return 1
        else:
            return -1
    else:
        if residue(a, p):
            return 1
        else:
            return -1


def jacobi(a, n):
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -1 * t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -1 * t
        a %= n
    if n == 1:
        return t
    else:
        return 0


# Stage 4 - legendre
print('legendre and jacobi')
print(legendre(37, 17))
print(jacobi(7, 15))


def cipolla(a, p):

    if legendre(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


# Stage 5 - cipolla
print('cipolla')
print(cipolla(223, 17))


def miller_rabin(n, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = rand.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# stage 6 - miller_rabin algorithm
print('miller-rabin algorithm')
print(miller_rabin(13, 2))
