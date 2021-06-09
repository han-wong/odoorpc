import odoorpc
from pprint import pprint as pp
from urllib.error import URLError


def set_credential():
    val = ''
    while True:
        val = input('''
        Set configuration
        1. New
        2. Load
        3. Delete 
        4. Abort
        ''')
        if val == '1':
            return create_credential()
        elif val == '2':
            return load_credential()
        elif val == '3':
            delete_configuration()
        elif val == '4':
            return ''
        else:
            print('Invalid option!')


def login_to_host():
    try:
        odoo = odoorpc.ODOO(input('Hostname: '), timeout=5)
    except URLError as u:
        pp(u.errno)
    return odoo


def create_credential():
    odoo = login_to_host()
    pp(odoo.db.list())

    db = input('db_name: ')
    login = input('login: ')
    password = input('password: ')

    try:
        odoo.login(db,
                   login if login else 'admin',
                   password if password else 'admin')
    except odoorpc.error.RPCError as exc:
        pp(exc.info)
    else:
        if input('\nDo you want to save configuration? [y/N] > ').lower() == 'y':
            odoo.save(input('Name of configuration: '))
        return odoo
    return ''


def delete_configuration():
    pp(odoorpc.ODOO.list())
    session = input('Session to delete: ')
    if session:
        odoorpc.ODOO.remove(session)


def load_credential():
    dbname = input(f'{odoorpc.ODOO.list()}\nChoose entry if not empty: ')
    try:
        return odoorpc.ODOO.load(dbname)
    except ValueError as e:
        pp(e.args)
    except URLError as u:
        pp(u.args)


x = ''
target = ''
source = ''

while x != '3' or target == '' or source == '':
    val = input('''
        1. Set source
        2. Set target
        3. Start configuration
        ''')
    if val == '1':
        source = set_credential()
    elif val == '2':
        target = set_credential()
    elif val == '3':
        x = '3'
