class Student:

    def __init__(self, roll, name, gpa):
        self.roll = roll
        self.name = name
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False