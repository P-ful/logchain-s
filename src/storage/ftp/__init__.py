class FtpDisk:
    def write(file_name, message):

        f = open(file_name, 'a')
        f.write(message)
        f.write('\n')
        f.close()


    def read_all_line(file_name):

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