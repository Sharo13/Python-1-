import json
from json import JSONEncoder

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student:
    row_id = 0

    def __init__(self, name, mark, address):
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = self.grade_calculator()
        Student.row_id += 1
        self.row_id = Student.row_id

    def grade_calculator(self):
        if self.mark >= 91:
            return "A"
        elif self.mark >= 81:
            return "B"
        elif self.mark >= 71:
            return "C"
        else:
            return "D"


class StudentEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__

address1 = Address("Tbilisi", "Saburtalo")
address2 = Address("Tbilisi", "Gldani-7-11-4-93")
address3 = Address("Tbilisi", "Leselidzs str. 25")
address4 = Address("Tbilisi", "Varketili IV 407-5-123")

student1 = Student("Paata", 87, address1)
student2 = Student("Demetre", 100, address2)
student3 = Student("Alexander", 100, address2)
student4 = Student("Teona", 92, address2)
student5 = Student("Nino", 99, address3)
student6 = Student("Andria", 87, address4)

students = [student1, student2, student3]

with open('students.json', 'w') as file:
    json.dump(students, file, cls=StudentEncoder, indent=3)

with open('students.json', 'r') as file:
    students_data = json.load(file)

for student_data in students_data:
    student_data['mark'] = str(student_data['mark'])  
    if 'grade' not in student_data:
        student_data['grade'] = Student(student_data['name'], int(student_data['mark']), None).grade

with open('modified_students.json', 'w') as file:
    json.dump(students_data, file, indent=3)
