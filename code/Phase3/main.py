from lexer_file import Lexer
from parser_file import Parser


def print_begin():
    print("#include <stdio.h>")
    print()
    print("int array[(int)1e6];")
    print()
    print("")
    print("")
    print("")
    print("int main()")
    print("{")


def print_end():
    print("return 0;")
    print("}")


# file
file = open("test.txt")
text_input = file.read()
file.close()

# lexer
lexer = Lexer().build()
lexer.input(text_input)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)


# # parser
parser = Parser()
print_begin()
parser.build().parse(text_input, lexer, False)
print_end()
parser.print_symbol_table()
