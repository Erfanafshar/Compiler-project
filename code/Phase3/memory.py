class Memory:
    memory_size = 1000 * 1000
    array_base_memory = 0 * 100 * 1000

    array_memory_list = []
    array_max_length = 1000

    def insert_array_memory(self, array_name):
        self.array_memory_list.append(array_name)

    def get_array_memory(self, array_name, array_index):
        return self.array_memory_list.index(array_name) * self.array_max_length \
               + self.array_base_memory + array_index
