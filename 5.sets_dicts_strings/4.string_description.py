while True:
    string = input('Enter string to get info about it. Hit Enter button to exit.\n')
    if string:
        if string[0].isupper():
            print('The string begins with capital letter.')
        else:
            print('The string begins with lowercase letter.')
        print(f'The string is {len(string)} characters long.')
        if string[-2:-1] == '!!':
            print('The string is exclamation.')
        print(f'The string "fire" is {string.count("fire")} times in string.')
        print(string.upper())
        print(string.lower())
        print(string.title())
    else:
        print('Goodbye!')
        break
