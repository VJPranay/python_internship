# basic contacts application


data_repo = [
    {'name': 'pranay', 'phone': 9652290152},
]

user_input = input("Do you want to add a contact on to the list ? (y/Y)")

while user_input == 'y' or user_input == 'Y':
    name = input("Please enter the name")
    phone = int(input("Please enter number"))
    temp_contact = {
        'name': name,
        'phone': phone,
    }
    data_repo.append(temp_contact)
    user_input = input("Do you want to add a contact on to the list ? (y)")

for contact in data_repo:
    print('||', ' ', contact['name'], ' ', contact['phone'], ' ')
'''
T and T == T
T and F == F
T and F == F
F and F == F


T or T == T
T or F == T
F or T == T
F or F == F


'''
