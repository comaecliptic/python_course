n = None
while True:
    print("Enter a number to find out if it is fizz, buzz, both or none. Type 'exit' to escape.")
    n = input()
    try:
        n = int(n)
        if (n % 3 == 0) and (n % 5 == 0):
            print('fizzbuzz')
        elif n % 3 == 0:
            print('fizz')
        elif n % 5 == 0:
            print('buzz')
        else:
            print(n)
    except ValueError:
        if n == 'exit':
            print('Exiting...')
            break
        else:
            print('Something is wrong!')