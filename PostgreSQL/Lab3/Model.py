import time
from faker import Faker
from random import *
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:ndeene28082002@localhost:5432/Library', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

fake = Faker()


class Author(Base):
    __tablename__ = 'Author'
    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    origin = Column(String)

    authors = relationship('Book')

    def __init__(self, author_id: int, name: str, origin: str):
        self.author_id = author_id
        self.name = name
        self.origin = origin


class Book(Base):
    __tablename__ = 'Book'
    book_id = Column(Integer, primary_key=True)
    sub_id = Column(Integer, ForeignKey('Author.author_id'))
    author_id = Column(Integer, ForeignKey('Subscription.sub_id'))
    title = Column(String)
    genre = Column(String)

    def __init__(self, book_id: int, sub_id: int, author_id: int, title: str, genre: str):
        self.book_id = book_id
        self.sub_id = sub_id
        self.author_id = author_id
        self.title = title
        self.genre = genre


class Subscription(Base):
    __tablename__ = 'Subscription'
    sub_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    subscriptions = relationship('Book')

    def __init__(self, sub_id: int, name: str, email: str):
        self.sub_id = sub_id
        self.name = name
        self.email = email


def connect():
    Base.metadata.create_all(engine)


def insert(table, inp):
    if table == 1:
        lib = Author(inp[0], inp[1], inp[2])
        session.add(lib)
        session.commit()

    elif table == 2:
        lib = Book(inp[0], inp[1], inp[2], inp[3], inp[4])
        session.add(lib)
        session.commit()

    elif table == 3:
        lib = Subscription(inp[0], inp[1], inp[2])
        session.add(lib)
        session.commit()


def insert_rand(table, count):
    if table == 1:
        for i in range(0, count):
            lib = Author((session.query(Author.author_id).count() + 1), fake.name(), fake.country())
            session.add(lib)
            session.commit()

    elif table == 2:
        r_s = randrange(1, session.query(Subscription.sub_id).count())
        r_a = randrange(1, session.query(Author.author_id).count())
        r_g = ['bio', 'novel', 'fairy tale', 'prose', 'poetry', 'fiction', 'narrative', 'drama', 'article']

        lib = Book((session.query(Book.book_id).count() + 1), r_s, r_a, fake.word(), choice(r_g))
        session.add(lib)
        session.commit()

    elif table == 3:
        lib = Subscription((session.query(Subscription.sub_id).count() + 1), fake.name(), fake.email())
        session.add(lib)
        session.commit()


def update(table, inp):
    n_id = inp[0]
    column = inp[1]
    new = inp[2]

    if table == 1:
        if column == 1:
            lib = session.query(Author).filter(Author.author_id == int(n_id)).first()
            lib.name = new
            session.commit()

        elif column == 2:
            lib = session.query(Author).filter(Author.author_id == int(n_id)).first()
            lib.origin = new
            session.commit()

    elif table == 2:
        if column == 1:
            lib = session.query(Book).filter(Book.book_id == int(n_id)).first()
            lib.sub_id = new
            session.commit()

        elif column == 2:
            lib = session.query(Book).filter(Book.book_id == int(n_id)).first()
            lib.author_id = new
            session.commit()

        elif column == 3:
            lib = session.query(Book).filter(Book.book_id == int(n_id)).first()
            lib.title = new
            session.commit()

        elif column == 4:
            lib = session.query(Book).filter(Book.book_id == int(n_id)).first()
            lib.genre = new
            session.commit()

    elif table == 3:
        if column == 1:
            lib = session.query(Subscription).filter(Subscription.sub_id == int(n_id)).first()
            lib.name = new
            session.commit()

        elif column == 2:
            lib = session.query(Subscription).filter(Subscription.sub_id == int(n_id)).first()
            lib.email = new
            session.commit()


def delete(table, nid):

    if table == 1:
        lib = session.query(Author).filter(Author.author_id == int(nid)).first()
        session.delete(lib)
        session.commit()

    elif table == 2:
        lib = session.query(Book).filter(Book.book_id == int(nid)).first()
        session.delete(lib)
        session.commit()

    elif table == 3:
        lib = session.query(Subscription).filter(Subscription.sub_id == int(nid)).first()
        session.delete(lib)
        session.commit()


def select_table(table, inp):
    string = inp[0]

    if table == 1:
        if string == 1:
            n_id = inp[1]
            lib = session.query(Author).filter(Author.author_id == int(n_id)).first()
            r = [lib.name, lib.origin]
            return r

        elif string == 2:
            lib = session.query(Author)
            return lib

    elif table == 2:
        if string == 1:
            n_id = inp[1]
            lib = session.query(Book).filter(Book.book_id == int(n_id)).first()
            r = [lib.sub_id, lib.author_id, lib.title, lib.genre]
            return r

        elif string == 2:
            lib = session.query(Book)
            return lib

    elif table == 3:
        if string == 1:
            n_id = inp[1]
            lib = session.query(Subscription).filter(Subscription.sub_id == int(n_id)).first()
            r = [lib.name, lib.email]
            return r

        elif string == 2:
            lib = session.query(Subscription)
            return lib


def search(table, inp):

    column = inp[0]

    if table == 1:
        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            lib = session.query(Author).filter(
                and_(Author.author_id >= int(a)), Author.author_id <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 2:
            txt = inp[1]
            start_t = time.time()

            lib = session.query(Author).filter(Author.name == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 3:
            txt = inp[1]
            start_t = time.time()

            lib = session.query(Author).filter(Author.origin == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

    elif table == 2:

        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            lib = session.query(Book).filter(
                and_(Book.book_id >= int(a)), Book.book_id <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            lib = session.query(Book).filter(
                and_(Book.sub_id >= int(a)), Book.sub_id <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            lib = session.query(Book).filter(
                and_(Book.author_id >= int(a)), Book.author_id <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 4:
            txt = inp[1]
            start_t = time.time()

            lib = session.query(Book).filter(Book.title == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 5:
            txt = inp[1]
            start_t = time.time()

            lib = session.query(Book).filter(Book.genre == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

    elif table == 3:
        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            lib = session.query(Subscription).filter(
                and_(Subscription.sub_id >= int(a)), Subscription.sub_id <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 2:
            txt = inp[1]
            start_t = time.time()

            lib = session.query(Subscription).filter(Subscription.name == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret

        elif column == 3:
            txt = inp[1]
            start_t = time.time()

            lib = session.query(Subscription).filter(Subscription.email == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [lib, search_duration]
            return ret
