class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("Enter the Roll Number")
    roll = input()
    print(self.firstname, self.lastname,roll)


print("Enter the 1st name:")
f= input()
print("Enter the last name")
l = input()
x = Person(f, l)
x.printname()