from student import Student


class HighScoolStudent(Student):

    school_name = 'High school student Academy'

    def get_school_name(self):
        return self.name + ' is a hight school student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"