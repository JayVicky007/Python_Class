class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return self.name


class Group:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def __str__(self) -> str:
        return self.name


class Attendance:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)
        print(f"{group} has been added")

    def add_user_to_group(self, group: Group, user):
        if len(self.groups) != 0:
            for i in self.groups:
                if i.name == group.name:
                    i.add_user(user)
                    return f"{user} has been added to {group}"
            return f"Group {group} not found."
        else:
            return "No group added to attendance."

    def display_all_groups(self):
        for group in self.groups:
            print(group)

group1 = Group("Python Class")
group2 = Group("Java Class")

attendance = Attendance()
attendance.add_group(group1)
attendance.add_group(group2)

user1 = User("John Smith", 12345)
user2 = User("Jack Sparrow", 20435)

response = attendance.add_user_to_group(group1, user1)
response2 = attendance.add_user_to_group(group1, user2)

print(response)
print(response2)