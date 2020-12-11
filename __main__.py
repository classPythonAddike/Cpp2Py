import sys
from os.path import splitext
from lexer import Lexer
from Parser import parser
CPPLexer = Lexer().build_Lexer()


file = sys.argv[1]
f = open(file, 'r')
code = f.read()
f.close()

filename = splitext(file)[0] + ".py"

print(f"C++ Source File: {file}")
print(f"Output Python File: {filename}")


cde = \
"""
cout << true;
cout << fal << "hi" << hi << endl;
"""

text = ''

print("C++ code:")
for i in code.strip().split("\n"):
	print(i)
	try:
		text += parser.parse(CPPLexer.lex(i)).value
	except:
		text += str(parser.parse(CPPLexer.lex(i)))
print("\nPython Code:")
print(text)


print("Finished coverting C++ to Python")
print(f"Writing Python program to: {filename}")
Py = open(filename, 'w')
Py.write(text.strip())
Py.close()