class Animal:
  def __init__(self, name, length_of_the_legs, number_of_eyes):
    self.name = name
    self.length_of_the_legs = length_of_the_legs
    self.number_of_eyes = number_of_eyes
  def myfunc(self):
    print("The name of the animal is:" + self.name)
    print("The length of the leg is:", self.length_of_the_legs, "cm")
    print("The number of eye is:", self.number_of_eyes)
cat = Animal("cat", 43, 2)
cat.myfunc()
