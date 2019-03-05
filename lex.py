class Lexer:
    def __init__(self, src):
        self.src = src
        self.pos = 0;
        self.length = len(src)

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos > self.length - 1:
            raise StopIteration
        else:
            ch = self.src[self.pos]
            if ch == ' ':
                self.pos += 1
                return next(self)
            elif ch in '()':
                self.pos += 1
                return ch
            else:
                buffer = []
                while ch not in ' ()':
                    buffer.append(ch)
                    self.pos += 1
                    ch = self.src[self.pos]
                return "".join(buffer)


def main():
    l = Lexer("(* (- 5 6) 7)")
    for tok in l:
        print("token = " + tok)

if __name__ == '__main__':
    main()
