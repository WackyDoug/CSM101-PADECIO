

#Practice 4
students = {}


number = int(input("Enter number of students: "))

for i in range(number):
    print("\nStudent", i + 1)

    name = input("Enter Student name: ")

    grade1 = float(input("Enter Grade 1 > "))
    grade2 = float(input("Enter Grade 2 > "))
    grade3 = float(input("Enter Grade 3 > "))

    students[name] = (grade1, grade2, grade3)

print("\n======Student Records======")

highest = 0
namehighest = ""
tally = 0

lowest = 100
namelowest = ""

for name, grade  in students.items():
    average =sum(grade) / len(grade)
    print(f"{name}, {grade}, Average: {average:.2f}")

    if average > highest:
        highest = average
        namehighest = name

    if average < lowest:
        lowest = average
        namelowest = name

    for g in grade:
        if g < 75:
            tally += 1


print(f"Student : {namehighest} got the highest average of {highest:.2f}")
print(f"Student : {namelowest} got the lowest average of {lowest:.2f}")
print(f"There are {tally} grades which are below 75")