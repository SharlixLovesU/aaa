import time

class Pupil():
    def __init__(self, Surname, name, Mark):
        self.Surname = Surname
        self.Name = name
        self.Mark = Mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname, pupil.Name, "-", pupil.Mark)
        print("\n")

def print_five(pupils):
    print("Відмінники:")
    for pupil in pupils:
        if pupil.Mark == 5:
            print(pupil.Surname)
    print("\n")

def find_average(pupils):
    average = 0
    for pupil in pupils:
        average += pupil.Mark
    average /= len(pupils)
    print("Середня оцінка класу:", average)

start_time = time.time()
with open("aa.txt", 'r', encoding = "UTF-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], data[1], data[2])
        pupils.append(pupil)
print_class(pupils)
print_five(pupils)
find_average(pupils)
print("Час виконання:", (time.time()-start_time), "секунд")