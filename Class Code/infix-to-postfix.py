def prec(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return -1 

def postfix(infix):
    stack = []
    postfix = ""

    for ch in infix:
        if ch == ' ':
            continue  

        if ch.isalnum():
            postfix += ch
       
        elif ch == '(':
            stack.append(ch)
        
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()  
        else:
            while stack and prec(stack[-1]) >= prec(ch):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix

infix = input("Enter infix expression: ")
result = postfix(infix)
print("Postfix expression:", result)
