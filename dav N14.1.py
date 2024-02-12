import os
import json
# 1.დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.
def create_file(faddress, fname):
    fpath = os.path.join(faddress, fname)
    try:
        with open(fpath, 'w') as file:
            pass
    except Exception as e:
        print(f"Error: {e}")

faddress = "C:/Users/asus/Desktop/python/davalebebi/pp"
fname = "file.json"
create_file(faddress, fname)

# 2.დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს

def read_file(faddress, fname):
    fpath = os.path.join(faddress, fname)
    try:
        with open(fpath, 'r') as file:
            contents = file.read()
            return contents
    except Exception as e:
        print(f"Error: {e}")

file_contents = read_file(faddress, fname)
if file_contents:
    print(f"File contents: {file_contents}")

# 3.დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს
"""თუ განახლებაში იგულისხმება არსებულ კონტენტზე ახლის გადაწერა"""
def update_file1(faddress, fname, new_content):
    fpath = os.path.join(faddress, fname)
    try:
        with open(fpath, 'w') as file:
            file.write(new_content)
        print(f"File updated successfully at {fname}")
    except Exception as e:
        print(f"Error: {e}")

new_content = "gadawera\n"
update_file1(faddress, fname, new_content)

"""თუ განახლებაში იგულისხმება ახალი კონტენტის დამატება"""
def update_file(faddress, fname, new_content):
    fpath = os.path.join(faddress, fname)
    try:
        with open(fpath, 'a') as file:
            file.write(new_content)
        print(f"Content appended successfully to {fname}")
    except Exception as e:
        print(f"Error: {e}")

new_content = "chamateba.\n"
update_file(faddress, fname, new_content)

# 4.დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს
# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია


def fappend(fname, dictionaries):
    fpath = os.path.join(faddress, fname)

    try:
        with open(fpath, 'a') as file:
            for input_dict in dictionaries:
                json.dump(input_dict, file)
                file.write('\n')  
        print(f"Dictionaries appended to '{fname}' successfully.")
    except Exception as e:
        print(f"Error : {e}")

datas = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

fappend(fname, datas)

