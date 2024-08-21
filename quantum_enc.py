def quantum(up, down):
    for u,d in zip(up, down):
        if u ==  "-" or u == "|" or u == "+":
            if d == "+":
                print(u, end=" ")
            else:
                print("/", end=" ") if u!="+" else print("x", end=" ")
        else:
            if d == "x" or d == "X":
                print(u, end=" ")
            else:
                print("|", end=" ") if u!="x" or u!="X" else print("+", end=" ")
    print()
    

if __name__ == "__main__":
    # if you want to use \ use \\
    up = "-\\/|-\\|/"
    down = "+x++x++x"
    quantum(up, down)