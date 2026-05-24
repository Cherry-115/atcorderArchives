X = int(input())
S = list("HelloWorld")

print("".join(S[:X-1])+"".join(S[X:]))