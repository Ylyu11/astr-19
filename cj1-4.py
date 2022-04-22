class Animal():
    def cat(self, name, length_of_the_legs, number_of_eyes):
        self.name = name
        self.length_of_the_legs = length_of_the_legs
        self.number_of_eyes = number_of_eyes
    def animal_name(self):
        print("The name of the animal is:", self.name)
    def leg_length(self):
        print("The length of the leg is:", self.length_of_the_legs)
    def eye_number(self):
        print("The number of eye is:", self.number_of_eyes)
print(Animal())
        

