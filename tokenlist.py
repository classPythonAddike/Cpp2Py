tokenlist = ["PRINT", "INPUT", "INCL", "USE", "NMSPC",
"STD", "INT", "STR", "BOOL", "VOID",
"ENDL", "IF", "RETURN", "ELSE", "OPEN_PAREN",
"CLOSE_PAREN", "OPEN_ANG", "CLOSE_ANG", "OPEN_CURLY",
"CLOSE_CURLY", "HASH", "NUM", "ENDC", "VARIABLE", "STRING", "TRUE", "FALSE",
"COMMENTSTART", "SUM", "SUB", "PROD", "DIV", "MOD", "EQUAL_TO"]
precedence = [
    ('left', ['SUM', 'SUB']),
    ('left', ['PROD', 'DIV', 'MOD'])
]