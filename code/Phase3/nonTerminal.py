class NonTerminal:

    def __init__(self):
        self.value = ""
        self.code = ""
        self.place = ""
        self.type = ""
        self.true = ""
        self.false = ""
        self.next = ""
        self.begin = ""
        self.ex_value = ""
        self.code2 = ""
        self.code_pr = ""
        self.is_while = ""
        self.while_lab = ""
        self.is_while2 = ""
        self.while_lab2 = ""
        self.vars = ""

    def get_value(self):
        if self.value == "":
            return self.place
        return self.value
