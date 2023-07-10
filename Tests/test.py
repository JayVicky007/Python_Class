class Group:
    def __init__(self, name):
        self.name = name
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Attendance:
    def __init__(self, group):
        self.group = group
        self.attendance_data = {}

    def mark_attendance(self, classroom, user):
        if classroom not in self.attendance_data:
            self.attendance_data[classroom] = {}

        if user.id not in self.attendance_data[classroom]:
            self.attendance_data[classroom][user.id] = True
            print(f"Attendance marked for {user.name} in {classroom}")
        else:
            print(f"Attendance already marked for {user.name} in {classroom}")

    def get_attendance(self, classroom):
        if classroom in self.attendance_data:
            return self.attendance_data[classroom]
        else:
            return {}


# Example usage
group = Group("Lab Group")
classroom1 = "Lab A"
classroom2 = "Lab B"

group.add_classroom(classroom1)
group.add_classroom(classroom2)

user1 = User("John", 1)
user2 = User("Alice", 2)
user3 = User("Bob", 3)

attendance = Attendance(group)

attendance.mark_attendance(classroom1, user1)
attendance.mark_attendance(classroom1, user2)
attendance.mark_attendance(classroom2, user1)

print(attendance.get_attendance(classroom1))
print(attendance.get_attendance(classroom2))


# import requests

# url = "https://api-customer-038j.onrender.com/customer"

# data = {
#     "name": "John Smith",
#     "age": 39,
#     "order": "ABC123"
# }

# response = requests.post(url, json=data)
# content = response.json()

# print(content)
