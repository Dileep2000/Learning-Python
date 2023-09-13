print("Class and Objects")

print("Class")


class Game:
    environment = "Greenery"

    def __init__(self):
        self.game_name = "Coding Blocks"
        self.high_score = 10000
        self.ranking = {}


class GameCharater(Game):
    # attributes
    name = ''
    health = 100
    position = [0, 0]

    # initializer
    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.position = position
        self.health = 100

    # behaviours
    def move_by(self, position):
        self.position[0] += position[0]
        self.position[1] += position[1]

    def heal_self(self, heal_amount):
        self.health += heal_amount
        if self.health > 100:
            self.health = 100


class Class:
    def __init__(self, course):
        self.className = course
        self.professor = "Soumaya"
        self.timings = "Tuesday/Thursday 9:30 to 9:50 AM"


class Student(Class):
    def __init__(self, name, stud_id, course):
        super().__init__(course)
        self.name = name
        self.stud_id = stud_id

    def __str__(self):
        return "My name is {} and my student ID is {}".format(self.name, self.stud_id)


if __name__ == "__main__":
    character1 = GameCharater("Dileep", [100, 100])
    print(character1.name)
    print(character1.game_name)
    student1 = Student("Dileep", "1002169540", "5300 Foundation to Computing")
    print(student1)