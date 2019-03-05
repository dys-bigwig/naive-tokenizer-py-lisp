from lex import Lexer
from more_itertools import peekable


def parse(tokens):
    token = next(tokens)
    if token == None:
        raise SyntaxError("unexpected EOF")
    if token == '(':
        l = []
        while tokens.peek() != ')':
            l.append(parse(tokens))
        next(tokens)
        return l
    elif token == ')':
        raise SyntaxError("why rparen, why")
    else:
        return token

def main():
    l = peekable(Lexer("(+ 3 (- 4 4) (* 1 2))"))
    print(parse(l))


if __name__ == '__main__':
    main()
