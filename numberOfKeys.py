def is_prime(n):
    if n <= 1:
        return n
    for i in range(2, n+1):
        if n % i == 0:
            return i


def n_factor(n):
    divs = {}
    temp_n = n
    p = is_prime(temp_n)
    while temp_n != 1:
        while temp_n % p == 0:
            if p in divs:
                divs[p] += 1
            else:
                divs[p] = 1
            temp_n = temp_n//p
        p = is_prime(temp_n)
    return divs


if __name__ == '__main__':
    try:
        while True:
            num = input("Enter a number to find its prime factors (or type 'exit' to quit): ")
            if num == 'exit':
                raise SystemExit("bye")
            while not num.isdigit():
                num = input("Please enter a valid number (or type 'exit' to quit): ")
                if num == 'exit':
                    raise SystemExit("bye")
            print("=====================================")
            all_primes = n_factor(int(num))
            if not all_primes and int(num) > 1:
                print(f"{num} is a prime number")
            elif int(num) <= 1:
                print(f"{num} is not a prime number")
            else:
                print(f"Prime factors of {num} are:")
                for key, value in all_primes.items():
                    print(f"- {key}^{value}")
            print("-------------------------------------")
            num_keys = int(num)
            for key, value in all_primes.items():
                num_keys *= ((key**value)-(key**(value-1)))
                print(f"({key**value} - {key**(value-1)})", end='')
            num_keys -= 1
            print(f'{num} - 1 = {num_keys}')
            print("-------------------------------------")
            print(f"Number of keys for {num} are: {num_keys}")
            print("=====================================", end='\n\n')
    except SystemExit as e:
        print(e)
