from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

# === Схемы для Категорий ===
class CategoryBase(BaseModel):
    # Field(...) означает, что поле обязательно. min_length=1 запрещает пустую строку
    title: str = Field(..., min_length=1, max_length=255, description="Название категории")

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Название не может быть пустым или состоять только из пробелов")
        return v

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    # Для обновления поле необязательное (можно передать None, чтобы не менять)
    title: Optional[str] = Field(None, min_length=1, max_length=255)

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise ValueError("Название не может быть пустым или состоять только из пробелов")
        return v

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True) 

# === Схемы для Книг ===
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Название книги")
    description: Optional[str] = None
    # ИСПРАВЛЕНИЕ: Цена должна быть строго больше нуля
    price: float = Field(..., gt=0, description="Цена должна быть больше нуля")
    url: Optional[str] = ""
    category_id: int

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Название книги не может быть пустым или состоять только из пробелов")
        return v

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    url: Optional[str] = None
    category_id: Optional[int] = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise ValueError("Название книги не может быть пустым или состоять только из пробелов")
        return v

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)