def inverse(num:int, mod:int) -> int:
    return pow(num, -1, mod)


if __name__ == "__main__":
    num = 3
    mod = 11
    
    inv = inverse(num=num, mod=mod)

    print(f"The inverse of {num} mod {mod} is {inv}")