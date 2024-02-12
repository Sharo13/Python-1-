# 1.შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს
#  პარამეტრად მიღებულ რიცხვს.
int_list = [10, 20, 30, 40]
def f(number):
    int_list.append(number)
new_num = eval(input("Enter number: "))
f(new_num)
print(f"Updated int_list: {int_list}")
# 2.დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
#  პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].
def sum_list(nums):
    return sum(nums)
num_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(f"Sum of the numbers: {sum_list(num_list)}")
# 3.შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს 
# იგივე სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას
gl_str = "Global"
def f():
    gl_str = "Local"
    return gl_str

print(f"Local variable: {f()}")
# 4.რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს 
# ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).
def sum1(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum1(number // 10)
number= int(input("Enter number:"))
print(f"The sum of the digits of {number} is {sum1(number)}.")
# 5.რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს 
# და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)
def reversed(st):
    if len(st) == 0:
        return st
    else:
        return reversed(st[1:]) + st[0]
st = input("Enter string: ")
print(f"Input: {st} \nOutout: {reversed(st)}")
