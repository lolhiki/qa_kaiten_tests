class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"{self.brand}, {self.model}, {self.year}")


def task_2_2_car():
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("BMW", "X5", 2023)
    car3 = Car("Lada", "Vesta", 2021)
    car1.print_car_info()
    car2.print_car_info()
    car3.print_car_info()


class Lead:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name: str):
        self.name = new_name


def task_2_2_lead():
    lead = Lead("Ivan")
    print(lead.name)
    lead.change_name("Anton")
    print(lead.name)


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


def task_2_2_student():
    students = [
        Student("Анна", 20, [4.5, 5.0, 4.8]),
        Student("Борис", 21, [3.2, 4.0, 3.8]),
        Student("Вера", 19, [4.9, 5.0, 4.7]),
    ]
    good_students = [s for s in students if s.get_avg_grade() > 4.1]
    for s in good_students:
        print(f"{s.name}: {s.get_avg_grade()}")


if __name__ == "__main__":
    task_2_2_car()
    task_2_2_lead()
    task_2_2_student()
