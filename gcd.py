def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


if __name__ == "__main__":
    while True:
        try:
            num_1 = input("Enter the first number (or exit): ")
            if num_1 == "exit":
                break
            num_2 = input("Enter the second number (or exit): ")
            if num_2 == "exit":
                break
            if not num_1.isdigit() or not num_2.isdigit():
                raise ValueError("Please enter a valid number")
            print(f"---------------------------------\nGCD({num_1}, {num_2}) = {gcd(int(num_1), int(num_2))}\n---------------------------------")
        except ValueError as e:
            print(f"---------------------------------\n*** {e} ***\n---------------------------------")
