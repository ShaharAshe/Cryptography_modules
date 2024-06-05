def is_a_creator(n, a):
    res = [18]
    double = []
    print(f"To check if {a} is a creator of the group Z_{n} we will calculate the following:\n")

    print('=============================\n')
    for i in range(1, n):
        res.append((res[-1] * a)%n)
        if res[-1] in res[:-1]:
            double.append(res[-1])
        print(f'{i+1}. {res[-1]}^{i} = {res[-1] * a} mod {n} = {res[-1]}')
    print('\n=============================\n')

    print(f"The group is:\n{res}\n")
    print(f"The duplicates are: {double}\n")
    print(f"- The length of the group is: {len(res)}")
    print(f"- The length of the group without duplicates is: {len(res) - len(double)}")
    if len(res) == n:
        return True
    return False

if __name__ == "__main__":
    n = 349
    a = 18
    if is_a_creator(n, a):
        print("\n")
        print(f"YES {a} is a creator of the group Z_{n}")
    else:
        print("\n")
        print("NO")
