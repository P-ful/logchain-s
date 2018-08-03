import os
import socket
import json
import shutil
import netifaces
import logging
from monitoring import monitoring
from settings import Settings
from storage.local import LocalDisk
from storage.ftp import FtpDisk

# database_path = os.path.dirname(
#     os.path.dirname(__file__)) + '\_DataStorage' + '\\'

database_path = Settings.get_instance().get_root_path() + '/_DataStorage/'

# block_storage_path = os.path.dirname(
#     os.path.dirname(__file__)) + '\_BlockStorage' + '\\'


block_storage_path = Settings.get_instance().get_root_path() + '/_BlockStorage/'

# voting_storage_path = os.path.dirname(
#     os.path.dirname(__file__)) + '\_VotingStorage' + '\\'
voting_storage_path = Settings.get_instance().get_root_path() + '/_VotingStorage/'

voting_info_file = 'Voting.txt'
node_info_file = 'NodeInfo.txt'
ledger_file = 'Transactions.txt'
block_file = "Block.txt"

'File write and read function'


def create_storage_driver(type):
    if (type == "local"):
        return LocalDisk()
    else:
        return FtpDisk()


def append(file_name, message):
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    driver.append(file_name, message)


def appendln(file_name, message):
    append(file_name, message + "\n")


def read_all_line(file_name):
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    return driver.read_all_line(file_name)


'Add transaction, block, voting, node info'


def add_transaction(trx):
    append(database_path + ledger_file, trx)


def add_block(block):
    append(block_storage_path + block_file, block)


def add_voting(trx):
    append(voting_storage_path + voting_info_file, trx)


def add_node_info(node_info):
    append(database_path + node_info_file, node_info)


def get_my_ip():
    ip = socket.gethostbyname(socket.gethostname())
    monitoring.log("log.IP address:" + ip)
    return ip


def get_my_ip_rpi():
    interface_name = Settings.get_instance().get_network_interface_name()
    netifaces.ifaddresses(interface_name)
    ip = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['addr']
    monitoring.log("log.IP address:" + ip)
    return ip


def get_ip_list():
    f = open(database_path + node_info_file, 'r')
    ip_list = []
    while True:
        line = f.readline()
        line = line[:-1]
        if not line:
            break
        if line == "":
            break
        ip_list.append(line)

    return ip_list


def get_transaction_list():
    return read_all_line(database_path + ledger_file)


def get_voting_list():
    return read_all_line(voting_storage_path + voting_info_file)


def get_blockconfirm_list():
    return read_all_line(block_confirm_path + block_confirm_file)


def get_number_of_transactions():
    return len(get_transaction_list())


def get_my_block():
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    return driver.read(block_storage_path + 'a_my_block')


def get_last_file():
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    return driver.listfiles(block_storage_path)[-1]


def get_last_block():
    driver = create_storage_driver(Settings.get_instance().get_storage_type())

    block_list = driver.list_files(block_storage_path)
    block_list_size = len(block_list)

    j = 0
    for i in block_list:
        block_list[j] = int(i)
        j = j + 1

    # last_block_file_name = block_list[-1]
    last_block_file_name = str(block_list_size)

    monitoring.log("log.last_block_file_name is .. " + last_block_file_name)

    # monitoring.log("log."+last_block_file_name+type(last_block_file_name))

    last_block_tx_list = read_all_line(
        str(block_storage_path) + last_block_file_name)
    last_block = "\n".join(last_block_tx_list)
    a = json.loads(last_block)

    return a['block_header']['block_number'], a['block_header']['block_hash']


def get_block_height():
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    return len(driver.list_files(block_storage_path))


def remove_all_transactions():
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    driver.write(database_path + ledger_file, "")
    monitoring.log('log.All transactions were removed.')


def remove_all_voting():
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    driver.write(voting_storage_path + voting_info_file, "")
    monitoring.log('log.The consensus related data has been deleted.')


def remove_all_blocks():
    try:
        driver = create_storage_driver(Settings.get_instance().get_storage_type())
        driver.rmdir(block_storage_path)
        driver.mkdir(block_storage_path)
        monitoring.log('log.All blocks were removed.')
    except Exception as e:
        print(e)


def create_new_block(file_name, block_json):
    driver = create_storage_driver(Settings.get_instance().get_storage_type())
    driver.write(block_storage_path + file_name, block_json)


def save_my_block(block_json):
    create_new_block('a_my_block', block_json)
