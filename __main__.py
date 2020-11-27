import sys
from os.path import splitext
from rply import ParserGenerator
from tokenlist import *
from Parser import Lexer
CPPLexer = Lexer().build_Lexer()

'''
file = sys.argv[1]
f = open(file, 'r')
code = f.read()
f.close()
tokens = CPPLexer.lex(code)

stemmed_code = []
for t in tokens:
    stemmed_code.append((t.__dict__['value'], t.__dict__['name']))

filename = splitext(file)[0] + ".py"

print(f"C++ Source File: {file}")
print(f"Output Python File: {filename}")
'''
text = ""


pg = ParserGenerator(tokenlist, precedence)

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG expression ENDC')
def cout(p):
    global text
    text += f'print("{p[0]}")'
    return 0

@pg.production('expression : INPUT CLOSE_ANG CLOSE_ANG expression ENDC')
def cin(p):
    global text
    text += f"{p[0]} = input()"
    return 0

parser = pg.build()

cde = """a + b"""
parser.parse(CPPLexer.lex(cde))
print(text)

'''
print("Finished coverting C++ to Python")
print(f"Writing Python program to: {filename}")
Py = open(filename, 'w')
Py.write(text.strip())
Py.close()
'''