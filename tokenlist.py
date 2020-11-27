tokenlist = ["PRINT", "INPUT", "INCL", "USE", "NMSPC",
"STD", "INT", "STR", "BOOL", "VOID", "MAIN_FUNC",
"ENDL", "ENDL", "IF", "RETURN", "ELSE", "OPEN_PAREN",
"CLOSE_PAREN", "OPEN_ANG", "CLOSE_ANG", "OPEN_CURLY",
"CLOSE_CURLY", "HASH", "NUM", "ENDC", "VARIABLE", "STRING",
"COMMENTSTART", "SUM", "SUB", "PROD", "DIV", "MOD"]
precedence = [
    ('left', ['SUM', 'SUB']),
    ('left', ['PROD', 'DIV', 'MOD'])
]