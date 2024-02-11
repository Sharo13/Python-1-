# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

st = input("Enter string: ")
st_enc = st.encode('utf-8')
print(st_enc)
# 2.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ 
# ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში 
# და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს
# სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip().

# მაგ.:

# "  Python is funny     ".strip()   ====>  "Python is funny"
st = input("Enter string: ")
st1 = 'Python ' + st.strip().lower()  
st1 = st1.replace('python', 'Python')
print(st1)
# 3.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.
st = input("Enter string: ")
half_length = len(st) // 2
first_half = st[:half_length]
# print("First Half of the String:", first_half)
# 4.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. 
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)
st = input("Enter a string: ")
if st and any(char.isdigit() for char in st) and st.isalnum():
    print("String is valid.")
else:
    print("String is not valid.")
#  5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში
#  და ბეჭდავს სტრიქონს.

st = input("Enter a string: ")
bt = st.encode('utf-8')
print("In bytes:", bt)
dst = bt.decode('utf-8')
print("Decoded String:", dst)


