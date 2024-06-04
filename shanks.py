from math import ceil, sqrt


def shanks(p, a, base):
    print("We are solving the discrete log problem with shanks algorithm.\n")
    m = ceil(sqrt(p - 1))
    print(f"The order of the group is {p - 1} and m = ceil(sqrt({p-1})) = {m}\n")
    print(f"Now we are looking for 0<=i,j<={m} such that:")
    print(f"{base}^(i+{m}*j) {a} mod {p} <=> {base}^i = {a}X({base}^((-{m})^j) mod {p}\n")

    print(f"Let's calculate the values of {base}^i mod {p} for 0<=i<={m}:")
    i = [(base**index)%p for index in range(m)]
    for index, value in enumerate(i):
        print(f"i = {index}: {base}^{index} mod {p} = {value}")

    print(f"\nNow let's calculate the values of {base}^((-{m})^j) mod {p} for 0<=j<={m} antil we find a match in the i values:")
    j = 0
    m_1 = (p-1)-m
    while j <= m:
        print('-------------------')
        print(f'{j = }: ')
        value = (a * (base**m_1)**j) % p
        print(f"{a} X {base}^((-{m})^{j}) mod {p} = {value}")
        if value in i:
            print('\n===================')
            print(f"We found a match in the i values: {value} = {base}^{i.index(value)} mod {p}")
            i_index = i.index(value)
            res = i_index + m*j
            print(f"{a}X({base}^((-{m})^{j}) = {base}^{i_index} mod {p}")
            print(f"<=> {a} = {base}^{i_index}+{m}*{j} = {base}^{res} mod {p}")
            print(f"\n- Therefore the discrete log of {a} in base {base} mod {p} is {res}")
            print('===================')
            return res
        else:
            print(f"{value} is not in the i values")
        j += 1


if __name__ == '__main__':
    p = 349
    a = 202
    base = 18
    discrete_log = shanks(p, a, base)
