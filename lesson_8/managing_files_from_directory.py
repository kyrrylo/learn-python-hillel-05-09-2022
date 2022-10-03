import os

# operation system

directory_to_manage = 'directory_with_files'


for filename in os.listdir(directory_to_manage):
    full_filename = os.path.join(directory_to_manage, filename)  # path - путь к файлам, join - соединить вместе
    print(full_filename)
    with open(full_filename) as fp:
        print(f'Opened file {full_filename}')
        print(f'It\'s contents: {fp.read()}')
