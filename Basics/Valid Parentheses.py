def code(s):
    stack=[]
    count=0
    dict={')':'(',']':'[','}':'{'}
    for i in s:
        if i in dict:
            if stack and stack[-1]==dict[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
            count+=1
    return count if not stack else -1
s="()("
print(code(s))
