"""
School()



"""

class School:
    def __init__(self):
        self.students = set()
        self.results = []

    def add_student(self, name, grade):
        l = len(self.students)
        self.students.add((name, grade))
        if l < len(self.students):
            self.results.append(name)
        self.results.append(True)

    def roster(self):
        return []

    def grade(self, grade_number):
        result = []

        for student in self.students:
            if student[1] == grade_number:
                result.append(student[0])

        return result

    def added(self):
        return [self.results[-1]]
