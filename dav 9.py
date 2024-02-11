#1. დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის
# გამოყენებით დააჯგუფეთ სიების ელემენტები.
# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def zip_lists(list1, list2):
    if len(list1) != len(list2):
        print("Lists are not of the same size")
        return None
    zipped_list = list(zip(list1, list2))
    return zipped_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = zip_lists(list1, list2)
print(result)

# 2.დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
#  ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce

def prod_elem(nums):
    try:
        if not all(isinstance(num, (int, float)) for num in nums):
            raise TypeError("Input must be a list of numbers")
        return reduce(lambda x, y: x * y, nums, 1)

    except TypeError as e:
        print(f"Error: {e}")
        return None

list1 = [1, 2, 3, 4, 5]
print( prod_elem(list1))

# 3.დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და 
# აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

nums = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: x % 2 != 0, nums)))

# 4.დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც 
# აღმოჩნდა ისიც გაითვალისწინეთ.
# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც 
# მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

def f(string_list, st):
    try:
        if not all(isinstance(s, str) for s in string_list):
            raise TypeError("Input must be a list of strings")
        fstr = list(filter(lambda s: s.endswith(st), string_list))
        return fstr
    except TypeError as e:
        print(f"Error: {e}")
        return None
    
st_list = ['hello', 'world', 'coding', 'nod']
st = 'ing'
print(f(st_list, st))
