from lex import lex

def parse_tokens(program):
    return parse(lex(program))

def parse(tokens):
    if len(tokens) == 0:
        raise SyntaxError
    token = tokens.pop(0)
    if token.type == 'L_PAREN':
        L = []
        while tokens[0].type != 'R_PAREN':
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token.type == 'R_PAREN':
        raise SyntaxError
    else:
        return atom(token)

def atom(token):
    if token.type == 'NUMBER':
        return int(token.value)
    else:
        return str(token.value)

print(parse_tokens('(+ (- 1 1) (+ 0 0))'))
