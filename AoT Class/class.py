from functools import reduce

def avg(arr):
    """
    args:
        -arr: Array of numbers
    returns:
        float: the average of the numbers
    """
    return reduce(lambda x, y: x + y, arr) / len(arr)

class Student:

    weight = [0.1, 0.3, 0.6]

    def __init__(self, name):
        # Construct the Student object here
        # Using __init__ !
        self.name = name
        self.homework = []
        self.quizzes = []
        self.tests = []

    def avg_homework(self):
        return avg(self.homework)

    def avg_quizzes(self):
        return avg(self.quizzes)
    
    def avg_tests(self):
        return avg(self.tests)

    def overall_avg(self):
        return (
        self.avg_homework() * Student.weight[0] +
        self.avg_quizzes() * Student.weight[1] +
        self.avg_tests() * Student.weight[2])

    def is_higher_avg_than(self, another_student):
        # Compare the current student's score to another.
        # Returns true if self is higher
        # Otherwise, false

        return self.overall_avg() > another_student.overall_avg()


eren = Student("Eren")
eren.homework += [90, 97, 75, 92]
eren.quizzes += [88, 40, 94]
eren.tests += [75, 90]

mikasa = Student("Mikasa")
mikasa.homework += [100, 92, 98, 100]
mikasa.quizzes += [82, 83, 91]
mikasa.tests += [89, 97]

print("Eren avg: {}".format(eren.overall_avg()))
print("Mikasa avg: {}".format(mikasa.overall_avg()))

Student.weight = [.5, .3, .2]

print("Eren new avg: {}".format(eren.overall_avg()))
print("Mikasa new avg: {}".format(mikasa.overall_avg()))

print()
print("Mikasa's score is higher than Eren's: {}".format(
    mikasa.is_higher_avg_than(eren)
    ))

print("Eren's score is higher than Mikasa's: {}".format(
    eren.is_higher_avg_than(mikasa)
    ))