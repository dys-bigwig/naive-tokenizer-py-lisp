from lex import Lexer

def parse(tokens):
    token = next(tokens, None)
    if not token:
        raise SyntaxError("unexpected EOF")
    if token == '(':
        l = []
        while tokens.peek() != ')':
            l.append(parse(tokens))
        next(tokens, None)
        return l
    elif token == ')':
        raise SyntaxError("unexpected )")
    else:
        return token

def main():
    l = Lexer("(+ (* num.A num-B))")
    print(parse(l))


if __name__ == '__main__':
    main()
