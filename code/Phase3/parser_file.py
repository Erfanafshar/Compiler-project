import os

from ply import yacc
from lexer_file import Lexer
from nonTerminal import NonTerminal
from codeGenerator import CodeGenerator
from symbolTable import SymbolTable
from memory import Memory


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        self.tempCount = 0
        self.tempCount2 = 0
        self.codeGenerator = CodeGenerator()
        self.symbolTable = SymbolTable()
        self.memory = Memory()
        self.print_str = False
        self.enable_symbol_tree = True
        self.enable_code_generation = True
        self.print_sym_tree = True

    def print_symbol_table(self):
        if self.print_sym_tree:
            self.symbolTable.print_table()

    # 1 *
    def p_program_declist(self, p):
        """program : declist MAIN LRB RRB block"""
        if self.print_str:
            print("""       program : declist MAIN LRB RRB block""")
        if self.enable_symbol_tree:
            self.symbolTable.function_detect("main", "void")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code_pr = p[1].code2 + os.linesep + p[5].code2

            vars = p[1].vars + " " + p[5].vars
            for var in vars.split(" "):
                if var != "":
                    if var not in p[0].vars:
                        p[0].vars += var + ","

            for var in p[0].vars[:-1].split(","):
                print("int " + var + ";")

            print(p[0].code_pr)

    def p_program_main(self, p):
        """program : MAIN LRB RRB block"""
        if self.print_str:
            print("""       program : MAIN LRB RRB block""")
        if self.enable_symbol_tree:
            self.symbolTable.function_detect("main", "void")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code_pr = p[4].code2

            for var in p[4].vars.split(" "):
                if var != "":
                    if var not in p[0].vars:
                        p[0].vars += var + ","

            for var in p[0].vars[:-1].split(","):
                print("int " + var + ";")

            print(p[0].code_pr)

    # 2 *
    def p_declist_dec(self, p):
        """declist : dec"""
        if self.print_str:
            print("""       declist : dec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code2 = p[1].code

            p[0].vars += p[1].vars + " "

    def p_declist_declist(self, p):
        """declist : declist dec"""
        if self.print_str:
            print("""       declist : declist dec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 3
    def p_dec_vardec(self, p):
        """dec : vardec"""
        if self.print_str:
            print("""       dec : vardec""")
        if self.enable_symbol_tree:
            self.symbolTable.declaration_detect()
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[1].code

            p[0].vars += p[1].vars + " "

    def p_dec_funcdec(self, p):
        """dec : funcdec"""
        if self.print_str:
            print("""       dec : funcdec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 4
    def p_type_int(self, p):
        """type : INTEGER"""
        if self.print_str:
            print("""       type : INTEGER""")
        if self.enable_symbol_tree:
            p[0] = NonTerminal()
            p[0].type = p[1]
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_type_float(self, p):
        """type : FLOAT"""
        if self.print_str:
            print("""       type : FLOAT""")
        if self.enable_symbol_tree:
            p[0] = NonTerminal()
            p[0].type = p[1]
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_type_bool(self, p):
        """type : BOOLEAN"""
        if self.print_str:
            print("""       type : BOOLEAN""")
        if self.enable_symbol_tree:
            p[0] = NonTerminal()
            p[0].type = p[1]
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 5
    def p_iddec_id1(self, p):
        """iddec : ID"""
        if self.print_str:
            print("""       iddec : ID""")
        if self.enable_symbol_tree:
            self.symbolTable.add_var(p[1])
        if self.enable_code_generation:
            p[0] = NonTerminal()
            # print("int " + p[1] + ";")
            p[0].code = "int " + p[1] + ";" + os.linesep

            # p[0].vars += p[1] + " "

    def p_iddec_id2(self, p):
        """iddec : ID LSB exp RSB"""
        if self.print_str:
            print("""       iddec : ID LSB exp RSB""")
        if self.enable_symbol_tree:
            if hasattr(p[3], 'type'):
                self.symbolTable.add_var_arr(p[1], p[3].get_value())
            else:
                self.symbolTable.add_var_arr(p[1], 1)
        if self.enable_code_generation:
            p[0] = NonTerminal()
            self.memory.insert_array_memory(p[1])

    def p_iddec_id3(self, p):
        """iddec : ID ASSIGN exp"""
        if self.print_str:
            print("""       iddec : ID ASSIGN exp""")
        if self.enable_symbol_tree:
            self.symbolTable.add_var(p[1])
        if self.enable_code_generation:
            # print("int " + p[1] + ";")
            p[0] = NonTerminal()
            p[0].code = p[3].code + os.linesep + p[1] + " = " + str(p[3].get_value()) + ';'  # get_value?
            p[0].value = p[3].get_value()  # ?
            # print(p[0].code)

            p[0].vars += p[3].vars + " " + p[1] + " "

    # 6
    def p_idlist_iddec(self, p):
        """idlist : iddec"""
        if self.print_str:
            print("""       idlist : iddec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[1].code

            p[0].vars += p[1].vars + " "

    def p_idlist_idlist(self, p):
        """idlist : idlist COMMA iddec"""
        if self.print_str:
            print("""       idlist : idlist COMMA iddec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[1].code + p[3].code

            p[0].vars += p[1].vars + " " + p[3].vars + " "

    # 7
    def p_vardec_idlist(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        if self.print_str:
            print("""       vardec : idlist COLON type SEMICOLON""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[1].code

            p[0].vars += p[1].vars + " "

    # 8 *
    def p_funcdec_fun1_1(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block"""
        if self.print_str:
            print("""       funcdec : FUNCTION ID LRB paramdecs RRB COLON type block""")
        if self.enable_symbol_tree:
            self.symbolTable.function_detect(p[2], p[7].type)
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_funcdec_fun1_2(self, p):
        """funcdec : FUNCTION ID LRB RRB COLON type block"""
        if self.print_str:
            print("""       funcdec : FUNCTION ID LRB RRB COLON type block""")
        if self.enable_symbol_tree:
            self.symbolTable.function_detect(p[2], p[6].type)
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_funcdec_fun2_1(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB block"""
        if self.print_str:
            print("""       funcdec : FUNCTION ID LRB paramdecs RRB block""")
        if self.enable_symbol_tree:
            self.symbolTable.function_detect(p[2], "void")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_funcdec_fun2_2(self, p):
        """funcdec : FUNCTION ID LRB RRB block"""
        if self.print_str:
            print("""       funcdec : FUNCTION ID LRB RRB block""")
        if self.enable_symbol_tree:
            self.symbolTable.function_detect(p[2], "void")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 9 *
    def p_paramdecs_paramdecslist(self, p):
        """paramdecs : paramdecslist"""
        if self.print_str:
            print("""       paramdecs : paramdecslist""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 10
    def p_paramdecslist_paramdec(self, p):
        """paramdecslist : paramdec"""
        if self.print_str:
            print("""       paramdecslist : paramdec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_paramdecslist_paramdecslist(self, p):
        """paramdecslist : paramdecslist COMMA paramdec"""
        if self.print_str:
            print("""       paramdecslist : paramdecslist COMMA paramdec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 11
    def p_paramdec_id1(self, p):
        """paramdec : ID COLON type"""
        if self.print_str:
            print("""       paramdec : ID COLON type""")
        if self.enable_symbol_tree:
            self.symbolTable.add_var(p[1])
        if self.enable_code_generation:
            p[0] = NonTerminal()
            # print("int " + p[1] + ";")

    def p_paramdec_id2(self, p):
        """paramdec : ID LSB RSB COLON type"""
        if self.print_str:
            print("""       paramdec : ID LSB RSB COLON type""")
        if self.enable_symbol_tree:
            self.symbolTable.add_var(p[1])
        if self.enable_code_generation:
            #     print("int " + p[1] + ";")
            p[0] = NonTerminal()
            self.memory.insert_array_memory(p[1])

    # 12 *
    def p_block_stmtlist(self, p):
        """block : LCB stmtlist RCB"""
        if self.print_str:
            print("""       block : LCB stmtlist RCB""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code2 = p[2].code2
            # print("")

            p[0].vars += p[2].vars + " "

    def p_block_null(self, p):
        """block : LCB RCB"""
        if self.print_str:
            print("""       block : LCB RCB""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 13 *
    def p_stmtlist_stmt(self, p):
        """stmtlist : stmt"""
        if self.print_str:
            print("""       stmtlist : stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code2 = p[1].code2
            # print("AS")

            p[0].vars += p[1].vars + " "

    def p_stmtlist_stmlist(self, p):
        """stmtlist : stmtlist stmt"""
        if self.print_str:
            print("""       stmtlist : stmtlist stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code2 += p[1].code2 + os.linesep + p[2].code2
            # print()
            # print("hey " + p[0].code)

            p[0].vars += p[1].vars + " " + p[2].vars + " "

    # 15 *
    def p_case_where_1(self, p):
        """case : WHERE const COLON stmtlist"""
        if self.print_str:
            print("""       case : WHERE const COLON stmtlist""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_case_where_2(self, p):
        """case : WHERE const COLON """
        if self.print_str:
            print("""       case : WHERE const COLON """)
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 16 *
    def p_cases_case(self, p):
        """cases : case"""
        if self.print_str:
            print("""       cases : case""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_cases_cases(self, p):
        """cases : cases case"""
        if self.print_str:
            print("""       cases : cases case""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 17 *
    def p_stmt_return(self, p):
        """stmt : RETURN exp SEMICOLON"""
        if self.print_str:
            print("""       stmt : RETURN exp SEMICOLON""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_exp(self, p):
        """stmt : exp SEMICOLON"""
        if self.print_str:
            print("""       stmt : exp SEMICOLON""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].ex_value = p[1].get_value()
            p[0].code = p[1].code
            p[0].code2 = p[1].code
            # print("     " + p[0].code)
            # print("sd")

            p[0].vars += p[1].vars + " "

    def p_stmt_block(self, p):
        """stmt : block"""
        if self.print_str:
            print("""       stmt : block""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[1].code2
            # print("SD")

            p[0].vars += p[1].vars + " "

    def p_stmt_vardec(self, p):
        """stmt : vardec"""
        if self.print_str:
            print("""       stmt : vardec""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code2 = p[1].code

            p[0].vars += p[1].vars + " "

    def p_stmt_while(self, p):
        """stmt : WHILE LRB exp RRB stmt"""
        if self.print_str:
            print("""       stmt : WHILE LRB exp RRB stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].next = self.new_label()
            p[0].begin = self.new_label()
            p[3].true = self.new_label()
            p[3].false = p[0].next
            p[5].next = p[0].begin
            p[0].code = p[0].begin + ":" + os.linesep
            p[0].code += "if(" + p[3].place + ") goto " + p[3].true + ";" + os.linesep
            p[0].code += "goto " + p[0].next + ";" + os.linesep
            p[0].code += p[3].true + ": " + os.linesep
            p[0].code += p[5].code + os.linesep
            p[0].code += "goto " + p[0].begin + ";" + os.linesep
            p[0].code += p[0].next + ":" + os.linesep

            p[0].code2 = p[0].code

            p[0].is_while = True
            p[0].while_lab = p[0].begin

            p[0].is_while2 = True
            p[0].while_lab2 = p[0].next

            p[0].vars += p[5].vars + " "

            # print(p[0].code)

    def p_stmt_on_1(self, p):
        """stmt : ON LRB exp RRB LCB cases RCB SEMICOLON"""
        if self.print_str:
            print("""       stmt : ON LRB exp RRB LCB cases RCB SEMICOLON""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_on_2(self, p):
        """stmt : ON LRB exp RRB LCB RCB SEMICOLON"""
        if self.print_str:
            print("""       stmt : ON LRB exp RRB LCB RCB SEMICOLON""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_for1(self, p):
        """stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"""
        if self.print_str:
            print("""       stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_for2(self, p):
        """stmt : FOR LRB ID IN ID RRB stmt"""
        if self.print_str:
            print("""       stmt : FOR LRB ID IN ID RRB stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_if1_1(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist"""
        if self.print_str:
            print("""       stmt : IF LRB exp RRB stmt elseiflist""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_if1_2(self, p):
        """stmt : IF LRB exp RRB stmt """
        if self.print_str:
            print("""       stmt : IF LRB exp RRB stmt """)
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].next = self.new_label()
            p[3].true = self.new_label()
            p[3].false = p[0].next
            p[5].next = p[0].next

            p[3].code = p[3].code.replace("Ltrue", p[3].true)
            p[3].code = p[3].code.replace("Lfalse", p[3].false)

            p[0].code = p[3].code + "\n" + p[3].true + ": " + p[5].code + "\n" + p[0].next + ": "
            # print(p[0].code)
            # p[0].code = "if(" + p[3].code + ") goto " + p[3].true + ";" + os.linesep
            # p[0].code += "goto " + p[3].false + ";" + os.linesep
            # p[0].code += p[3].true + ": " + os.linesep
            # p[0].code += p[5].code2 + os.linesep
            # p[0].code += p[3].false + ":" + os.linesep

            p[0].code2 = p[0].code

            p[0].vars += p[3].vars + " " + p[5].vars

            # print(p[0].code)

    def p_stmt_if2_1(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"""
        if self.print_str:
            print("""       stmt : IF LRB exp RRB stmt elseiflist ELSE stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_stmt_if2_2(self, p):
        """stmt : IF LRB exp RRB stmt ELSE stmt"""
        if self.print_str:
            print("""       stmt : IF LRB exp RRB stmt ELSE stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].next = self.new_label()
            # p[0].next = self.new_label()

            if p[5].is_while:
                p[3].true = p[5].while_lab
            else:
                p[3].true = self.new_label()
            # if p[5].is_while2:
            #     p[3].false = p[5].while_lab2
            # else:
            #     p[3].false = self.new_label()
            # p[3].true = self.new_label()
            p[3].false = self.new_label()

            p[5].next = p[0].next
            p[7].next = p[0].next
            p[3].code = p[3].code.replace("Ltrue", p[3].true)
            p[3].code = p[3].code.replace("Lfalse", p[3].false)

            # if p[5].is_while and p[5].is_while2:
            #     p[0].code = p[3].code + "\n" + p[5].code + "\n" \
            #                 + p[7].code
            # elif p[5].is_while:
            #     p[0].code = p[3].code + "\n" + p[5].code + "\n" \
            #                 + p[3].false + ": " + p[7].code
            #
            # elif p[5].is_while2:
            #     p[0].code = p[3].code + "\n" + p[3].true + ": " + p[5].code + "\n" \
            #                 + p[7].code
            #
            # else:
            #     p[0].code = p[3].code + "\n" + p[3].true + ": " + p[5].code + "\n" \
            #                 + p[3].false + ": " + p[7].code
            if p[5].is_while:
                p[0].code = p[3].code + "\n" + p[5].code + "\n" + "goto " \
                            + p[5].next + ";" + "\n" \
                            + p[3].false + ": " + p[7].code + "goto " + p[7].next + \
                            ";" + "\n" + p[0].next + ":"
            else:
                p[0].code = p[3].code + "\n" + p[3].true + ": " + p[5].code + "\n" + "goto " \
                            + p[5].next + ";" + "\n" \
                            + p[3].false + ": " + p[7].code + "goto " + p[7].next + \
                            ";" + "\n" + p[0].next

            # p[0].code = "if(" + p[3].code + ") goto " + p[3].true + ";" + os.linesep
            # p[0].code += "goto " + p[3].false + ";" + os.linesep
            # p[0].code += p[3].true + ": " + os.linesep
            # p[0].code += p[5].code2 + os.linesep
            # p[0].code += "goto " + p[0].next + ";" + os.linesep
            # p[0].code += p[3].false + ":" + os.linesep
            # p[0].code += p[7].code2 + os.linesep
            # p[0].code += p[0].next + ":"

            p[0].code2 = p[0].code

            p[0].vars += p[3].vars + " " + p[5].vars + " " + p[7].vars

            # print(p[0].code)

    def p_stmt_print(self, p):
        """stmt : PRINT LRB ID RRB SEMICOLON"""
        if self.print_str:
            print("""       stmt : PRINT LRB ID RRB SEMICOLON""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code2 = r'printf("%d", ' + p[3] + ");"
            # print(p[0].code)

    # 18 *
    def p_elseiflist_elseif(self, p):
        """elseiflist : ELSEIF LRB exp RRB stmt"""
        if self.print_str:
            print("""       elseiflist : ELSEIF LRB exp RRB stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_elseiflist_elseiflist(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt"""
        if self.print_str:
            print("""       elseiflist : elseiflist ELSEIF LRB exp RRB stmt""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 19
    def p_relopexp_1(self, p):
        """relopexp : exp GT exp"""
        if self.print_str:
            print("""       relopexp : exp GT exp""")
        if self.enable_code_generation:
            # self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse")
            label = None
            if (len(p[1].code + p[3].code) > 0):
                label = self.new_label()
            self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse", label)
            ##

            # p[0] = NonTerminal()
            # p[0].true = "Ltrue"
            # p[0].false = "Lfalse"
            # if(len(p[1].code + p[3].code) > 0):
            #     label = self.new_label()
            #     p[1].code = p[1].code.replace("Ltrue", label)
            #     p[0].code = p[1].code + p[3].code + "\n" + label + ": "

            # # print("p1", p[1].code)
            # # print("p3", p[3].code)
            # # print("yo", p[0].code)
            # p[0].code += "if(" + str(p[1].get_value()) + " " + p[2] + " "
            # p[0].code += str(p[3].get_value()) + ")" + " goto " + p[0].true + ";" + os.linesep
            # p[0].code += "goto " + p[0].false
            # p[0].place = p[3].get_value()

    def p_relopexp_2(self, p):
        """relopexp : exp LT exp"""
        if self.print_str:
            print("""       relopexp : exp LT exp""")
        if self.enable_code_generation:
            label = None
            if (len(p[1].code + p[3].code) > 0):
                label = self.new_label()
            self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse", label)

    def p_relopexp_3(self, p):
        """relopexp : exp NE exp"""
        if self.print_str:
            print("""       relopexp : exp NE exp""")
        if self.enable_code_generation:
            label = None
            if (len(p[1].code + p[3].code) > 0):
                label = self.new_label()
            self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse", label)

    def p_relopexp_4(self, p):
        """relopexp : exp EQ exp"""
        if self.print_str:
            print("""       relopexp : exp EQ exp""")
        if self.enable_code_generation:
            label = None
            if (len(p[1].code + p[3].code) > 0):
                label = self.new_label()
            self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse", label)

    def p_relopexp_5(self, p):
        """relopexp : exp GE exp"""
        if self.print_str:
            print("""       relopexp : exp GE exp""")
        if self.enable_code_generation:
            label = None
            if (len(p[1].code + p[3].code) > 0):
                label = self.new_label()
            self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse", label)

    def p_relopexp_6(self, p):
        """relopexp : exp LE exp"""
        if self.print_str:
            print("""       relopexp : exp LE exp""")
        if self.enable_code_generation:
            label = None
            if (len(p[1].code + p[3].code) > 0):
                label = self.new_label()
            self.codeGenerator.generate_relop_code(p, "Ltrue", "Lfalse", label)

    # 19.5
    def p_otherop_1(self, p):
        """otherop : exp AND exp"""
        if self.print_str:
            print("""       otherop : exp AND exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_otherop_2(self, p):
        """otherop : exp OR exp"""
        if self.print_str:
            print("""       otherop : exp OR exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_otherop_3(self, p):
        """otherop : exp SUM exp"""
        if self.print_str:
            print("""       otherop : exp SUM exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_otherop_4(self, p):
        """otherop : exp SUB exp"""
        if self.print_str:
            print("""       otherop : exp SUB exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_otherop_5(self, p):
        """otherop : exp MUL exp"""
        if self.print_str:
            print("""       otherop : exp MUL exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())
            # print("T")

    def p_otherop_6(self, p):
        """otherop : exp DIV exp"""
        if self.print_str:
            print("""       otherop : exp DIV exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_otherop_7(self, p):
        """otherop : exp MOD exp"""
        if self.print_str:
            print("""       otherop : exp MOD exp""")
        if self.enable_code_generation:
            self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_nlvalue1(self, p):
        """exp : ID ASSIGN exp"""
        if self.print_str:
            print("""       exp : ID ASSIGN exp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            # p[0].code = p[1] + " = " + str(p[3].get_value()) + ";"  # get_value?
            # p[0].code = p[1] + " = " + str(p[3].code) + ";"  # get_value?
            p[0].value = p[3].get_value()  # ?
            p[0].code = p[3].code + os.linesep + p[1] + " = " + str(p[3].get_value()) + ";"
            # print(p[3].code)
            # print("     " + p[0].code2)
            # print(p[0].value)
            # print("k")

            p[0].vars += p[3].vars + " "

    def p_exp_nlvalue2(self, p):
        """exp : ID LSB exp RSB ASSIGN exp"""
        if self.print_str:
            print("""       exp : ID LSB exp RSB ASSIGN exp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[6].code + os.linesep + "array" + p[2] + str(
                self.memory.get_array_memory(p[1], p[3].get_value()))
            p[0].code += p[4] + " = " + str(p[6].get_value()) + ';'
            p[0].place = "array" + p[2] + \
                         str(self.memory.get_array_memory(p[1], p[3].get_value())) + p[4]  # ?value?
            # print(p[0].code)

            p[0].vars += p[3].vars + " " + p[6].vars + " "

    def p_exp_exp1(self, p):
        """exp : relopexp"""
        if self.print_str:
            print("""       exp : relopexp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].code = p[1].code
            # me
            p[0] = p[1]

            p[0].vars += p[1].vars + " "

    def p_exp_relopexp(self, p):
        """exp : otherop"""
        if self.print_str:
            print("""       exp : otherop""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].place = p[1].place
            p[0].code = p[1].code
            # p[0].code2 = p[1].code

            p[0].vars += p[1].vars + " "

    def p_exp_const(self, p):
        """exp : const"""
        if self.print_str:
            print("""       exp : const""")
        if self.enable_code_generation or self.enable_symbol_tree:
            p[0] = NonTerminal()
            p[0].value = p[1].value

    def p_exp_nlvalue3(self, p):
        """exp : ID"""
        if self.print_str:
            print("""       exp : ID""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].place = p[1]

    def p_exp_nlvalue4(self, p):
        """exp : ID LSB exp RSB"""
        if self.print_str:
            print("""       exp : ID LSB exp RSB""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].place = "array" + p[2] + str(self.memory.get_array_memory(p[1], p[3].get_value())) \
                         + p[4] + ';'  # ?
            # print(p[0].code)

    def p_exp_id1(self, p):
        """exp : ID LRB explist RRB"""
        if self.print_str:
            print("""       exp : ID LRB explist RRB""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_exp_exp2(self, p):
        """exp : LRB exp RRB"""
        if self.print_str:
            print("""       exp : LRB exp RRB""")
        if self.enable_code_generation:
            p[0] = NonTerminal()  # maybe error
            p[0].code = p[2].code
            p[0] = p[2]
            # p[0] = NonTerminal()
            # p[0].place = p[2].place
            # p[0].code = p[2].code

            p[0].vars += p[2].vars + " "

    def p_exp_id2(self, p):
        """exp : ID LRB RRB"""
        if self.print_str:
            print("""       exp : ID LRB RRB""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_exp_exp3(self, p):
        """exp : SUB exp"""
        if self.print_str:
            print("""       exp : SUB exp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()
            p[0].value = "- " + str(p[2].get_value())  # ?

    def p_exp_exp4(self, p):
        """exp : NOT exp"""
        if self.print_str:
            print("""       exp : NOT exp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 22
    def p_const_intnumber(self, p):
        """const : INTEGERNUMBER"""
        if self.print_str:
            print("""       const : INTEGERNUMBER""")
        if self.enable_code_generation or self.enable_symbol_tree:
            p[0] = NonTerminal()
            p[0].value = p[1]

    def p_const_floatnumber(self, p):
        """const : FLOATNUMBER"""
        if self.print_str:
            print("""       const : FLOATNUMBER""")
        if self.enable_code_generation or self.enable_symbol_tree:
            p[0] = NonTerminal()
            p[0].value = int(p[1])

    def p_const_True(self, p):
        """const : TRUE"""
        if self.enable_code_generation or self.enable_symbol_tree:
            print("""       const : TRUE""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_const_False(self, p):
        """const : FALSE"""
        if self.enable_code_generation or self.enable_symbol_tree:
            print("""       const : FALSE""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    # 24
    def p_explist_exp(self, p):
        """explist : exp"""
        if self.print_str:
            print("""       explist : exp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    def p_explist_explist(self, p):
        """explist : explist COMMA exp"""
        if self.print_str:
            print("""       explist : explist COMMA exp""")
        if self.enable_code_generation:
            p[0] = NonTerminal()

    precedence = (
        ('right', 'ASSIGN'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'LT', 'GE', 'LE'),
        ('left', 'SUB', 'SUM'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('left', 'NOT'),
        ('left', 'LRB', 'RRB', 'LCB', 'RCB', 'LSB', 'RSB'),
        ('left', 'IF'),
        ('left', 'ELSE', 'ELSEIF')
    )

    def new_label(self):
        temp = "L" + str(self.tempCount2)
        self.tempCount2 += 1
        return temp

    def new_temp(self):
        temp = "T" + str(self.tempCount)
        self.tempCount += 1
        return temp

    def p_error(self, p):
        print("err ", p.value)
        raise Exception('Error !!!', p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
