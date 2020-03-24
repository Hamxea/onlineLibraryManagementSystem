import enum
from enum import IntEnum


class BookStatusEnum(enum.Enum):
    ACTIVE = 1
    PASSIVE = 0

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class GenderEnum(enum.Enum):
    MALE = 1
    FEMALE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class BookCategoryEnum(enum.Enum):
    PERIODICAL = 1  # 'Periodical'
    ENGLISH = 2  # 'English'
    MATH = 3  # 'Math'
    SCIENCE = 4  # 'Science'
    ENCYCLOPEDIA = 5  # 'Encyclopedia'
    FILIPINIANA = 6  # 'Filipiniana'
    NEWSPAPER = 7  # 'Newspaper'
    GENERAL = 8  # 'General'
    REFERENCE = 9  # 'Reference'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
