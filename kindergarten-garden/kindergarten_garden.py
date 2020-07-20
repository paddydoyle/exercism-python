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
            self.students = STUDENTS
        else:
            self.students = sorted(students)

        rows = diagram.split()

        # Verify that the rows are equal sizes
        if len(set(len(row) for row in rows)) != 1:
            raise Exception("Garden diagram is unbalanced. Some rows"
                            "are longer than others: {}".format(rows))

        self.rows = rows

    def plants(self, student):
        if student not in self.students:
            raise Exception("Requested student {} not in the list: {}"
                            "".format(student, self.students))

        index = self.students.index(student) * PLANTS_PER_ROW

        return [PLANTS[ch] for row in self.rows
                for ch in row[index:index+PLANTS_PER_ROW]]
