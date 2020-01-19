class ParseError(SyntaxError):
    
    def __init_(self, error: str):
        super().__init__(error)