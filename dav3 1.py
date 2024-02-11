# # 1.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

n = int(input("Enter number: "))
sum = 0
for i in range(1,n+1):
    sum +=i 
print(f"The sum of numbers from 1 to {n}  is {sum}")

# # 2.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. 
# # მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1

n = int(input("Enter number: "))
while True:
    print(n, end=' ')
    n-=1
    if n <= 0:
        break

# # 3.დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი. 
# # როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.

from random import  randint
rand_num = randint (1, 1000)
while True:
    n = int (input("Enter number: "))
    if n == rand_num:
        print("Correct!")
        break
    elif n > rand_num:
        print("Too big, try again!")
        continue
    else:
        print("Too small, try again!")
        continue


# # 4.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია,
# #  მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
# #  ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.
total_sum = 0 
while True:
    n =  input("Enter number: ")
    if n == "sum":
        print(total_sum)
        break
    n = int(n)
    if n > 0 :
        total_sum += n
    

  






