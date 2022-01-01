from colors import Color

AGENDA = dict()


def menu():
    print(f'{Color.HEADER} ' * 12, f'{Color.TITLE}MENU', ' ' * 12)
    print(f'{Color.OPTIONS}1 - Show Contacts\n'
          '2 - Search Contact\n'
          '3 - Add Contact\n'
          '4 - Edit Contact\n'
          '5 - Remove Contact\n'
          '6 - Export Contacts to CSV\n'
          '7 - Import Contacts in CSV\n'
          '0 - End Program')
    print(f'{Color.TITLE}-' * 30)


def show_contacts():
    if AGENDA:
        for contact in AGENDA:
            search_contact(contact)
    else:
        print(f'{Color.ERROR}**No contacts.**')


def search_contact(name):
    try:
        AGENDA[name]
        print(f'{Color.NORMAL}Name: {name}')
        print(f'Number: {AGENDA[name]["Telephone"]}')
        print(f'Email: {AGENDA[name]["Email"]}')
        print(f'Address: {AGENDA[name]["Address"]}')
        print(f'{Color.TITLE}-' * 37)
    except KeyError:
        print(f'{Color.ERROR}**Non-existant contact.**')
    except Exception as err:
        print(f'{Color.ERROR}Error: {err}')


def read_details():
    number = input(f'Type the telephone: ')
    email = input(f'Type the email: ')
    address = input(f'Type the address: ')
    return number, email, address


def add_edit_contact(name, number, email, address):
    AGENDA[name] = {
        'Telephone': number,
        'Email': email,
        'Address': address
    }
    save()


def del_contact(name):
    # del AGENDA[name]
    try:
        AGENDA.pop(name)
        save()
    except KeyError:
        print(f'{Color.ERROR}**Non-existant contact.**')
    except Exception as err:
        print(f'{Color.ERROR}Error: {err}')


def export_csv(filename):
    try:
        with open(filename, 'w') as file:
            for contact in AGENDA:
                number = AGENDA[contact]['Telephone']
                email = AGENDA[contact]['Email']
                address = AGENDA[contact]['Address']
                file.write(f'{contact},{number},{email},{address}\n')
    except:
        print(f'{Color.ERROR}**Failed to export contacts.**')


def import_csv(filename):
    try:
        with open(filename, 'r') as file:
            for contacts in file.readlines():
                data = contacts.strip().split(',')
                name = data[0]
                number = data[1]
                email = data[2]
                address = data[3]
                add_edit_contact(name, number, email, address)
        return True
    except FileNotFoundError:
        print(f'{Color.ERROR}**Non-existant file.**')
        return False
    except Exception as err:
        print(f'{Color.ERROR}**Error: {err}**')
        return False


def load():
    try:
        open('database.csv', 'r')
    except FileNotFoundError:
        open('database.csv', 'w')
        print(f'{Color.DATA}Creating database..')
    finally:
        import_csv('database.csv')
        print(f'{Color.DATA}>{len(AGENDA)} contacts loaded.<')


def save():
    export_csv('database.csv')
