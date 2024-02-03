# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

class Person:
  
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, first, last):
    self.first = first
    self.last = last
  def speak(self):
    return str(self.last + ", " + self.first)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

print(me.speak())
print(you.speak())
