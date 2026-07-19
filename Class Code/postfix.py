def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
    

expression = input("Enter ")
result = evaluate_postfix(expression)