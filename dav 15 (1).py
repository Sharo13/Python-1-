# 1.დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას 
import csv

def create_file(fpath):
    h = ["id", "name", "age", "grade", "subject_name", "marks"]
    with open(fpath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(h)

def add_student(fpath, student_data):
    with open(fpath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

def get_info():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    subject_name = input("Enter subject name: ")
    marks = input("Enter student marks: ")

    return [id, name, age, grade, subject_name, marks]

if __name__ == "__main__":
    ff = "students.csv"
    create_file(ff)
    student_data = get_info()
    add_student(ff, student_data)
    print("Student added successfully.")

# 2.დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება,
# როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
# (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.

def read_students(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def read_student(fpath, stID):
    with open(fpath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] == stID:
                print(row)
                return
        print(f"Student with ID {stID} not found.")

def main():
    f= "students.csv"

    while True:
        print("\nMenu:")
        print("1. Read information for all students")
        print("2. Read information for a specific student")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\nAll Students:")
            read_students(f)
        elif choice == '2':
            stID = input("Enter the ID of the student: ")
            read_student(f, stID)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

# # 3.დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის
#  ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.


def update_score(fpath, stID, subject_name, updated_score):
    with open(fpath, mode='r') as file:
        students_data = list(csv.DictReader(file))
    for student in students_data:
        if student["id"] == stID and student["subject_name"] == subject_name:
            student["marks"] = updated_score
            break
    else:
        print(f"Student with ID {stID} and subject {subject_name} not found.")
        return

    with open(fpath, mode='w', newline='') as file:
        header = ["id", "name", "age", "grade", "subject_name", "marks"]
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(students_data)

    print(f"Score updated successfully for student {stID}, subject {subject_name}.")

if __name__ == "__main__":
    fpath = "students.csv"
    stID = input("Enter the ID of the student: ")
    subject= input("Enter the subject name: ")
    updated_score = input("Enter the updated score: ")

    update_score(fpath, stID, subject, updated_score)

