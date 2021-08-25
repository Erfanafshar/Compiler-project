import os

from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        pass

    def generate_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code += p[1].code + os.linesep + p[3].code + os.linesep
        p[0].code += p[0].place + " = "
        p[0].code += str(p[1].get_value()) + " " + p[2] + " " + str(p[3].get_value()) + ";"
        # print(p[0].code)

        p[0].vars += p[1].vars + " " + p[3].vars + " " + p[0].place + " "

    def generate_relop_code(self, p, t_lab, f_lab, extra_lab):
        p[0] = NonTerminal()
        p[0].true = t_lab
        p[0].false = f_lab
        if len(p[1].code + p[3].code) > 0:
            p[1].code = p[1].code.replace("Ltrue", extra_lab)
            p[0].code = p[1].code + p[3].code + "\n" + extra_lab + ": "
        p[0].code += "if(" + str(p[1].get_value()) + " " + p[2] + " "
        p[0].code += str(p[3].get_value()) + ")" + " goto " + p[0].true + ";" + os.linesep
        p[0].code += "goto " + p[0].false + ";"
        p[0].place = p[3].get_value()

        p[0].vars += p[1].vars + " " + p[3].vars + " "

        # p[0] = NonTerminal()
        # p[0].place = temp
        # p[0].code = str(p[1].get_value()) + " " + p[2] + " " + str(p[3].get_value())
        # print(p[0].code)
