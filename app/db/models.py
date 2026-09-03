from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # ИСПРАВЛЕНИЕ 1: Добавили unique=True, чтобы нельзя было создать две одинаковые категории
    title = Column(String, unique=True, index=True)
    
    # ИСПРАВЛЕНИЕ 2: Добавили cascade="all, delete-orphan"
    # Теперь при удалении категории SQLAlchemy сам удалит все связанные книги
    books = relationship("Book", back_populates="category", cascade="all, delete-orphan")

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    url = Column(String, default="")
    
    # ИСПРАВЛЕНИЕ 3: Добавили ondelete="CASCADE" на уровне самой базы данных
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="books")