import os

class LocalDisk:
    def append(self, file_name, message):
        f = open(file_name, 'a')
        f.write(message)
        f.close()

    def write(self, file_name, message):
        f = open(file_name, 'w')
        f.write(message)
        f.close()

    def read(self, file_name):
        f = open(block_storage_path + 'a_my_block', 'r')
        block = f.read()
        f.close()
        return block

    def read_all_line(self, file_name):
        f = open(file_name, 'r')
        line_list = []
        while True:
            line = f.readline()
            if not line:
                break
            else:
                line_list.append(line)
        f.close()
        return line_list