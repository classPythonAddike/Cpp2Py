from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.CodeParser = LexerGenerator()
    
    def add_commands(self):
        #Commands
        self.CodeParser.add("PRINT", r'cout')
        self.CodeParser.add("INPUT", r'cin')
        self.CodeParser.add("INCL", r'include')
        self.CodeParser.add("USE", r'using')
        self.CodeParser.add("NMSPC", r'namespace')
        self.CodeParser.add("STD", r'std')
        self.CodeParser.add("INT", r'int')
        self.CodeParser.add("STR", r'string')
        self.CodeParser.add("BOOL", r'bool')
        self.CodeParser.add("VOID", r'void')
        self.CodeParser.add("MAIN_FUNC", r'main')
        self.CodeParser.add("ENDL", r'endl')
        self.CodeParser.add("IF", r'if')
        self.CodeParser.add("RETURN", 'return')
        self.CodeParser.add("ELSE", r'else')

        #Miscellaneous
        self.CodeParser.add('OPEN_PAREN', r'\(')
        self.CodeParser.add('CLOSE_PAREN', r'\)')
        self.CodeParser.add('OPEN_ANG', r'\<')
        self.CodeParser.add('CLOSE_ANG', r'\>')
        self.CodeParser.add('OPEN_CURLY', r'\{')
        self.CodeParser.add('CLOSE_CURLY', r'\}')
        self.CodeParser.add('HASH', r'\#')
        self.CodeParser.add('NUM', r'\d+')
        self.CodeParser.add('TRUE', r'true')
        self.CodeParser.add('FALSE', r'false')
        self.CodeParser.add('ENDC', r'\;')
        self.CodeParser.add('PUT', r'<<')
        self.CodeParser.add('GET', r'>>')
        self.CodeParser.add('VARIABLE', r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.CodeParser.add('STRING', r'("(.*?))"|(\'(.*?)\')')
        self.CodeParser.add('COMMENTSTART', r'//')

        #Operations
        self.CodeParser.add('SUM', r'\+')
        self.CodeParser.add('SUB', r'\-')
        self.CodeParser.add('PROD', r'\*')
        self.CodeParser.add('DIV', r'\/')
        self.CodeParser.add('MOD', r'\%')
        self.CodeParser.add('EQUAL_TO', r'\=')

        #Ignore
        self.CodeParser.ignore(r'\s+')
        self.CodeParser.ignore(r'\t')
        self.CodeParser.ignore('\n')
    
    def build_Lexer(self):
        self.add_commands()
        return self.CodeParser.build()

if __name__ == "__main__":
    CPPLexer = Lexer().build_Lexer()
    file = open('Example.cpp', 'r')
    code = file.read()
    file.close()
    tokens = CPPLexer.lex(code)
    for t in tokens:
        print(t.__dict__)