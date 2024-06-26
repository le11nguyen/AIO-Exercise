class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name}, Year of Birth: {self.yob}"


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"{super().describe()}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"{super().describe()}, Subject: {self.subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"{super().describe()}, Specialist: {self.specialist}"


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        descriptions = [person.describe() for person in self.people]
        return f"Ward: {self.name}\n" + "\n".join(descriptions)

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        return self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        total = sum(
            person.yob for person in self.people if isinstance(person, Teacher))
        count = sum(1 for person in self.people if isinstance(person, Teacher))
        return total/count


# Examples
# 2a:
student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()

# 2(b)
print()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.describe())

# 2(c)
print(f"\ nNumber of doctors : { ward1 . count_doctor ()}")

# 2(d)
print("\ nAfter sorting Age of Ward1 people ")
ward1.sort_age()
print(ward1.describe())

# 2(e)
print(f"\ nAverage year of birth ( teachers ): { ward1.compute_average()}")
