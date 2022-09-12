def read_a_b():
    user_a = float(input('Input first number a='))
    user_b = float(input('Input second number b='))
    return user_a, user_b


while True: # пока Правда, выполняется
    print("""
1. +
2. -
3. *
4. /
5. Exit
6. Say Hello
    """)
    user_input = input('Choose your math operation: ')

    if user_input == '1' or user_input == '+':
        user_a, user_b = read_a_b()
        print(f'{user_a} + {user_b} = {user_a + user_b}')
    elif user_input == '2' or user_input == '-':
        user_a, user_b = read_a_b()
        print(f'{user_a} - {user_b} = {user_a - user_b}')
    elif user_input == '3' or user_input == '*':
        user_a, user_b = read_a_b()
        print(f'{user_a} * {user_b} = {user_a * user_b}')
    elif user_input == '4' or user_input == '/':
        user_a, user_b = read_a_b()
        print(f'{user_a} / {user_b} = {user_a / user_b}')
    elif user_input == '5' or user_input.lower() == 'exit':
        break  # досрочный выход из цикла
    elif user_input == '6':
        print('Hello World!')
    else:
        print('Received value is not recognized. Please input 1-4 or +, -, * or /')
