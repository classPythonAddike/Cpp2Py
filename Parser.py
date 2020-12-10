from rply import ParserGenerator
from tokenlist import *

pg = ParserGenerator(tokenlist, precedence)

'''
variable
integer
string
true
false
'''
@pg.production('expression : VARIABLE')
def variable(p):
	return f"{p[0].value}"

@pg.production('expression : NUM')
def integer(p):
	return f"{p[0].value}"

@pg.production('expression : STRING')
def string(p):
	return f"{p[0].value}"

@pg.production('expression : TRUE')
def true(p):
	return f"{p[0].value}"

@pg.production('expression : FALSE')
def false(p):
	return f"{p[0].value}"

@pg.production('expression : EQUAL_TO')
def is_equal(p):
	return "="

'''
cout << string;
cout << integer;
cout << boolean;
cout << variable;
cout << endl;
'''
@pg.production('expression : PRINT OPEN_ANG OPEN_ANG STRING ENDC')
def cout_str(p):
    return f'print({p[3].value}, end = '')\n'

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG NUM ENDC')
def cout_int(p):
	return f"print({p[3].value}, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG TRUE ENDC')
def cout_true(p):
	return "print(True, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG FALSE ENDC')
def cout_false(p):
	return "print(False, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG VARIABLE ENDC')
def cout_var(p):
	return f"print({p[3].value}, end = '')\n"

@pg.production('expression : PRINT OPEN_ANG OPEN_ANG ENDL ENDC')
def cout_endl(p):
	return "print()"


'''
cin << variable;
'''
@pg.production('expression : INPUT CLOSE_ANG CLOSE_ANG VARIABLE ENDC')
def cin(p):
    return f"{p[0]} = input()\n"


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
errors
'''
@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()