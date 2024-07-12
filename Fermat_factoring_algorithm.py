import numpy as np
from math import ceil


def fermat(n:int) -> tuple[int, int]:
    x:int = ceil(np.sqrt(n))
    temp_table = []
    while np.sqrt((x**2)-n) != int(np.sqrt((x**2)-n)):
        temp_table.append([x, (x**2)-n, np.sqrt((x**2)-n)])
        x += 1
    temp_table.append([x, (x**2)-n, np.sqrt((x**2)-n)])
    y:int = np.sqrt((x**2)-n)
    header = ['x', f'x^2 - {n}', f'sqrt(x^2 - {n})']

    for t in temp_table:
        print("-----------------------------")
        for i in range(len(temp_table[0])):
            print(f'{header[i]} = ', end='')
            print(f'{t[i]}')
        print()
    print("-----------------------------")
    print("The factors are: x-y and x+y, where x and y are the values from the table above, and n is the number to be factored.\n")
    print(f'{x = }, {y = }, {n = }\n')
    print(f'{x-y} X {x+y} = ({x}-{y})({x}+{y}) = {x}^2 - {y}^2 = {n}')


if __name__ == "__main__":
    fermat(47197)