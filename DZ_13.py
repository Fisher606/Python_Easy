class UserException(Exception):
    pass


class UserTypeStrError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'"Это должно" {self.value}  быть текстом'


class UserTypeTextError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value.isalpha():
            return f'Это значение {self.value} буквенное'
        elif not self.value.istitle():
            return f'Это значение {self.value} с большой буквы'


class UserLessonsError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'"Предмет {self.value} не функционирует"'


class UserEstimateError(UserException):
    def __init__(self, value, lower, upper):
        self.value = value
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = ''
        if self.value < self.lower:
            text = 'меньше нижнего таргета'
        elif self.value > self.lower:
            text = 'больше верхнего таргета'
        return f'Результат {self.value} {text} оценки границы. Надо попадать в диапазон ({self.lower}, {self.upper}).'