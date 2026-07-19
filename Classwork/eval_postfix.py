def eval_postfix(expression):
    stack=[]
    token_list=expression.split()
    
    for item in token_list:
        if item.isdigit():  #operand
            stack.append(int(item))
        else: #operator
            a=stack.pop()
            b=stack.pop()
            ans=calc(a,b,item)
            stack.append(ans)
    return stack.pop()

def calc(a,b,op):
    if op=="+":
        return b+a
    elif op=="-":
        return b-a
    elif op=="/":
        return b/a
    elif op=="*":
        return b*a
    elif op=="^":
        return pow(b,a)
    else:
        return None

expression=input("Enter postfix expression")
result=eval_postfix(expression)
print(result)