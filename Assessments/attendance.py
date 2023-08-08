class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.is_present = False
        self.attendance_record = []  

    def __str__(self):
        return self.name


class Group:
    def __init__(self, title):
        self.title = title
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def __str__(self):
        return self.title


class Attendance:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)
        print(f"{group} has been added")

    def add_user_to_group(self, group, user):
        if group in self.groups:
            group.add_user(user)
            return f"{user} has been added to {group}"
        else:
            return 'Could not find group'

    def remove_user_from_group(self, group, user):
        if group in self.groups:
            group.remove_user(user)
            return f"{user} is absent from {group}"
        else:
            return 'Could not find group'

    def mark_attendance(self, user, date):
        user.is_present = True
        user.attendance_record.append(date)

    def view_attendance(self, user):
        return user.attendance_record

    def generate_attendance_report(self, group):
        pass

    def display_all_groups(self):
        for group in self.groups:
            print(group)


def main():

    group1 = Group('Python class')
    group2 = Group('Java class')

    attendance = Attendance()
    attendance.add_group(group1)
    attendance.add_group(group2)

    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Mark attendance for a student")
        print("3. View attendance for a student")
        print("4. Generate attendance report")
        print("5. Exit the program")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter the student's name: ")
            number = input("Enter the student's number: ")
            new_user = User(name, number)
            group = input("Enter the group to add the student (Python class/Java class): ").lower()
            if group == "python class":
                attendance.add_user_to_group(group1, new_user)
                print(f"{new_user} successfully added!")
            elif group == "java class":
                attendance.add_user_to_group(group2, new_user)
                print(f"{new_user} successfully added!")

        elif choice == '2':
            name = input("Enter the student's name: ")
            date = input("Enter the date of attendance (YYYY-MM-DD): ")
            for user in group1.users + group2.users:
                if user.name == name:
                    attendance.mark_attendance(user, date)
                    print(f"{user} is present on {date}")
                    break
            else:
                print("Student not found!")

        elif choice == '3':
            name = input("Enter the student's name: ")
            for user in group1.users + group2.users:
                if user.name == name:
                    print(f"Attendance record for {user}: {attendance.view_attendance(user)}")
                    break
            else:
                print("Student not found!")

        elif choice == '4':
            group = input("Enter the group to generate the attendance report (Python class/Java class): ").lower()
            if group == "python class":
                print(attendance.generate_attendance_report(group1))
            elif group == "java class":
                print(attendance.generate_attendance_report(group2))

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


main()

