class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.ispresent = False

    def __str__(self):
        return self.name

class Group:
    def __init__(self, title):
        self.title = title
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        if user in self.users:
            return f"user already exists"

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            
    def __str__(self):
        return self.title
    
class Attendance:
    def __init__(self, group):
        self.groups = []
        self.groups.append(group)

    def add_group(self, group):
        self.groups.append(group)
        if group in self.groups:
            return f"This group already exists"
        else:
            return f"{group} group created"
    
    def add_user_to_group(self, user, group):
        group.add_user(user)
        return f"{user} has been added to the {group} group"
    
    def remove_user_from_group(self, user, group):
        group.remove_user(user)
        return f"{user} has been removed from the {group} group"
    
    def check_attendance(self, group):
        if group in self.groups:
            present_user = [user for user in group.users if user.ispresent] 
            return present_user
        else:
            return f"Could not find group"
    
    
    def display_all_groups(self, group):
        if group in self.groups:
            print(group)
    
    # def add_new_student(self):
    #     name = input("Enter student name: ")
    #     number = input("Enter student number: ")
    #     user = User(name, number)

    # def admin_menu(self):
    #     while True:
    #         print("1. Add a new student")
    #         print("2. Mark attendance for a student")
    #         print("3. View atendance for a student")
    #         print("4. Mark attendance for a student")
    #         print("5. Generate attendance report")

    #         choice = input("Enter a choice from 1-5")

            # if choice == "1":
            #     name = input

    def __str__(self):
        return self.group
    
def main():
    
    group1 = Group("Python")
    group2 = Group("Java")

    user1 = User("Lamba", 419)
    user2 = User("Banga", 45)
    user3 = User("Killua", 1)


    attendance = Attendance(group1)

    attendance.add_group(group1)
    attendance.add_group(group2)

    attendance.add_user_to_group(user3, group1)
    attendance.add_user_to_group(user2, group1)
    attendance.add_user_to_group(user1, group2)

    attendance.remove_user_from_group(user3, group1)

    user1.ispresent = True

    attendance.display_all_groups(group1)

    print(attendance.check_attendance(group1))

    print(user1)
    print(user2)

main()