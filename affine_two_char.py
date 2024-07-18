def affine(origin_1, origin_2, cipher_1, cipher_2):
    a_co_1:int = (ord(origin_1.lower())-ord("a"))%26
    b_co_1:int = 1
    c_co_1:int = (ord(cipher_1.lower())-ord("a"))%26

    a_co_2:int = (ord(origin_2.lower())-ord("a"))%26
    b_co_2:int = 1
    c_co_2:int = (ord(cipher_2.lower())-ord("a"))%26
    
    print(f"We have:")
    print(f"e({origin_1}) = {cipher_1}")
    print(f"{origin_1} = {a_co_1} // {cipher_1} = {c_co_1}")
    print("AND:")
    print(f"e({origin_2}) = {cipher_2}")
    print(f"{origin_2} = {a_co_2} // {cipher_2} = {c_co_2}", end="\n\n")

    print("Now we gonna find the key for the affine cipher.")

    a_co_1:int = (ord(origin_1.lower())-ord("a"))%26
    b_co_1:int = 1
    c_co_1:int = (ord(cipher_1.lower())-ord("a"))%26

    a_co_2:int = (ord(origin_2.lower())-ord("a"))%26
    b_co_2:int = 1
    c_co_2:int = (ord(cipher_2.lower())-ord("a"))%26

    a_co:int = (a_co_2-a_co_1)%26
    b_co:int = (b_co_2-b_co_1)%26
    c_co:int = (c_co_2-c_co_1)%26

    a = -1
    b = -1
    if a_co_1 == 0:
        b = c_co_1
        a_co:int = a_co_2
        b_co:int = b_co_1
        c_co:int = c_co_2

        print(f"[1] - {c_co_1}=({a_co_1})a+({b_co_1})b mod 26")
        print(f"[2] - {c_co_2}=({a_co_2})a+({b_co_2})b mod 26")
        print(f"Then we have:")
        print(f"[3] - {c_co}=({a_co})a+({b_co})b = ({a_co})a+({b_co})({b}) mod 26")
    elif a_co_2 == 0:
        b = c_co_2
        a_co:int = a_co_1
        b_co:int = b_co_2
        c_co:int = c_co_1

        print(f"[1] - {c_co_1}=({a_co_1})a+({b_co_1})b mod 26")
        print(f"[2] - {c_co_2}=({a_co_2})a+({b_co_2})b mod 26")
        print(f"Then we have:")
        print(f"[3] - {c_co}=({a_co})a+({b_co})b = ({a_co})a+({b_co})({b}) mod 26")
    elif b_co_1 == 0:
        a = a_co_1
        a_co:int = a_co_2
        b_co:int = b_co_1
        c_co:int = c_co_2

        print(f"[1] - {c_co_1}=({a_co_1})a+({b_co_1})b mod 26")
        print(f"[2] - {c_co_2}=({a_co_2})a+({b_co_2})b mod 26")
        print(f"Then we have:")
        print(f"[3] - {c_co}=({a_co})a+({b_co})b = ({a_co})({a})+({b_co})b mod 26")
    elif b_co_2 == 0:
        a = a_co_2
        a_co:int = a_co_1
        b_co:int = b_co_2
        c_co:int = c_co_1

        print(f"[1] - {c_co_1}=({a_co_1})a+({b_co_1})b mod 26")
        print(f"[2] - {c_co_2}=({a_co_2})a+({b_co_2})b mod 26")
        print(f"Then we have:")
        print(f"[3] - {c_co}=({a_co})a+({b_co})b = ({a_co})({a})+({b_co})b mod 26")
    else:
        print(f"[1] - {c_co_1}=({a_co_1})a+({b_co_1})b mod 26")
        print(f"[2] - {c_co_2}=({a_co_2})a+({b_co_2})b mod 26")
        print(f"Then we have:")
        print(f"[3] - {c_co}=({a_co})a+({b_co})b mod 26")


if __name__ == "__main__":
    origin_1 = "d"
    cipher_1 = "p"

    origin_2 = "r"
    cipher_2 = "x"

    affine(origin_1, origin_2, cipher_1, cipher_2)
