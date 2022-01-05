# Contacts Manager V1.0
import resources
from colors import Color


resources.load()
while True:
    resources.menu()

    try:
        option = int(input(f'{Color.INPUT}Type your option: '))
        print(f'{Color.DIVISION}-' * 30)

        if option == 0:
            print(f'{Color.END}Program Ended.')
            break

        elif option == 1:
            resources.show_contacts()

        elif option == 2:
            if resources.AGENDA:
                name = input(f'{Color.INPUT}Type the contact name: ')
                resources.search_contact(name)
            else:
                print(f'{Color.ERROR}**No contacts.**')

        elif option == 3:
            name = input(f'{Color.INPUT}Type the contact name to be added: ')
            try:
                resources.AGENDA[name]
                print(f'{Color.ERROR}**Contact already exists.**')
            except KeyError:
                number, email, address = resources.read_details()
                resources.add_edit_contact(name, number, email, address)
                print(f'**{name} was added successfully.**')

        elif option == 4:
            if resources.AGENDA:
                name = input(f'{Color.INPUT}Type the contact name to be edited: ')
                try:
                    resources.AGENDA[name]
                    print(f'Editing contact: {name}')
                    number, email, address = resources.read_details()
                    resources.add_edit_contact(name, number, email, address)
                    print(f'**{name} was edited successfully.**')
                except KeyError:
                    print(f'{Color.ERROR}**Non-existent contact.**')
            else:
                print(f'{Color.ERROR}**No contacts.**')

        elif option == 5:
            if resources.AGENDA:
                name = input(f'{Color.INPUT}Type the contact name to be excluded: ')
                resources.del_contact(name)
                print(f'**{name} was excluded successfully.**')
            else:
                print(f'{Color.ERROR}**No contacts.**')

        elif option == 6:
            filename = input('Type the name of the file to be exported: ')
            if '.' in filename:
                file = filename.split('.')
                resources.export_csv(file[0]+'.csv')
            else:
                resources.export_csv(filename + '.csv')
            print('**Contacts exported successfully.**')

        elif option == 7:
            filename = input('Type the name of the file to be imported: ')
            if resources.import_csv(filename):
                print('**Contacts imported successfully.**')
            else:
                pass

        else:
            print(f'{Color.ERROR}**Invalid option.**')
    except ValueError:
        print(f'{Color.ERROR}**Type a number.**')
    except KeyboardInterrupt:
        break
