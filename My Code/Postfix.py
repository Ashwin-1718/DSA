def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():   # Operand → push
            stack.append(int(token))
        else:                 # Operator → pop two operands
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)  # float division
            elif token == '%':
                stack.append(a % b)
            elif token == '^':
                stack.append(a ** b)
            else:
                print("Unknown operator:", token)
                return None

    return stack.pop() 

expr = input("Enter a postfix expression (use space between tokens): ")
result = evaluate_postfix(expr)
print("Result:", result)
