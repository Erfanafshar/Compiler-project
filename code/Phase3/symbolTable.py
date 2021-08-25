from tabulate import tabulate


class SymbolTable:

    def __init__(self):
        self.list = []
        self.tempVar = []
        self.address = 0
        self.local_address = 0

    def add_var(self, name):
        self.tempVar.append([name, "Var", "Int", 4, self.address, "None"])
        self.address += 4
        self.local_address += 4

    def add_var_arr(self, name, size):
        arr_size = 4 * size
        self.tempVar.append([name, "Array", "Int", arr_size, self.address, "None"])
        self.address += arr_size
        self.local_address += arr_size

    def insert_to_list(self, outer_name, base_address):
        outer_info = [outer_name, base_address]
        for itm in range(len(self.tempVar)):
            self.list.append(outer_info + self.tempVar[itm])
        # self.list.append(outer_info + self.tempVar)
        self.tempVar.clear()

    def declaration_detect(self):
        self.local_address = 0
        self.insert_to_list("program", 0)

    def function_detect(self, func_name, return_type):
        base_address = self.address - self.local_address
        self.local_address = 0
        func_size = self.get_func_size()
        self.list.append(["program", 0, func_name, "Function", "None", func_size,
                          base_address, return_type])
        self.insert_to_list(func_name, base_address)

    def get_func_size(self):
        sum = 0
        for item in self.tempVar:
            sum += item[3]
        return sum

    def print_table(self):
        vars_list = []
        func_list = []
        table_name = ""
        for i in range(len(self.list)):
            if self.list[i][3] == "Function":
                func_list.append(self.list[i])
            if i == 0:
                table_name = self.list[i][0]
                vars_list.append(self.list[i][2:])
            else:
                if table_name != self.list[i][0]:
                    self.printer(table_name, vars_list)
                    table_name = self.list[i][0]
                    vars_list.clear()
                    vars_list.append(self.list[i][2:])
                else:
                    vars_list.append(self.list[i][2:])

        if len(vars_list) != 0:
            self.printer(table_name, vars_list)

        func = []
        for i in range(len(func_list)):
            func.append([func_list[i][2], func_list[i][6], func_list[i][5], func_list[i][1]])
        if len(func) != 0:
            self.printer2("Scopes", func)

    def printer(self, table_name, vars_list):
        print()
        print()
        print(table_name + " : ")
        print()
        print(tabulate(vars_list,
                       headers=['Name', 'Entity Type', 'Var Type', 'Size', 'Address', 'Return Type'],
                       tablefmt='orgtbl'))

    def printer2(self, table_name, func_list):
        print()
        print()
        print(table_name + " : ")
        print()
        print(tabulate(func_list,
                       headers=['Name', 'Address', 'Size', 'Outer Scope Address'],
                       tablefmt='orgtbl'))
