#Stack을 사용한 괄호 VPS
print('원하는 문자열을 입력하세요');

input_ = input()
input_list = list(input_)

length = len(input_list)

count = 0
result = 0

while count<length :
        top = input_list.pop()
        if top == '(' :
                result += 1
        elif top == ')' :
                result -= 1
        count+=1

if result != 0 or top == ')':
    print('FAIL')
else :
    print("SUCCESS")
