def most_common(i: int, strI: str):
    str_list = [s for s in strI if s != ' ']
    return (str_list, max(str_list, key=str_list.count))


def cipher(i: int, strI: str):
    str_list, mC = most_common(i, strI)
    print(f"The most common letter in the M{i + 1} cipher is: {mC}", end="\n\n")
    re_list = []
    letter_frequency = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]

    for aBi in range(len(letter_frequency)):
        distunce = ((ord(mC.lower()) - ord(letter_frequency[aBi])) % 26)
        if distunce >= 0:
            re_list = " ".join([str(chr(((ord(s) - ord("a") - distunce) % 26) + ord('a'))) for s in str_list])
            print(f"Possible messages for {letter_frequency[aBi]}:\n {re_list}\n")
            ans = input("Is this the correct message? (y/n): ")
            while ans not in ['y', 'n']:
                print(
                    "---------------------------------\n*** Invalid answer, please try again ***\n---------------------------------")
                ans = input("Please enter a valid answer (y/n): ")
            if ans == 'n':
                continue
            else:
                print(f"The most common letter in the M{i + 1} cipher is: {mC}", end="\n\n")
                print("=================================")
                print(f"The message M{i + 1} is encripted with the Shift code:")
                print(f"e(x) = x+{distunce} mod26")
                print("---------------------------------")
                print(f"And copying the decoding is:")
                print(f"d(y) = d-{distunce} = d+{26 - distunce} mod26")
                print("=================================", end="\n\n")
                ans = input("Do you want to continue with the other message? (y/n): ")
                while ans not in ['y', 'n']:
                    print(
                        "---------------------------------\n*** Invalid answer, please try again ***\n---------------------------------")
                    ans = input("Please enter a valid answer (y/n): ")
                if ans == 'n':
                    return True
                else:
                    continue
    return False


if __name__ == "__main__":
    M1 = "xkxo qdtm tkmu dgqb kcza pmkd gtkq pues"
    M2 = "nani mzfe faeu zsmv akrg xeaz sfam xuoq"

    text_encripted = [M1, M2]

    for i in range(len(text_encripted)):
        if cipher(i, text_encripted[i]):
            break

    print("\n=================================")
    print("           Goodbye!")
    print("=================================")
