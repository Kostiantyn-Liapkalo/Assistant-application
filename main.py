
# Phone book in the form of a dictionary.
phone_book = {}

# Standard phone number decorator.
def format_phone_number(func):
    
    def wrapper(num):
        
        new_num = func(num)
        if len(new_num) == 12:
            return f" + {new_num}"
        else:
            return f" + 3 8 {new_num}"
    return wrapper

# Checking with syntax sugar whether the number consists only of numbers.
@format_phone_number
def sanitize_phone_number(phone):
    
    new_phone = (phone.strip().removeprefix("+").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))
    new_phone = [str(int(i)) for i in new_phone]
    new_phone = "".join(new_phone)
    return new_phone


# Exclusion.
def input_error(func):

    def wrapper(*args, **kwargs):
        
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Phone's number is not correct!"
        except IndexError:
            return "Give me name and phone please"
    return wrapper


@input_error
def say_hello(lst):
    return "How can I help you?"


@input_error
def say_goodbye(lst):
    return "Good bye!"


# The function records or changes the number in the phone book, and if there are two words firstname lastname,
# then we combine them into one line. Recording will take place only if the number consists only of numbers
# and is of sufficient length.
@input_error
def set_number(lst):

    phone = str(lst[-1])
    name = " ".join(lst[:-1])
    phone = sanitize_phone_number(phone)

    if phone:
        phone_book[name.title()] = phone
        return f"Contact {name.title()} was created/updated"
    else:
        return ""


# The function displays the phone number of the subscriber whose name was in the command 'phone ...'
@input_error
def show_phone(lst):
    
    name = " ".join(lst)
    return phone_book[name.title()]


def help(lst):
    rules = """List of commands:
    1) if you want to add new contact, please write command: add {name} {phone number}
    2) if you want to change contact, please write command: change {name} {phone number}
    3) if you want to see the phone of contact, please write command: phone {name}
    4) if you want to see all contacts, please write command: show all
    5) if you want to say goodbye, please write one of these commands: good bye / close / exit
    6) if you want to say hello, please write command: hello
    """
    return rules


# The function displays all entries in the phone book with the 'show all' command.
@input_error
def show_all(lst):
    
    if len(phone_book) == 0:
        return "Phone book is empty"
    text = ""
    for name, phone in phone_book.items():
        text += f"{name} {phone}\n"
    return text.strip()

# Keys are keywords in commands.
# Values are functions that are called by these commands.
commands = {
    ("add", "change"): set_number,
    "phone": show_phone,
    "show all": show_all,
    "hello": say_hello,
    ("good bye", "close", "exit"): say_goodbye,
    "help": help
}



@input_error
def main():

    while True:
        command = input("Enter command: ")
        if command in (".", ):
            break
        command = command.lower().split()
        for key in commands:
            if command[0] in key:
                print(commands[key](command[1:]))


if __name__ == "__main__":
    main()
