#საშინაო დავალება 1
#მარიამ ლორია 
#ჯგუფი 15
#2
class Calculator:
  def __init__(self, a, b):
    self.firstnumber = a
    self.secondnumber = b
  
  def add(self):
        print('sum of two no', self.firstnumber + self.secondnumber)
  def sub(self):
        print('sub of two no', self.firstnumber - self.secondnumber)
  def mul(self):
        print('mul of two no', self.firstnumber * self.secondnumber)
  def div(self):
      print('div of two no', self.firstnumber / self.secondnumber)

p5 = Calculator(22, 36)
p5.add() 
p5.sub()
p5.mul()
p5.div()

#3
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return (self.length + self.width) * 2

  def print_info(self):
    return f"Length - {self.length}, Width - {self.width}, Area - {self.area()}, Perimeter - {self.perimeter()}"

if __name__ == "__main__":
  r = Rectangle(5,6)
  print(r.print_info())

#4  
import csv

csv_file = open('dataset1.csv')
for row in csv_file:
  print(row)

csv_file.close()
  reader = csv.reader(Emploee)
  for row in reader:
    print(row)

class Employee:
  def __init__(self, name=row[1], surname=row[2], age=row[3], salary=row[4]):
    self.name = name
    self.surname = surname
    self.age = age
    self.salary = salary

