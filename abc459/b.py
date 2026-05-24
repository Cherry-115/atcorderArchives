N = int(input())
S = map(str, input().split())

ans = ""
for i in S:
    j = "".join(list(i.lower())[0])

    if j == "a" or j == "b" or j == "c":
        ans += "2"
    elif j == "d" or j == "e" or j == "f":
        ans += "3"
    elif j == "g" or j == "h" or j == "i":
        ans += "4"
    elif j == "j" or j == "k" or j == "l":
        ans += "5"
    elif j == "m" or j == "n" or j == "o":
        ans += "6"
    elif j == "p" or j == "q" or j == "r" or j == "s":
        ans += "7"
    elif j == "t" or j == "u" or j == "v":
        ans += "8"
    elif j == "w" or j == "x" or j == "y" or j == "z":
        ans += "9"

print(ans)
