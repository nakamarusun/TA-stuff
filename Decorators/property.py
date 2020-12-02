class Student:

    def __init__(self):
        self.__sname = ""

    @property
    def sname(self):
        return "my name is " + self.__sname

    @sname.setter
    def sname(self, sname):
        if not sname.isnumeric():
            self.__sname = sname


me = Student()
me.sname = "Edsel"