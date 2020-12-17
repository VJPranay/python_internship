# for > loop through the lists or loop through a range of values
# while >


import itertools

names = [
    'pranay',
    'chandu',
    'aparna',
    'niha',
    'sowmya',
    'jayanthi'
]

assignments = [
    {'name': '0001', 'phone': 1},
    {'name': '0002', 'phone': 1},
    {'name': '0003', 'phone': 1},
    {'name': '0004', 'phone': 1},
    {'name': '0005', 'phone': 1},
    {'name': '0007', 'phone': 1},
    {'name': '0008', 'phone': 1},
    {'name': '0009', 'phone': 1},
    {'name': '0010', 'phone': 1},
    {'name': '0011', 'phone': 1},
    {'name': '0012', 'phone': 1},
    {'name': '0013', 'phone': 1},
    {'name': '0014', 'phone': 1},
    {'name': '0051', 'phone': 1},
    {'name': '0041', 'phone': 1},
    {'name': '0021', 'phone': 1},
    {'name': '0061', 'phone': 1},
    {'name': '0061', 'phone': 1},
    {'name': '0421', 'phone': 1},
    {'name': '03421', 'phone': 1},
    {'name': '4234', 'phone': 1},
    {'name': '123', 'phone': 1},
    {'name': '134', 'phone': 1},
    {'name': '434', 'phone': 1},
    {'name': '55', 'phone': 1},
]

cycle_names = itertools.cycle(names)
for assignment in assignments:
    print(assignment['name'], " is assigned to ", next(cycle_names))

# for assignment in assignments:
#     print(assignment)

# number = 0
# while number < 10:
#     print(number)
#     number = number + 1


# names = ['pranay', 'karthik', 'chandu', 'marc']
#
# for name in names:
#     if name == 'pranay':
#         print(name.upper())
#     else:
#         print(name)
