#a, b = map(int, input("a").split())
#print(a+b, a-b, a*b, a/b, a%b)

b = input()
s = list(b)
sum = 0

for i in range(len(s)):
    if s[i] == "(":
        sum += 1
    elif s[i] == ")":
        sum -= 1

if sum == 0 and s[0] == "(":
    print("yes")
else :
    print("no")
    


    


