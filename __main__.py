import sys
from os.path import splitext
import pickle

file = sys.argv[1]

f = open(file, 'r')
code = f.read()
f.close()

try:
    with open("Lexer.pkl", "rb") as w:
        CPPLexer = pickle.load(f)
except:
    from Parser import Lexer
    CPPLexer = Lexer().build_Lexer()
    with open("Lexer.pkl", "wb") as w:
        pickle.dump(CPPLexer, w)
tokens = CPPLexer.lex(code)

stemmed_code = []
for t in tokens:
    stemmed_code.append((t.__dict__['value'], t.__dict__['name']))

filename = splitext(file)[0] + ".py"

print(f"C++ Source File: {file}")
print(f"Output Python File: {filename}")

text = ""
currentCommand = []
ignore = [None, "HI"]
ignoreCommand = None

for e, i in enumerate(stemmed_code):

    if i[0] == ignore[0] or ignore[1] == 0:
        ignore[1] = ignore[1] - 1
    
    if ignore[1] != "HI":
        if ignore[1] > -1:
            continue

    if ignore[1] == -1:
        ignore = ["HI", "HI"]

        if ignoreCommand == "PRINT":
            text += f"({i[0]})"
        
        if ignoreCommand == "INPUT":
            text += "()"
        continue

    if i[0] == ";":
        text += "\n"
    
    elif i[0] == "cout":
        text += "print"
        ignore = ["<", 2]
        ignoreCommand = i[1]
    
    elif i[0] == "cin":
        text += f"{stemmed_code[e + 3][0]} = "
        text += "input"
        ignore = [">", 2]
        ignoreCommand = i[1]
    
    if i[1] in ["OPEN_PAREN", "OPEN_CURLY"]:
        currentCommand.append([i[1], False])

    if i[1] in [r"CLOSE_PAREN", "CLOSE_CURLY"]:
        l = ["OPEN_PAREN", "OPEN_CURLY"]
        v = ["CLOSE_PAREN", "CLOSE_CURLY"].index(i[1])
        Commands = currentCommand[0:]
        Commands.reverse()
        pos = -1 * (Commands.index([l[v], False]) + 1)
        currentCommand[pos][1] = True
    
    print(f"{e}. Token: {i}")

print("Finished coverting C++ to Python")
print(f"Writing Python program to: {filename}")
Py = open(filename, 'w')
Py.write(text.strip())
Py.close()