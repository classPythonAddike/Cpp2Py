import sys
from os.path import splitext
from lexer import Lexer
from Parser import parser
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

cde = \
"""
// hi hello
cout << true;
cout << false;
if (a == 'b'){
"""

text = ''

print("C++ code:")
for i in cde.strip().split("\n"):
	print(i)
	text += parser.parse(CPPLexer.lex(i))
print("\nPython Code:")
print(text)

'''
print("Finished coverting C++ to Python")
print(f"Writing Python program to: Example.py")
Py = open('Example.py', 'w')
Py.write(text.strip())
Py.close()
'''