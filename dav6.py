# დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი;
#  თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
# მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:
# a – append
# r – remove
# e – exit
# მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.

my_list = []
while True:
    num = input("First enter a command (a, r, e), then a number: ")

    command = num[0] 
    if command == 'a':
        if len(num) > 2 and num[2:].isdigit():
            number = int(num[2:])
            my_list.append(number)
        else:
            print("Invalid input.")
    elif command == 'r':
        if len(num) > 2 and num[2:].isdigit():
            number = int(num[2:])
            if number in my_list:
                my_list.remove(number)
            else:
                print("Number not found in the list.")
        else:
            print("Invalid input. ")
    elif command == 'e':
        break
    else:
        print("Enter a valid command (a, r, e)!")

print("Resulting list:", my_list)

# 2.დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექსს;

# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;

# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

my_list = [43, '22', 12, 66, 210, ["hi"]]
i = my_list.index(210)
print(f"a. Index of 210: {i}")

my_list[-1].append("hello")
print(f"b. {my_list}")

del my_list[2]
print(f"c. {my_list}")

my_list_2 = my_list.copy()
my_list_2.clear()
print(f"d. my_list: {my_list}")
print(f"   my_list_2 : {my_list_2}")

# დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს,
# თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.
import re

phone = input("Enter a phone number (in the format (123) 456-789): ")
f = re.compile(r'^\(\d{3}\) \d{3}-\d{3}$')

if f.match(phone):
    print(phone)
else:
    print("Invalid format")






