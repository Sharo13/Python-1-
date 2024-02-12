my_dict = {
    "students": [
        {"id": 20, "name": "giorgi", "age": 25},
        {"id": 25, "name": "giorgi", "age": 23},
        {"id": 100, "name": "nika", "age": 22},
        {"id": 56, "name": "nika", "age": 25},
        {"id": 1232, "name": "dato", "age": 22},
        {"id": 846723, "name": "archili", "age": 32}
    ],
    "subjects": [
        {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
        {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
        {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
        {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
        {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    ]
}

def student_ids():
    student_ids = [student["id"] for student in my_dict["students"]]
    print("\nStudentebis ID:", ", ".join(map(str, student_ids)))

def student_info(id):
    info = next((student for student in my_dict["students"] if student["id"] == id), None)
    if info:
        print("\nStudent Information:")
        print(f"ID: {info['id']}, name: {info['name']}, age: {info['age']}")
        for subject in my_dict["subjects"]:
            grade = subject["grades"].get(str(id), "-")  
            print(f"subject: {subject['name']}, grade: {grade}")
    else:
        print("Araswori ID.")

student_ids()
id = int(input("\nAirchiet studentis ID: "))
student_info(id)
