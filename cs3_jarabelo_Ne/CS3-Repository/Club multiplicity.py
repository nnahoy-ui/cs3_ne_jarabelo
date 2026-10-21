class club:

    def __init__(self, name, adviser):
        self.name = name
        self.adviser = adviser
        self.members = []

    def add_member(self, member):
        self.members.append(member)

class member:

    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level

    def attend_meeting(self, meeting):
        print (f"{self.name} attended at {meeting}")


class meeting:

    def __init__(self, date, venue):
        self.date = date
        self.venue = venue
        self.attendees = []

    def record_attendance(self, members):
        self.attendees.append(member)

club1 = club("NeonPink", "Mr Salcedo")
member1 = member("Sebastain", "G9")
member2 = member("Yohann", "G9")
member3 = member ("Jarabelo", "G9")

meeting1 = meeting("September 16, 2026", "CS lab 3")
club1.add_member(member1)
club1.add_member(member2)
club1.add_member(member3)

print(club1.members[0].name)
print(member1.attend.meeting(meeting1.venue))