""""1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს შორის შესრულებული არითმეტიკული 
ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება)"""
x = eval (input("enter first number: "))
y= eval (input("enter second number: "))

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} ** {y} = {x**y}")
print(f"{x} // {y} = {x//y}")
print(f"{x} / {y} = {x/y}")
print(f"{x} % {y} = {x%y}") 

#2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.
d1 = eval(input("Enter fisrt diagonal: "))
d2 = eval(input("Enter second diagonal: "))
print(f"area of rhombus is {(d1*d2)/2}")

#3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.
metre = eval(input("Enter metre: "))
print(f"{metre} metre to cm is {metre*100}")
print(f"{metre} metre to mm is {metre*1000}")
print(f"{metre} metre to decimeter is {metre*10}")
print(f"{metre} metre to mile is {metre * 0.000621371}")
#4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა."
x = eval( input("enter triangle side: "))
h=eval( input("enter triangle height: "))
print(f"triangle area is {(h*x)/2}")