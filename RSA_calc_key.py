def calc(q, p, e_d):
    phi = (p-1) * (q-1)
    print(f'{phi = }')
    return pow(e_d, -1, phi)


if __name__ == "__main__":
    p = 149
    q = 109
    e_d = 17

    key = calc(q, p, e_d)
    print(f'{key = }')