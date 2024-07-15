import random 


def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def shaum(n:int, e:int, d:int, m:int):
    k = random.randint(1, n)
    while gcd(k, n) != 1:
        k = random.randint(2, n-1)
    print(f'{k = :<5} {e = :<5} {d = :<5} {m = :<5} {n = :<5}')

    print('=======================')
    t = (m*(k**e)) % n
    print(f't = m*(k^e) = {m}*({k}^{e}) = {t} mod {n}')

    t_d = pow(t, d, n)
    print(f't^d = (m*(k^e))^d = {t}^{d} = {t_d} mod {n}')

    s = (t_d * pow(k, -1, n)) % n
    print(f's = (t^d)/k = m^d = {t_d}/{k} = {s} mod {n}')
    print(f'm^d = {m}^{d} = {pow(m, d, n)} mod {n}')
    print('=======================')

    print('_______________________')
    print(f'{s = }')
    print(f'm^d = {pow(m, d, n)}', end="\n\n")
    print("Check if the signature is valid (s == m^d)")
    print('_______________________')


if __name__ == "__main__":
    n = 16241
    e = 17
    d = 3761

    m = 2093
    
    shaum(n, e, d, m)
