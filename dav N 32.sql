-- 1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
USE it_step;
create table Author(
AuthorID int NOT NULL,
Aname varchar(100),
Aage int,
primary key(AuthorID)
);
-- 2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
create table Books(
BookID int NOT NULL,
primary key (BookID),
Bname varchar (1000),
Byear int,
foreign key(AuthorID) REFERENCES Author(AuthorID)
);

-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO Author (AuthorID, Aname, Aage) VALUES
(1, 'Diana Wynne Jones', 70),
(2, 'Stephen King', 75),
(3, 'Haruki Murakami', 60),
(4, 'Mariam Gurgenishvili', 30),
(5, 'Jane Austen', 50);

-- Inserting records into the Books table
INSERT INTO Books (BookID, Bname, Byear, AuthorID) VALUES
(1, 'Howls Moving Castle', 1986, 1),
(2, 'The Shining', 1977, 2),
(3, 'Norwegian Wood', 1987, 3),
(4, 'Pearls', 2022, 4),
(5, 'Pride  Prejudice' , 1813, 5);


-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE Books
SET Bname = 'The Knight in the Panthers Skin', Byear = 1712
WHERE BookID = 2;

-- 5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
delete from Author;
delete from Books;
-- 6. წაშალეთ Author და Books ცხრილები
drop table Author;
drop table Books;


