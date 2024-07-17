def euclidean_algorithm(e_a, e_b):
    r = [e_b, e_a]
    q = []

    while r[-1] != 0:
        q.append(r[-2] // r[-1])
        r.append(r[-2] % r[-1])
    r = r[:-1]
    
    s = [0, 1]
    t = [1, 0]
    c = -1
    for i in range(2, len(q)+1):
        s.append(c*((abs(s[i - 1])*q[i - 2])+abs(s[i - 2])))
        c *= -1
        t.append(c*((abs(t[i - 1])*q[i - 2])+abs(t[i - 2])))

    for i in range(len(r)):
        if not i:
            print(f'{i = :<10} r = {r[i]:<10}{"":16}s = {s[i]:<10} t = {t[i]}')
        else:
            print(f'{i = :<10} r = {r[i]:<10} q = {q[i-1]:<10} s = {s[i]:<10} t = {t[i]}')
    print("-----------------")
    print(f'we got that {r[-1]} = {e_a}*({s[-1]}) + {e_b}*({t[-1]})')
    print("-----------------")
    print("So:")
    print(f"The value of s is {s[-1]}")
    print(f"The value of t is {t[-1]}")
    print("-----------------")
    return (s[-1], t[-1])

if __name__ == "__main__":
    e_a = 17
    e_b = 71
    
    euclidean_res = euclidean_algorithm(e_a, e_b)
    # print(euclidean_res)
