num = int(input("숫자입력: "))

for i in range(num):
    vps = list(input("괄호입력: "))
    while len(vps) != 0:
        if vps[0] == ')':
            print("NO")
            break
        else:
            if ')' in vps:
                vps.remove(')')
                vps.remove('(')
            else:
                print("NO")
                break
    if len(vps)==0:
        print("YES")
        