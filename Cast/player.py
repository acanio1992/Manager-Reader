import Helper


class Player:

    def __init__(self, num, name, value, salary, age, temp):
        self.num = num
        self.name = name
        self.value = Helper.Helper.parse_string(value)
        self.salary = Helper.Helper.parse_string(salary)
        self.age = int(age)
        self.temp = int(temp.strip("'"))
        self.grade = self.calificar()

    def show_status(self):
        print(self.age)

    def calificar(self):
        grade = 0
        if self.age > 18:
            if self.value < 300000:
                grade = 1
            elif 300000 < self.value < 500000:
                grade = 2
            elif 500000 < self.value < 700000:
                grade = 3
            elif 700000 < self.value < 900000:
                grade = 4
            elif 900000 < self.value < 1100000:
                grade = 5
            elif self.value > 1100000:
                grade = 6
            return grade
        else:
            if self.value < 70000:
                grade = 1
            elif 70000 < self.value < 90000:
                grade = 2
            elif 90000 < self.value < 120000:
                grade = 3
            elif 120000 < self.value < 170000:
                grade = 4
            elif 170000 < self.value < 250000:
                grade = 5
            elif self.value > 250000:
                grade = 6
            return grade
