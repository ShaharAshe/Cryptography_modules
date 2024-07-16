def decrypt(plaintext:str, a:int, b:int) -> str:
    de_txt:list = []
    a_1 = pow(a, -1, 26)
    print(f"[cipher] - e(x) = {a}x + {b}")
    print(f"[de-cipher] - d(x) = {a_1}(y - {b})")
    print("--------------")
    for c in plaintext:
        if c.isalpha():
            temp_c = (((ord(c.lower())-ord("a"))-b)*a_1)%26
            print(f'e({c}) = {c}*{a} + {b} = {temp_c} mod 26')
            temp_c = chr(temp_c+ord("a"))
            de_txt.append(temp_c)
    print("--------------")
    for c in de_txt:
        print(c, end=" ")
    print()

    return de_txt


if __name__ == "__main__":
    plaintext = "nexs mpmf wpbx nkpg xgdd vbfk"
    a = 11
    b = 5

    de_txt = decrypt(plaintext, a, b)
    # print(de_txt)