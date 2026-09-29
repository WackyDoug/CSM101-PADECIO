PADECIO_classroom = {
    "diza": {
    "studID" : "S001",
    "grade": [90, 85, 86, 82, 83, 90, 92],
    },
    "jeremy": {
    "studID" : "S002",
    "grade": [90, 85, 86, 82, 83, 90, 92],
    },
    "bob": {
    "studID" : "S003",
    "grade": [50, 50, 50, 50, 70, 56, 34],
    },
    "jayvee": {
    "studID" : "S004",
    "grade": [80, 89, 80, 90, 90, 90, 90],
    },
}

print("\n====Student_Checker====")
PADECIO_choice1 = input("search student name > ").lower()

has60 = False
PADECIO_total = 0
PADECIO_found = 0
for PADECIO_name, PADECIO_info in PADECIO_classroom.items():
    if PADECIO_name == PADECIO_choice1:
        PADECIO_found = 1
        print("\nFound Name")

        print(f"Student    : {PADECIO_name.title()} ")
        print(f"Student ID : {PADECIO_info['studID']}")

        for PADECIO_grade in PADECIO_info['grade']:
            if PADECIO_grade <= 60:
                has60 = True
            PADECIO_total += PADECIO_grade

        PADECIO_AVR = PADECIO_total / len(PADECIO_info['grade'])
        PADECIO_Highest = max(PADECIO_info['grade'])

        print(f"Average    : {PADECIO_AVR:.2f}")
        print(f"Highest    : {PADECIO_Highest}")
        if has60 == True:
            print("Student Candidate for Intervention")

        print("===Grades===")
        for PADECIO_grade in PADECIO_info['grade']:
            print(f"\t {PADECIO_grade}")
        break

if PADECIO_found == 0:
    print("No Student Found With That Name")
