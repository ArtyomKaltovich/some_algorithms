import sys


def exec_cmd(cmd: str, stack, max_stack):
    if cmd.startswith("push"):
        _, _, elem = cmd.partition(" ")
        elem = int(elem.strip())
        stack.append(elem)
        if not max_stack or elem > max_stack[-1]:
            max_stack.append(elem)
        else:
            max_stack.append(max_stack[-1])
    elif cmd.startswith("pop"):
        stack.pop()
        max_stack.pop()
    else:
        return max_stack[-1]


if __name__ == '__main__':
    n = int(next(sys.stdin))
    stack = []
    max_stack = []
    commands = []
    for _ in range(n):
        commands.append(next(sys.stdin))
    if n > 10:
        print(commands)
    for command in commands:
        result = exec_cmd(command, stack, max_stack)
        if result:
            print(result)
