def brackets(line: str):
    closing = {"]": "[", ")": "(", "}": "{"}
    opening = {"{", "(", "["}
    stack = []
    for index, bracket in enumerate(line, 1):
        if bracket in closing:
            if not stack or closing[bracket] != stack.pop()[0]:
                return index
        else:
            if bracket in opening:
                stack.append((bracket, index))
    if not len(stack):
        return "Success"
    else:
        return stack.pop()[1]


if __name__ == '__main__':
    line = input()
    print(brackets(line))
