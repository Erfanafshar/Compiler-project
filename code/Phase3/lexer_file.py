from ply import lex
import string


class Lexer:
    reserved = {
        "int": "INTEGER",
        "float": "FLOAT",
        "bool": "BOOLEAN",
        "fun": "FUNCTION",
        "True": "TRUE",
        "False": "FALSE",
        "print": "PRINT",
        "return": "RETURN",
        "main": "MAIN",
        "if": "IF",
        "else": "ELSE",
        "elseif": "ELSEIF",
        "while": "WHILE",
        "on": "ON",
        "where": "WHERE",
        "for": "FOR",
        "and": "AND",
        "or": "OR",
        "not": "NOT",
        "in": "IN"
    }

    tokens = [
                 "ID", "INTEGERNUMBER", "FLOATNUMBER", "SUM", "SUB", "MUL", "DIV", "MOD", "ERROR", "ASSIGN",
                 "GT", "GE", "LT", "LE", "EQ", "NE", "LCB", "RCB", "LRB", "RRB", "LSB", "RSB", "SEMICOLON",
                 "COLON", "COMMA", "OPERATOR"
             ] + list(reserved.values())

    operators = {
        "+": "SUM",
        "-": "SUB",
        "*": "MUL",
        "/": "DIV",
        "%": "MOD"
    }

    t_ASSIGN = r"="
    t_GT = r">"
    t_GE = r">="
    t_LT = r"<"
    t_LE = r"<="
    t_EQ = r"=="
    t_NE = r"!="
    t_LCB = r"\{"
    t_RCB = r"\}"
    t_LRB = r"\("
    t_RRB = r"\)"
    t_LSB = r"\["
    t_RSB = r"\]"
    t_SEMICOLON = r";"
    t_COLON = r":"
    t_COMMA = r","
    t_SUM = r"\+"
    t_ignore = " \n\t"

    def t_ID(self, t):
        r"""[a-zA-Z_0-9]*[a-zA-Z_][a-zA-Z_0-9]*"""
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words
        if t.type == "ID":
            # starts with number or uppercase
            if t.value[0].isupper() or t.value[0].isnumeric():
                t.type = "ERROR"
                return t
        return t

    def t_FLOATNUMBER(self, t):
        r"""(\d*\.[0-9\.]*)"""

        if t.value.count(".") > 1:
            t.type = "ERROR"
            return t

        if t.value[0] == ".":
            t.type = "ERROR"
            return t

        if len(t.value.split(".")[0]) > 9:
            t.type = "ERROR"
            return t

        t.value = float(t.value)
        return t

    def t_INTEGERNUMBER(self, t):
        r"""(\d+)"""

        if len(t.value) > 9:
            t.type = "ERROR"
            return t
        t.value = int(t.value)
        return t

    def t_OPERATOR(self, t):
        r"""[+\-*%/\s]+"""

        t.value = t.value.translate({ord(c): None for c in string.whitespace})

        if len(t.value) > 1:
            t.type = "ERROR"
        else:
            t.type = self.operators.get(t.value)
        return t

    def t_error(self, t):
        t.type = "ERROR"

        t.lexer.skip(len(t.value))
        return t

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
