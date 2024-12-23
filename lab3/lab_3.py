import os


dir = os.path.dirname(__file__) + "/"


def read_file(mode='all'):
    try:
        
        with open(dir + 'example.txt', 'r') as file:
            if mode == 'all':
                content = file.read()
                print(content)
            elif mode == 'line':
                for line in file:
                    print(line, end='') 
                print()
            else:
                print("Укажите корректный режим чтения: 'all' или 'line'.")
    except FileNotFoundError:
        print("Файл example.txt не найден. Проверьте, существует ли файл.")


def write_to_file():
    user_input = input("Введите текст для записи в файл: ")
    try:
        with open(dir + 'user_input.txt', 'w') as file:
            file.write(user_input + '\n')
        print("Текст успешно записан в файл user_input.txt.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


#read_file("line")
read_file()
write_to_file()