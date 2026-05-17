class Student:
    def __init__(self, first_name, last_name, age, gender, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.department = department


students = []

# initial 10 students
students.append(Student("Lamine", "Yamal", 19, "M", "CS"))
students.append(Student("Pedri", "Gonzalez", 22, "M", "EE"))
students.append(Student("Arda", "Güler", 21, "M", "ME"))
students.append(Student("Kenan", "Yıldız", 23, "M", "CS"))
students.append(Student("Sidiki", "Cherif", 19, "M", "CE"))
students.append(Student("Christ", "Oulai", 19, "M", "IE"))
students.append(Student("Alexia", "Putellas", 20, "F", "CS"))
students.append(Student("Birgül", "Sadıkoğlu", 22, "F", "EE"))
students.append(Student("Yiğit", "Akçicek", 21, "M", "ME"))
students.append(Student("Selin", "Celik", 23, "F", "CS"))


while True:
    print("\n***MENU***")
    print("(1) Add student")
    print("2 Find student")
    print("3 Show all students")
    print("4 Show by age range")
    print("5 Update student")
    print("6 Delete student")
    print("7 Write to file")
    print("8 Read from file")
    print("0 Exit")

    choice = input("Your Choice: ")

    if choice == "1":
        fn = input("First name: ")
        ln = input("Last name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        department = input("Department: ")

        students.append(Student(fn, ln, age, gender, department))
        print("Student added")

    elif choice == "2":
        fn = input("First name: ")
        ln = input("Last name: ")

        found = False
        for s in students:
            if s.first_name == fn and s.last_name == ln:
                print(s.first_name, s.last_name, s.age, s.gender, s.department)
                found = True

        if not found:
            print("Student not found")

    elif choice == "3":
        for s in students:
            print(s.first_name, s.last_name, s.age, s.gender, s.department)

    
    elif choice == "4":
        min_age = int(input("Min age: "))
        max_age = int(input("Max age: "))

        for s in students:
            if s.age >= min_age and s.age <= max_age:
                print(s.first_name, s.last_name, s.age)


    elif choice == "5":
        fn = input("First name: ")
        ln = input("Last name: ")

        for s in students:
            if s.first_name == fn and s.last_name == ln:
                print("1 name 2 surname 3 age 4 gender 5 department")
                ch = input("Choose: ")

                if ch == "1":
                    s.first_name = input("New name: ")
                elif ch == "2":
                    s.last_name = input("New surname: ")
                elif ch == "3":
                    s.age = int(input("New age: "))
                elif ch == "4":
                    s.gender = input("New gender: ")
                elif ch == "5":
                    s.department = input("New department: ")

                print("Student updated")

    
    elif choice == "6":
        fn = input("First name: ")
        ln = input("Last name: ")

        for s in students:
            if s.first_name == fn and s.last_name == ln:
                students.remove(s)
                print("Student deleted")
                break

    
    elif choice == "7":
        file = open("students.txt", "w")
        for s in students:
            file.write(s.first_name + "," + s.last_name + "," + str(s.age) + "," + s.gender + "," + s.department + "\n")
        file.close()
        print("Saved")

    
    elif choice == "8":
        try:
            file = open("students.txt", "r")
            students.clear()

            for line in file:
                parts = line.strip().split(",")
                students.append(Student(parts[0], parts[1], int(parts[2]), parts[3], parts[4]))

            file.close()
            print("File Loaded")
        except:
            print("File not found")

    elif choice == "0":
        break

    else:
        print("Please enter valid choice !!")
