# add name number ПРАЦЮЄ
def add_phone(name_number):
    """Зберігає новий контакт в словник контактів."""
    contacts.update({name_number[0]: name_number[1]})
    return contacts
    
    
# change name number ПРАЦЮЄ
def change_phone(name_number):
    """Зберігає новий номер існуючого контакту в словнику."""
    contacts[name_number[0]] = name_number[1]
    return contacts


# "goodbye", "close", "exit" ПРАЦЮЄЄЄЄЄ
def close(user_input):
    """Прощається з користувачем й закриває програму.""" 
    global flag
    flag = False
    return flag


def get_handler(user_command):
    """Знаходить команду користувача в словнику."""
    return COMMANDS[user_command]


# phone name ПРАЦЮЄ, але що з прінтом?
def get_phone(name):
    """Бере й виводить номер телефону за іменем зі словника контактів."""
    print (contacts[name[0]])
    return contacts[name[0]]


# hello ПРАЦЮЄ, але що з прінтом?
def hello(user_input): 
    print("Hello, how can I help you? Available commands: \n add name phone \n change name phone \n phone name \n show_all \n close")


def parser(user_input):
    """Розбирає інпут користувача"""
    user_input_list = user_input.lower().split(" ")
    user_command = user_input_list[0]
    return user_command, user_input_list[1:]


# show_all ПРАЦЮЄ, але як викликати команду двома словами?
def show_all(user_input):
    """Виводить всі додані контакти в словнику."""
    for key, value in contacts.items():
        print(f"{key.title()}: {value}")




# Ну і як виправляти помилки? KeyError, ValueError, IndexError
def input_error():
    """Декоратор який виправляє помилки"""


def main():
    """Бере інпут, потім обирає яка це команда, перетворює інпут в потрібні елементи списку [name, phone...] 
    перепитує параметри якщо були введені неправильно, виводить результат, продовжує чекати нову команду"""
    while flag == True:
        user_input = input('Please, input command: ')
        command, other_commands = parser(user_input)
        handler = get_handler(command)
        
        # Обробник помилок є, але як його засунути в декоратор?
        try:
            # @input_error можливо якось так?
            handler(other_commands)
        except KeyError:
            print("Введіть ім'я правильно")
        except ValueError:
            print("Введіть значення правильно")
        except IndexError:
            print("Введіть необхідні модифікатори команди правильно")
    if flag == False:
        print("Good bye!")
  

COMMANDS = {
    'hello': hello,
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


    # 1. Як обробляти помилки іннером? обробник помилок поки що є в мейні.
    # 2. Як зробити всі прінти в мейні? (hello, phone, show_all, close)
    # 3. А що якщо команда складається з двох слів? good bye, show all? чи пофіг і достатньо goodbye show_all як зараз?
    # 4. Чи треба перевіряти що в номері телефону містяться тільки цифри? в ідеалі звісно було б непогано.