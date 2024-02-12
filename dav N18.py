# 1 შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. კლასში 
# დაამატეთ __add__ მეთოდი, რომ მოახდინოთ  ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Error!!")

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3) 

#3. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს 
# ორი წიგნის ტოლობას. ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია. 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2) 
print(book1 == book3)  