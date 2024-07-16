def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def find_equetion(a:int, num_of_solutions:int):
    i = num_of_solutions+1 if num_of_solutions > a else a+1

    while gcd(a, i) != num_of_solutions:
        i += 1

    print(f"gcd({a}, {i}) = {num_of_solutions}, and {num_of_solutions}|{num_of_solutions}")
    print(f"---------------------------------")
    print(f"The equation {a}x = {num_of_solutions} mod {i}")
    print(f"has {num_of_solutions} solutions")
    print(f"---------------------------------")


if __name__ == '__main__':
    a = 45
    num_of_solutions = 15
    find_equetion(a, num_of_solutions)
