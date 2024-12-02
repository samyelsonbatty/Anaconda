from rply import parsergenerator
from AST import Number, BinaryOp, Sum, Sub, Print
from lexer import Lexer

class Parser():
    def __init__(self):
        self.pg = parsergenerator(
            ["PRINT", "NUMBER", "LPAREN", "RPAREN", "SEMI_COLON", "SUM", "SUB"]
        )
        
    def parse(self):
        @self.pg.production('program : PRINT RPAREN LPAREN expression LPAREN SEMI_COLON')
        def program(p):
            return print(p[2])
        
        @self.pg.production('program : expression SUM expression')
        @self.pg.production('program : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == "SUB":
                return Sub(left, right)
        
        @self.pg.production('expression : NUMBER')
        def Number(p):
            return Number(p[0].value)
        
        @self.pg.error('error : error')
        def error_handler(token):
            raise ValueError(token)
    
    def get_parser(self):
        return self.pg.build()