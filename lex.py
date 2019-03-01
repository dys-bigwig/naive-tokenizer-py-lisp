
from collections import namedtuple as NamedTuple

def lex(exp):
    Token = NamedTuple("TOKEN", ("type", "value"))
    tokens = []
    buffer = []
    state = "START"
    i = 0

    while i < len(exp):
        char = exp[i]
        if state == "START":
            if char not in ' ()':
                if char == '"':
                    state = "STRING"
                    i += 1
                else:
                    state = "IDENTIFIER"
            else:
                if char == '(':
                    tokens.append(Token('L_PAREN','('))
                elif char == ')':
                    tokens.append(Token('R_PAREN',')'))
                i += 1
        elif state == "IDENTIFIER":
            if char not in ' ()':
                buffer.append(char)
                i += 1
            else:
                identifier = "".join(buffer)
                if identifier.isnumeric():
                    tokens.append(Token('NUMBER', identifier))
                else:
                    tokens.append(Token('IDENTIFIER', identifier))
                buffer.clear()
                state = "START"
        elif state == "STRING":
            if char != '"':
                buffer.append(char)
                i += 1
            else:
                string = "".join(buffer)
                tokens.append(Token('STRING', string))
                buffer.clear()
                i += 1
                state = "START"
    return tokens
