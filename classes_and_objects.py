#parent class
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, track: list, score: float):
        self.name:str = name
        self.age:int = age
        self.track:list = track
        self.score: float = score

Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
def change_name(self, new_name):
    self.name = new_name
    return str(self, new_name)

def change_age(self, new_age):
    self.age = new_age
    return int(self, new_age)

def add_track(self, new_track):
    self.track = new_track
    return list(self, new_track)

def get_score(self, new_score):
    self.score = new_score
    return float(get_score)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

x = Student("Peter", 34, ["UI", "UX"],  )
x
#Unfinished code. I do not understand it well, my laptop battery is almost dead, no light.