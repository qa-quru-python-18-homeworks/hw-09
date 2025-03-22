import os
from datetime import datetime


class Student:
    def __init__(self, first_name: str, last_name: str, gender: str, email: str, mobile_number: str,
                 birth_date: datetime.date,
                 subjects: list, hobbies: tuple, picture: str, address: str, state: str, city: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__mobile_number = mobile_number
        self.__birth_date = birth_date
        self.__subjects = subjects
        self.__hobbies = hobbies
        self.__picture = picture
        self.__address = address
        self.__state = state
        self.__city = city

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def gender(self):
        return self.__gender

    @property
    def email(self):
        return self.__email

    @property
    def mobile_number(self):
        return self.__mobile_number

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def subjects(self):
        return self.__subjects

    @property
    def hobbies(self):
        return self.__hobbies

    @property
    def picture(self):
        return self.__picture

    @property
    def address(self):
        return self.__address

    @property
    def state(self):
        return self.__state

    @property
    def city(self):
        return self.__city


class StudentSubmittedView:
    def __init__(self, student):
        self.__student = student

    @property
    def name(self):
        return f'{self.__student.first_name} {self.__student.last_name}'

    @property
    def email(self):
        return self.__student.email

    @property
    def gender(self):
        return self.__student.gender

    @property
    def mobile_number(self):
        return self.__student.mobile_number

    @property
    def birth_date(self):
        date_obj = datetime.strptime(self.__student.birth_date, "%d %B %Y")
        return date_obj.strftime("%d %B,%Y")

    @property
    def subjects(self):
        return ', '.join(self.__student.subjects)

    @property
    def hobbies(self):
        return ', '.join(self.__student.hobbies)

    @property
    def picture(self):
        filename = os.path.basename(self.__student.picture)
        return filename

    @property
    def address(self):
        return self.__student.address

    @property
    def state_and_city(self):
        return f'{self.__student.state} {self.__student.city}'
