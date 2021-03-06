import sys
from os.path import splitext
from lexer import Lexer
from rply import ParserGenerator
from tokenlist import *
from objects import *
CPPLexer = Lexer().build_Lexer()

try:
	file = sys.argv[1]
except:
	file = "ExampleFile.cpp"

f = open(file, 'r')
code = f.read()
f.close()

filename = splitext(file)[0] + ".py"

print(f"C++ Source File: {file}")
print(f"Output Python File: {filename}")
text = ''

tabs = 0

pg = ParserGenerator(tokenlist, precedence)

'''
#include "iostream"
#include "iostream.h"
#include <iostream>
#include <iostream.h> ---> Not yet coded!!
'''
@pg.production('expression : HASH INCL STRING')
def incl_iostr(p):
	return ""

@pg.production('expression : HASH INCL OPEN_ANG VARIABLE CLOSE_ANG')
def incl_var(p):
	return ""

'''
using namespace std;
'''
@pg.production('expression : USE NMSPC STD ENDC')
def using_namespace(p):
	return "\n"

'''
variable
integer
string
true
false
endl
'''
@pg.production('expression : VARIABLE')
def variable(p):
	return Data(p[0].value)

@pg.production('expression : NUM')
def integer(p):
	return Data(p[0].value)

@pg.production('expression : STRING')
def string(p):
	return Data(p[0].value)

@pg.production('expression : TRUE')
def true(p):
	return Data(p[0].value)

@pg.production('expression : FALSE')
def false(p):
	return Data(p[0].value)

@pg.production('expression : ENDL')
def endline(p):
	return Data(p[0].value)

'''
expression << expression
'''
@pg.production('expression : expression OPEN_ANG OPEN_ANG expression')
def i(p):
	return Concat(p[0], p[3])

'''
cout << string;
cout << integer;
cout << boolean;
cout << variable;
cout << endl;
cout << expression;
'''
@pg.production('expression : PRINT OPEN_ANG OPEN_ANG STRING ENDC')
def cout_str(p):
	return f"print({p[3].value}, end = '')\n"
@pg.production('expression : PRINT OPEN_ANG OPEN_ANG NUM ENDC')
def cout_int(p):
	return f"print({p[3].value}, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG TRUE ENDC')
def cout_true(p):
	return f"print(True, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG FALSE ENDC')
def cout_false(p):
	return f"print(False, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG VARIABLE ENDC')
def cout_var(p):
	return f"print({p[3].value}, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG ENDL ENDC')
def cout_endl(p):
	return f"print()"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG expression ENDC')
def cout_exp(p):
	return f"print({p[3].value}, end = '')\n"


'''
cin << variable;
'''
@pg.production('expression : INPUT CLOSE_ANG CLOSE_ANG VARIABLE ENDC')
def cin(p):
	return f"{p[3].value} = input()\n"


'''
comments
'''
@pg.production('expression : COMMENTSTART expression')
def ignore_comment(p):
	y = [p[i] for i in range(1, len(p))]
	return f"# {' '.join(y)} \n"

@pg.production('expression : COMMENTSTART expression expression')
def ignore_comment(p):
	y = [p[i] for i in range(1, len(p))]
	return f"# {' '.join(y)} \n"

@pg.production('expression : COMMENTSTART expression expression expression')
def ignore_comment(p):
	y = [p[i] for i in range(1, len(p))]
	return f"# {' '.join(y)} \n"

@pg.production('expression : COMMENTSTART expression expression expression expression')
def ignore_comment(p):
	y = [p[i] for i in range(1, len(p))]
	return f"# {' '.join(y)} \n"

'''
FUNCTIONS

int func(){
bool func(){
string func(){
void func(){
'''
@pg.production('expression : INT VARIABLE OPEN_PAREN CLOSE_PAREN OPEN_CURLY')
def start_int(p):
	global tabs
	tabs += 0.5
	return f"def {p[1].value}():\n"

@pg.production('expression : BOOL VARIABLE OPEN_PAREN CLOSE_PAREN OPEN_CURLY')
def start_bool(p):
	global tabs
	tabs += 0.5
	return f"def {p[1].value}():\n"

@pg.production('expression : STR VARIABLE OPEN_PAREN CLOSE_PAREN OPEN_CURLY')
def start_str(p):
	global tabs
	tabs += 0.5
	return f"def {p[1].value}():\n"

@pg.production('expression : VOID VARIABLE OPEN_PAREN CLOSE_PAREN OPEN_CURLY')
def start_void(p):
	global tabs
	tabs += 0.5
	return f"def {p[1].value}():\n"

'''
func()
'''
@pg.production('expression : VARIABLE OPEN_PAREN CLOSE_PAREN ENDC')
def call_func(p):
	return f"{p[0].value}()\n"

'''
}
'''
@pg.production('expression : CLOSE_CURLY')
def close_curly(p):
	global tabs
	tabs -= 0.5
	return "\n"

'''
errors
'''
@pg.error
def error_handler(token):
	raise ValueError("Ran into a %s where it wasn't expected" % token.value)

parser = pg.build()

print("\nC++ code:")
for i in code.strip().split("\n"):
	if i != "":
		print(i)
		try:
			text += ('    ' * int(tabs)) + parser.parse(CPPLexer.lex(i)).value
		except:
			text += ('    ' * int(tabs)) + str(parser.parse(CPPLexer.lex(i)))
	else:
		text += "\n"

text = text.strip() + "\nmain()"
print("\nPython Code:")
print(text)


print("\nFinished transpiling C++ code.")
print(f"Writing Python program to: {filename}")
Py = open(filename, 'w')
Py.write(text.strip())
Py.close()
