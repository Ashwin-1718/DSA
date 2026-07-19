def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():   
            stack.append(int(token))
        else:                
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)  
            elif token == '%':
                stack.append(a % b)
            elif token == '^':
                stack.append(a ** b)
            else:
                print("Unknown operator:", token)
                return None

    return stack.pop() 

expr = input("Enter a postfix expression: ")
result = evaluate_postfix(expr)
print("Result:", result)