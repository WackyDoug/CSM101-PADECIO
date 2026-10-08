

students = [
    {
    "UID": "NU01",
    "Name": "Harold",
    "Health": 100
    },
    {
    "UID": "NU02",
    "Name": "Mat",
    "Health": 200
    },
]


UIDremove = "NU01"


for index, student in enumerate(students):
    if UIDremove == student['UID']:
        students.pop(index)
        break




for ID in students:
    print(f"UID    : {ID['UID']}")
    print(f"Name   : {ID['Name'].title()}")
    print(f"Health : {ID['Health']}")
