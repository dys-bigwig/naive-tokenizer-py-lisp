class Lexer:
    def __init__(self, src):
        self.src = src
        self.pos = 0;
        self.length = len(src)
        self.tok = self.advance()        

    def __iter__(self):
        return self
    
    def peek(self):
        return self.tok

    def __next__(self):
        retval = self.tok
        self.tok = self.advance()
        return retval
    
    def advance(self):
        if self.pos > self.length - 1:
            raise StopIteration
        else:
            ch = self.src[self.pos]
            while ch == ' ':
                self.pos += 1
                if self.pos > self.length:
                    raise StopIteration
                else:
                    ch = self.src[self.pos]
            if ch in '()':
                self.pos += 1
                return ch
            else:
                buffer = []
                while ch not in ' ()':
                    buffer.append(ch)
                    self.pos += 1
                    if self.pos > self.length:
                        raise StopIteration
                    else:
                        ch = self.src[self.pos]
                return "".join(buffer)


def main():
    l = Lexer("(+ (* numA numB) numC))")
    print("first peek = " + l.peek())
    for tok in l:
        print("token = " + tok)
        print("peek = " + l.peek())

if __name__ == '__main__':
    main()
