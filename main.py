def loger_errors(func):
    """Декоратор, який виправляє помилки"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Такої команди немає. Введіть help для довідки. Ви ввели {}".format(args))
        except NameError:
            print("Такого імені немає в контактах. Введіть ім'я правильно. Ви ввели {}".format(args))
        except ValueError:
            print("Введіть значення номеру телефону правильно. Ви ввели {}".format(args))
        except IndexError:
            print("Введіть необхідну кількість модифікаторів команд. Ви ввели {}".format(args))

    return inner
 

# add name number ПРАЦЮЄ
@loger_errors
def add_phone(name_number):
    """Зберігає новий контакт в словник контактів."""
    if name_number[1].isdigit():
        contacts.update({name_number[0]: name_number[1]})
    else:
        raise ValueError
    return contacts
    
    
# change name number ПРАЦЮЄ
@loger_errors
def change_phone(name_number):
    """Зберігає новий номер існуючого контакту в словнику."""
    if name_number[0] in contacts:
        if name_number[1].isdigit():
            contacts[name_number[0]] = name_number[1]
        else:
            raise ValueError
    else:
        raise NameError
    return contacts


# "goodbye", "close", "exit" ПРАЦЮЄЄЄЄЄ
@loger_errors
def close(user_input):
    """Прощається з користувачем й закриває програму.""" 
    global flag
    flag = False
    # return flag


@loger_errors
def get_handler(user_command):
    """Знаходить команду користувача в словнику."""
    return COMMANDS[user_command]


# phone name ПРАЦЮЄ
@loger_errors
def get_phone(name):
    """Бере й виводить номер телефону за іменем зі словника контактів."""
    return contacts[name[0]]


# hello ПРАЦЮЄ
@loger_errors
def hello(user_input): 
    return f"Hello, how can I help you? Available commands: \n add name phone \t # Додати новий контакт \n change name phone \t # Змінити номер існуючого контакту \n phone name \t\t # Показати номер контакту \n show_all \t\t # Показати список контактів \n close \t\t\t # Вихід"



@loger_errors
def parser(user_input):
    """Розбирає інпут користувача"""
    user_input_list = user_input.lower().split(" ")
    user_command = user_input_list[0]
    return user_command, user_input_list[1:]


# show_all ПРАЦЮЄ, але як викликати команду двома словами?
@loger_errors
def show_all(user_input):
    """Виводить всі додані контакти в словнику."""
    for key, value in contacts.items():
        print(f"{key.title()}: {value}")


def main():
    """Бере інпут, потім обирає яка це команда, перетворює інпут в потрібні елементи списку [name, phone...] 
    перепитує параметри якщо були введені неправильно, виводить результат, продовжує чекати нову команду"""
    while flag == True:
        user_input = input("Please, input command: ")
        command, other_commands = parser(user_input)
        handler = get_handler(command)    
        try:
            result = handler(other_commands)
            if bool(result) == True:
                print(result)
        except TypeError:
            pass
        
    if flag == False:
        print("Good bye!")

  

COMMANDS = {
    'hello': hello,
    'help': hello,
    'add': add_phone,
    'change': change_phone,
    'phone': get_phone,
    'show_all': show_all,
    'goodbye': close,
    'close': close,
    'exit': close
}

contacts = {}
flag = True

if __name__ == '__main__':
    main()
