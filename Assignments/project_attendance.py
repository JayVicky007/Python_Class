class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.is_present = False
    
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
            return f"{user} has been removed from {group}"
        else:
            return 'Could not find group'

    def check_attendance(self, group):
        if group in self.groups:
            present_users = [user for user in group.users if user.is_present]
            return present_users
        else:
            return 'Could not find group'

    def display_all_groups(self):
        for group in self.groups:
            print(group)
    
    def run_attendance_system(self):
        while True:
            print("Attendance System Menu:")
            print("1. Add a new student")
            print("2. Mark attendance for a student")
            print("3. View attendance for a student")
            print("4. Generate attendance report")
            print("5. Exit the program")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_new_student()
            elif choice == "2":
                self.mark_attendance()
            elif choice == "3":
                self.view_attendance()
            elif choice == "4":
                self.generate_attendance_report()
            elif choice == "5":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_student(self):
        name = input("Enter student's name: ")
        number = input("Enter student's number: ")
        user = User(name, number)
        group = self.select_group()
        if group:
            response = self.add_user_to_group(group, user)
            print(response)
        else:
            print("Could not find group.")

    def mark_attendance(self):
        group = self.select_group()
        if group:
            user = self.select_user(group)
            if user:
                date = input("Enter the attendance date: ")
                user.is_present = True
                print(f"Attendance marked for {user} on {date}.")
            else:
                print("Could not find user.")
        else:
            print("Could not find group.")

    def view_attendance(self):
        group = self.select_group()
        if group:
            user = self.select_user(group)
            if user:
                attendance_status = "Present" if user.is_present else "Absent"
                print(f"Attendance status for {user}: {attendance_status}")
            else:
                print("Could not find user.")
        else:
            print("Could not find group.")

    def generate_attendance_report(self):
        group = self.select_group()
        if group:
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            present_users = [user for user in group.users if user.is_present]
            print(f"Attendance report for {group} between {start_date} and {end_date}:")
            for user in present_users:
                print(f"{user}: Present")
            absent_users = [user for user in group.users if not user.is_present]
            for user in absent_users:
                print(f"{user}: Absent")
        else:
            print("Could not find group.")

    def select_group(self):
        print("Available Groups:")
        for i, group in enumerate(self.groups):
            print(f"{i+1}. {group}")
        group_number = int(input("Enter the group number: "))
        if group_number >= 1 and group_number <= len(self.groups):
            return self.groups[group_number - 1]
        else:
            return None

    def select_user(self, group):
        print("Available Users:")
        for i, user in enumerate(group.users):
            print(f"{i+1}. {user}")
        user_number = int(input("Enter the user number: "))
        if user_number >= 1 and user_number <= len(group.users):
            return group.users[user_number - 1]
        else:
            return None


def main():
    group1 = Group('Python class')
    group2 = Group('Java class')

    attendance = Attendance()
    attendance.add_group(group1)
    attendance.add_group(group2)

    attendance.run_attendance_system()


main()
