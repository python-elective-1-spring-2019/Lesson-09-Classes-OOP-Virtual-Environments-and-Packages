class Dog:
    
    type = 'Labador' # Class variable

    def __init__(self, name, gender):
        self._name = name
        self._gender = gender


    def get_gender(self):
        return self._gender

    def change_gender(self):
        if self.gender == 'male':
            self.gender == 'Female'

    def __str__(self):
        return " "+self._name+ "," + self._gender+" " 

    def __repr__(self):
        return 

class Puddle(Dog):
    
    def __init__(self, name, gender):
        return super().__init__(name, gender)



