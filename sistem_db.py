#== Importando o banco de dados e os atributos dele
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#== criação do banco de dados
bd = create_engine('sqlite:///banco_de_dados.db')

#---- Cria a sessao ----#
Session = sessionmaker(bind=bd)
session = Session()

#== declara as bases do banco de dados==
Base = declarative_base()

#=== classe pra criar o usuario===#
class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String)
    password = Column("password", String)
    active = Column("active", Boolean)

    def __init__(self, name, email, password, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.active = active


#====== classe pra criar os livros ====#
class Book(Base):
    __tablename__ = "book"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String)
    author = Column("author", String)
    pages = Column("pages", Integer)
    owner = Column("owner", Integer, ForeignKey("user.id"))

    def __init__(self, title, author, pages, owner):
        self.title = title
        self.author = author
        self.pages = pages
        self.owner = owner


Base.metadata.create_all(bind=bd)
