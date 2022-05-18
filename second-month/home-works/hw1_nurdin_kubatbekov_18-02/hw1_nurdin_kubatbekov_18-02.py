class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname} \n Age: {self.age} \n Is married: {self.is_married} \n')

    def output(self):
        return f'full name: {self.fullname} \n' \
               f'age: {self.age} \n' \
               f'is married: {self.is_married} \n'


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        res = sum(self.marks) / len(list)
        return res


class Teacher(Person):
    salary = 10000

    def __init__(self, fullname, age, is_married, exp=3):
        super().__init__(fullname, age, is_married)
        self.exp = exp

    def teacher_money(self):
        if self.exp > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.exp-3))
            return new_salary


teacher_aleksei = Teacher('Aleksei', 30, True, 10)

print(f'Name: {teacher_aleksei.fullname} \n Age: {teacher_aleksei.age} \n Is married: {teacher_aleksei.is_married}')
print(teacher_aleksei.teacher_money())


def create_student():
    student_nurdin = Student(fullname='Nurdin', age=18, is_married=False, marks={
        'English': 3,
        'History': 5,
        'Programming': 5,
        'physics': 5
    })
    student_erbol = Student(fullname='Erbol', age=18, is_married=True, marks={
        'English': 5,
        'History': 3,
        'Programming': 4,
        'physics': 2
    })
    student_syimyk = Student(fullname='Erbol', age=18, is_married=True, marks={
        'English': 4,
        'History': 5,
        'Programming': 5,
        'physics': 3
    })

    results = [student_nurdin, student_erbol, student_syimyk]
    return results


students = create_student()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f'Name: {i.fullname} \n'
          f'Married: {i.is_married} \n'
          f'Average marks: {sum(list) / len(list)} \n')

    # sum(list) / len(list)