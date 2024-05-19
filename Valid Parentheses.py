def valid_parentheses(s:str)->bool:
    stack:list = []
    match:dict = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for bracket in s:
        if bracket in match:
            if stack and stack[-1] == match[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return not stack

ans = valid_parentheses("()[]{}")

print(ans)
