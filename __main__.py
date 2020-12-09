import sys
from os.path import splitext
from rply import ParserGenerator
from tokenlist import *
from lexer import Lexer
CPPLexer = Lexer().build_Lexer()

'''
file = sys.argv[1]
f = open(file, 'r')
code = f.read()
f.close()

filename = splitext(file)[0] + ".py"

print(f"C++ Source File: {file}")
print(f"Output Python File: {filename}")
'''

text = ""


pg = ParserGenerator(tokenlist, precedence)

'''
cout << string;
cout << integer;
cout << boolean;
cout << variable;
'''

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG STRING ENDC')
def cout_str(p):
    global text
    text += f'print({p[3].value})\n'
    return 0

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG NUM ENDC')
def cout_int(p):
	global text
	text += f"print({p[3].value})\n"
	return 0

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG TRUE ENDC')
def cout_true(p):
	global text
	text += "print(True)\n"
	return 0

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG FALSE ENDC')
def cout_false(p):	
	global text
	text += "print(False)\n"
	return 0

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG VARIABLE ENDC')
def cout_var(p):
	global text
	text += f"print({p[3].value})\n"
	return 0

@pg.production('expression : INPUT CLOSE_ANG CLOSE_ANG VARIABLE ENDC')
def cin(p):
    global text
    text += f"{p[0]} = input()\n"
    return 0

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()

cde = """cout << true;
cout << false;"""

for i in cde.split("\n"):
	t = parser.parse(CPPLexer.lex(i))

print(text)

'''
print("Finished coverting C++ to Python")
print(f"Writing Python program to: Example.py")
Py = open('Example.py', 'w')
Py.write(text.strip())
Py.close()
'''