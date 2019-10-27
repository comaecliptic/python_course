while True:
    string = input('Enter string to get info about its first symbol. Hit Enter button to exit.\n')
    if string:
        if string[0].isdecimal():
            print('First symbol is digit.')
        elif string[0].isalpha():
            print('First symbol is alphabetic.')
        elif string[0] == ' ':
            print('First symbol is space.')
        else:
            print('First symbol can not be classified.')
    else:
        print('Goodbye!')
        break
