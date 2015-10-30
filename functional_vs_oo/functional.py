#! /usr/bin/env python
import sys
import os


def email_help():
    """
    Simple helper to explain how to use the script.
    """
    print('{}'.format('*' * 62))
    print('* Provide an email address to send a generic email to.{}*'.format(' ' * 7))
    print('* Example: python functional.py someone@somehwere.com{}*'.format(' ' * 16))
    print('* Yields: Expect a message detailing the email that was sent *')
    print('{}'.format('*' * 62))
    sys.exit()


database = {
    '1': {
        'name': 'Jim Brown',
        'email_address': 'jim@brown.com',
    },
    '2': {
        'name': 'Walter Payton',
        'email_address': 'walter@payton.com',
    },
    '3': {
        'name': 'Barry Sanders',
        'email_address': 'barry@sanders.com',
    },
    '4': {
        'name': 'LaDainian Tomlinson',
        'email_address': 'ladainian@tomlinson.com',
    },
}

BODY = "Hello {name}. We hope you are doing well and would like to invite you to check out " \
       "our awesome Python code.\n\n{url}\n\nIf you are not {name} or believed you received " \
       "this message in error you can simply disregard it."
URL = 'https://github.com/ricomoss/coding-campus-november-2015'
SUBJECT = 'Check Out Our Python Code'
FROM_ADDRESS = 'me@my_domain.com'


def _send_mail(to_address, message, from_address=None, subject=None):
    output = 'The following email was sent:\n\nTo: {}\nFrom: {}\nSubject: {}\n' \
             'Message:\n"""\n{}\n"""'
    if not from_address:
        from_address = FROM_ADDRESS

    if not subject:
        subject = SUBJECT

    print(output.format(to_address, from_address, subject, message))


def send_mail(to_address):
    recipient_name = lambda x: [v['name'] for v in database.values() if v['email_address'] == x][0]
    message = BODY.format(name=recipient_name(to_address), url=URL)
    _send_mail(to_address, message)


if __name__ == '__main__':
    # Clear the console to make the results more readable.
    os.system(['clear', 'cls'][os.name == 'nt'])

    # Simple approach to ensure the correct parameters are passed.
    if len(sys.argv) != 2:
        email_help()

    # Validating an email address is exceptionally complicated so we'll trust the user.
    email_address = sys.argv[1]
    try:
        send_mail(email_address)
    except KeyError:
        error_msg = 'The database does not contain an entry for "{}".  Please try again.'
        print(error_msg.format(email_address))
