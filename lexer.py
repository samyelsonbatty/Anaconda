from rply import lexergenerator

class Lexer():
    def __init__(self):
        self.lexer = lexergenerator()
        
    def _add_tokens(self):
        self.lexer.add("PRINT", r'print')
        
        self.lexer.add("LPAREN", r"\(")
        self.lexer.add("RPAREN", r"\)")
        
        self.lexer.add('SUM', r"\+")
        self.lexer.add('SUB', r"\-")
        
        self.lexer.add("SEMI_COLON", r'\;')
        
        self.lexer.add("NUMBER", r"\d+")
        
        self.lexer.ignore(' \t+')
        
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()