from datetime import datetime, date

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, work:str) -> None:
        if self.age >= 16:
            self._work = work
        else:
            print('Ты слишком мал')

    # @property
    def passport(self, *args) -> None:
        self.passport = Passport(*args)

    def dict(self) -> None:
        self.dict = self.__dict__
        for el in self.dict:
            print(el)
            if isinstance(self.dict[el], dict):
                print(el)
                # self.dict[el] = self.__getattribute__(el).__dict__


        # if isinstance(self.passport, Passport):
        #     self.dict['passport'] = self.passport.__dict__
        # return self.dict


class Passport:

    def __init__(self, num, issue='2015-5-5', validity='2020-5-5'):
        self.num = num
        self.issue = datetime.strptime(issue, '%Y-%m-%d').date()
        self.validity = datetime.strptime(validity, '%Y-%m-%d').date()


v = Person('Vasya', 'Pupkin', 22)
v.passport('123', '2015-1-1', '2025-1-1')