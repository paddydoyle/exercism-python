PLANTS = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets',
    }

PLANTS_PER_ROW = 2

STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
    ]


class Garden:
    def __init__(self, diagram, students=None):
        if not students:
            students = STUDENTS
        else:
            students = sorted(students)

        rows = diagram.split()

        self.rows = rows

        self.student_map = {student: self._gen_plants(student,
                                                      index * PLANTS_PER_ROW)
                            for (index, student) in enumerate(students)}

    def _gen_plants(self, student, index):
        return [PLANTS[ch] for row in self.rows
                for ch in row[index:index+PLANTS_PER_ROW]]

    def plants(self, student):
        if student not in self.student_map:
            raise Exception("Requested student {} not in the list: {}"
                            "".format(student, keys(self.student_map)))

        return self.student_map[student]
