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
            return f"{user} is absent from {group}"
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
            
def main():
    group1 = Group('Python class')
    group2 = Group('Java class')

    attendance = Attendance()
    attendance.add_group(group1)
    attendance.add_group(group2)

    user1 = User('John', 123456)
    user2 = User('James', 123456)
    user3 = User('Jane', 123456)
    user1 = User('John', 123456)

    response = attendance.add_user_to_group(group1, user1)
    response2 = attendance.add_user_to_group(group1, user2)
    response3 = attendance.add_user_to_group(group2, user2)
    response4 = attendance.add_user_to_group(group1, user3)

    
    print()
    print("Student List")
    print(response)
    print(response2)
    print(response3)
    print(response4)

    response5 = attendance.remove_user_from_group(group1, user2)
    print()
    print(f"{response5}")

    user3.is_present = True
    user1.is_present = True
    # user2.is_present = False
    attendance_status = attendance.check_attendance(group1)

    print()
    print(f"Attendance List for {group1}:")
    for user in attendance_status:
        print(f"{user} is present") 

main()

