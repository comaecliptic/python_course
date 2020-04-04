import re


# Yeah, I've seen full version of regexp for 99,99% of accuracy and it made me cry.
email_pattern = re.compile(r"""([\w!#$%&'*+/=?^_`{|}~-]+    # local part before the first dot
                           (\.[\w!#$%&'*+/=?^_`{|}~-]+)*)   # (dot and any number of symbols after) any number of times
                           @([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+              # subdomains and dots separating them
                           [A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?""", flags=re.ASCII | re.VERBOSE)

email_list = [
    'shamil.utaraptor@gmail.com',
    'tetpapx@bk.ru',
    'wrong....email@gmail.com',
    '.slightlywrong@mail.ru',
    'very-wrong',
    'special#characters$every^where@domain-name.for.life.com',
    'justmail@56738-377834.complicated.domain.ru',
    'justmail@fucked_up.domain',
    "that's.all-folks!@good.bye",
]

print('Email address examples:')
for email in email_list:
    if re.match(email_pattern, email):
        print(f'{email}: correct')
    else:
        print(f'{email}: INCORRECT')

while True:
    user_email = input('Enter your email to check if it is correct: ')
    if re.match(email_pattern, user_email):
        print('Correct!')
    else:
        print('Wrong! Do it again!')
