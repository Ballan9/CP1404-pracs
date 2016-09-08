
def main():
    valid_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                       'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                       'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    get_username = input("Please enter your username")
    if get_username in valid_usernames:
        print("You have entered a valid username")
    else:
        print( " you have entered an invalid username")


main()
