# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)




import time


class My_String(str):


    def __new__(cls, value, name):

        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance

    def __init__(self, value, name):

        self.name = name
        self.value = value

    def __str__(self):
        return f'"{self.name}" и  "{self.value}"'

    def __repr__(self):
        return f'({self.name}, {self.value})'


if __name__ == "__main__":
    string_1 = My_String('new', 'string_1')
    print(string_1)
    print(string_1.upper())
    print(string_1.title())
    print(string_1.time)
    print(string_1.name)