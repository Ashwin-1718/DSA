def prec(op):
    if op=="^":
        return  3
    elif op=="/" or op=="*":
        return 2
    elif op=="+" or op=="-":
        return 1
    else:
        return -1

def postfix(infix):
    stack=[]
    postfix=""

    for i in range(len(infix)):
        ch=infix[i]

        #'(' left parenthesis
        if ch=='(':
            stack.append('(')
        
        #operand
        elif (ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9'):
            postfix+=ch

        #')' Right parenthesis
        elif ch==')':
            while stack[-1]!='(':
                postfix+=stack.pop()
            stack.pop()
        
        #operator
        else:
            while stack and (prec(stack[-1])> prec(ch) or prec(stack[-1])==prec(ch)):
                postfix+=stack.pop()
            stack.append(ch)
            

    while stack:
        postfix+=stack.pop()
    return postfix



infix=input("Enter infix expression: ")
result=postfix(infix)
print(result)