def lex(exp):
    tokens = []
    buffer = []
    state = "START"
    i = 0

    while i < len(exp):
        char = exp[i]
        if state == "START":
            if char not in ' ()':
                state = "IDENTIFIER"
            else:
                if char == '(':
                    tokens.append('(')
                elif char == ')':
                    tokens.append(')')
                i += 1
        elif state == "IDENTIFIER":
            if char not in ' ()':
                buffer.append(char)
                i += 1
            else:
                tokens.append("".join(buffer))
                buffer.clear()
                state = "START"

    print(tokens)

lex(" ((lambda (  x) (* x x ))    7)")
