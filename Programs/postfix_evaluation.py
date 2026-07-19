def postfixEval(postfixExpr):
    operandStack = []
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token.isdigit():
            operandStack.append(int(token))
        else:
            a = operandStack.pop()
            b = operandStack.pop()
            result = calc(token, a, b)
            operandStack.append(result)
    return operandStack.pop()


def calc(op, a, b):
    if op == "*":
        return b * a
    elif op == "/":
        return b / a
    elif op == "+":
        return b + a
    elif op == "^":
        return pow(b,a)
    elif op == "-":
        return b - a
    else: 
        return -1

expression=input("Enter the postfix expression: ")
print("Answer is:", postfixEval(expression))