import hashlib
import os


def about_your_PC():
    mypc = 'hostname'
    myos = 'uname -a'
    print('Hostname of your computer:')
    print(os.system(mypc))
    print('OS:')
    print(os.system(myos))


def hashing_data_in_a_file(file):
    if os.path.exists(file):
        main_file = open(file, 'r')
        finish_file = open('hash.txt', 'w')
        hash = hashlib.sha256()
        for line in main_file:
            line = bytes(line, 'utf-8')
            hash.update(line)
            finish_file.write(hash.hexdigest() + '\n')
            hash = hashlib.sha256()
        main_file.close()
        finish_file.close()
    else:
        print('-' * 50)
        print('ERROR: No such file exists.')


def copy_group_files_to_a_new_directory(group, dir):
    directory = os.getcwd()
    count = 0
    mk = f'mkdir {dir}'
    os.system(mk)
    for file in os.listdir(directory):
        if group in file:
            count += 1
            add_file = 'cp ' + (os.path.join(directory, file)) + ' ' + dir
            os.system(add_file)
    if count == 0:
        md = f'rmdir {dir}'
        os.system(md)
        print('-' * 50)
        print('ERROR: No such file exists.')


print('Welcome to Multifunctional Assistant for the work of the System Administrator.')
func_num = 100

while func_num > 0:
    print('-' * 50)
    print(
        "Functions: \n1. About your PC\n2. Hashing data in a file\n3. Copying a group of files to a new directory\n0. Exit")
    func_num = int(input('Please, choose the number of the special function: '))

    if func_num == 1:
        print('-' * 50)
        print('About your PC')
        about_your_PC()
    elif func_num == 2:
        print('-' * 50)
        print('Hashing data in a file.\nPlease, write argument.')
        name_file = input('The name of the file in which to hash the data: ')
        hashing_data_in_a_file(name_file)
    elif func_num == 3:
        print('-' * 50)
        print('Copying a group of files to a new directory.\nPlease, write argument.')
        group_name = input('The name of the group of files to be copied: ')
        directory_name = input('The name of the directory where the files will be copied to: ')
        copy_group_files_to_a_new_directory(group_name, directory_name)
    elif func_num == 0:
        print('-' * 50)
        print('Exit\nIt was nice to work with you. See you soon.')
        exit()
