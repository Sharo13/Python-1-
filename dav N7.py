# 1.დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.
def fibonacci(n):
    fib = [1, 1]
    for _ in range(2, n):
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
    return fib[:n]

n = int(input ("Enter number: "))
print(fibonacci(n))
# 2.დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები. (ანაგრამი არის სიტყვა ან შესიტყვება,
#  რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.
def anagrams (st1, st2):
    st1 = st1.replace(" ", "").lower()
    st2 = st2.replace(" ", "").lower()
    return sorted(st1) == sorted(st2)
st1=input ("Enter first string: ")
st2=input ("Enter second string: ")
if anagrams(st1, st2):
    print(f"{st1} and {st2} are anagrams")
else:
    print({f"{st1} and {st2} are not anagrams"})
# 3.დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
def factorial (n):
    fact = 1
    while n > 0 :
        fact *= n
        n-=1
    return fact
n = int(input("Enter number:"))
print(factorial(n))
# 4.დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ
# უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა
def count_symb(st, symb):
    return st.count(symb)

st = input ("Enter string: ")
symb = input("Enter symbole: ")
print(f"{symb} is reapeted {count_symb(st,symb)} times")

    