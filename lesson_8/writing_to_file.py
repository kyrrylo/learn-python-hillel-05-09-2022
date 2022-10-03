def fp_status_check(file_pointer):
    print(file_pointer)
    print(type(file_pointer))
    print(f'{file_pointer.readable()=}')  # readable - читабельный, можно ли читать
    print(f'{file_pointer.writable()=}')  # writable - можно ли записывать

# mode = r (read)
# mode = w (write)
# mode = a (append)
# mode r+/w+/a+ (read and write) непрактично, но ошибку не выдаст при +
filename = 'file_to_write.extension-does-not-matter'


with open(filename, mode='w') as fp:
    fp_status_check(fp)

    # fp.read()  # выдаёт ошибку, потому как файл для чтения
    fp.write('I cleared everything and wrote into this file\n')
    # fp.writelines(['I write another line into file\n', 'And one more\n', 'This one too\n'])

with open(filename, mode='r') as read_fp:
    fp_status_check(read_fp)
    print(read_fp.read())

with open(filename, mode='a') as fp:
    fp_status_check(fp)

    # print(fp.read())  # выдаёт ошибку, потому как файл для чтения

    fp.write('I append into this file\n')
    fp.writelines(['I append another line into file\n', 'And one more\n', 'This one too\n'])