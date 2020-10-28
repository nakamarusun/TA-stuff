from functools import reduce

eren = {
    "name": "Eren",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}

mikasa = {
    "name": "Mikasa",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}

armin = {
    "name": "Armin",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}

students = [eren, mikasa, armin]

for s in students:
    print("\nStudent Information:")
    for key in s:
        print("{}: {}".format(key, s[key]))

def avg(arr):
    """
    args:
        -arr: Array of numbers
    returns:
        float: the average of the numbers
    """
    return reduce(lambda x, y: x + y, arr) / len(arr)

# Homework = 10%
# Quizzes = 30%
# Tests = 60%

# Array rule: index 1 = homework, index 2 = quizzes,
# index 3 = tests

weight = [.1, .3, .6]
ex_arr = [55, 55, 100]
zip(weight, ex_arr)

print(avg(ex_arr))

def weighted_average(arr, weight):
    """
    args:
        -arr: Array of numbers
    returns:
        float: the average of the numbers based on the weight
    """

    return reduce(lambda x, y: y[0] * y[1] + x, list(zip(arr, weight)), 0)

def get_average(student):
    homework = avg(student["homework"])
    quizzes = avg(student["quizzes"])
    tests = avg(student["tests"])
    return homework*0.1 + quizzes*0.3 + tests*0.6

print(get_average(eren))