import mysql.connector

db_connector = mysql.connector.connect(
    host="localhost",
    user="elene",
    password="password",
    database="it_step"
)

cursor = db_connector.cursor()

cursor.execute("""
    CREATE TABLE  User (
        user_id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE
    )
""")


cursor.execute("""
    CREATE TABLE Profile (
        profile_id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT UNIQUE,
        fname VARCHAR(100),
        bio varchar(100),
        pr_pic varchar(100),
        FOREIGN KEY (user_id) REFERENCES User(user_id)
    )
""")

user_data = [
    ('Elene1', 'Elene1@gmail.com'),
    ('Elene2', 'Elene2@gmail.com'),
    ('Elene3', 'Elene3@gmail.com'),
    ('Elene4', 'Elene4@gmail.com'),
    ('Elene5', 'Elene5@gmail.com')
]
cursor.executemany("INSERT INTO User (username, email) VALUES (%s, %s,)", user_data)


profile_data = [
    (1, 'Elene1', "x", 'Lorem '),
    (2, 'Elene2', "xx", 'ipsum'),
    (3, 'Elene3', "xxx", 'Lorem ipsum '),
    (4, 'Elene4', "xxxx", 'ipsum Lorem'),
    (5, 'Elene5', "xxxxx", 'LoremLorem')
]
cursor.executemany("INSERT INTO Profile (user_id, fname, pr_oic, bio) VALUES (%s, %s, %s, %s)", profile_data)

db_connector.commit()
db_connector.close()

####################################################################################

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_UR = "mysql+pymysql://elene:admin1234@localhost/it_step"
engine = create_engine(DATABASE_UR, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String, unique=True, nullable=False)

    profile = relationship("Profile", uselist=False, back_populates="user")

class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    bio = Column(String(300))
    profile_picture = Column(String(100))

    user = relationship("User", back_populates="profile")


Base.metadata.create_all(engine)


user_data = [
    ('Elene1', 'Elene1@gmail.com'),
    ('Elene2', 'Elene2@gmail.com'),
    ('Elene3', 'Elene3@gmail.com'),
    ('Elene4', 'Elene4@gmail.com'),
    ('Elene5', 'Elene5@gmail.com')
]


profile_data = [
    (1,  "x", 'Lorem '),
    (2,  "xx", 'ipsum'),
    (3,  "xxx", 'Lorem ipsum '),
    (4,  "xxxx", 'ipsum Lorem'),
    (5,  "xxxxx", 'LoremLorem')
]

for user_data in user_data:
    user = User(**user_data)
    session.add(user)

for profile_data in profile_data:
    profile = Profile(**profile_data)
    session.add(profile)


session.commit()
session.close()
