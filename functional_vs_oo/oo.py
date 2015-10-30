#! /usr/bin/env python
import sys
import os


def email_help():
    """
    Simple helper to explain how to use the script.
    """
    print('{}'.format('*' * 62))
    print('* Provide an email address to send a generic email to.{}*'.format(' ' * 7))
    print('* Example: python oo.py someone@somehwere.com{}*'.format(' ' * 16))
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


class EmailHandler:
    BODY = "Hello {name}. We hope you are doing well and would like to invite you to check out " \
           "our awesome Python code.\n\n{url}\n\nIf you are not {name} or believed you received " \
           "this message in error you can simply disregard it."
    URL = 'https://github.com/ricomoss/coding-campus-november-2015'
    SUBJECT = 'Check Out Our Python Code'
    FROM_ADDRESS = 'me@my_domain.com'

    def _send_mail(self, to_address, message, from_address=None, subject=None):
        output = 'The following email was sent:\n\nTo: {}\nFrom: {}\nSubject: {}\n' \
                 'Message:\n"""\n{}\n"""'
        if not from_address:
            from_address = self.FROM_ADDRESS

        if not subject:
            subject = self.SUBJECT

        print(output.format(to_address, from_address, subject, message))

    @staticmethod
    def _get_name(to_address):
        for v in database.values():
            if v['email_address'] == to_address:
                return v['name']

        # If the database doesn't have a user we'll raise a KeyError
        raise KeyError

    def send_mail(self, to_address):
        recipient_name = self._get_name(to_address)
        message = self.BODY.format(name=recipient_name, url=self.URL)
        self._send_mail(to_address, message)


if __name__ == '__main__':
    # Clear the console to make the results more readable.
    os.system(['clear', 'cls'][os.name == 'nt'])

    # Simple approach to ensure the correct parameters are passed.
    if len(sys.argv) != 2:
        email_help()

    # Validating an email address is exceptionally complicated so we'll trust the user.
    email_address = sys.argv[1]
    email_handler = EmailHandler()
    try:
        email_handler.send_mail(email_address)
    except KeyError:
        error_msg = 'The database does not contain an entry for "{}".  Please try again.'
        print(error_msg.format(email_address))
