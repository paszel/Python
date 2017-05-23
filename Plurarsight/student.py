from main import students


class Student:

    school_name = 'Elementary Student'

    def __init__(self, name, last_name, student_id=336):
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name