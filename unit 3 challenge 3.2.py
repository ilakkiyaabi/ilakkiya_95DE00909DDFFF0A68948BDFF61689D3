'''Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA 
(Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), 
roll_number (string), and cgpa (float). Test the function with different input lists of students.'''


class Student:
  def __init__(self , name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number 
    self.cgpa = cgpa
def sort_students(student_list):
  sort_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sort_students
students = [Student("tamil","A123", 7.8),
           Student("arasan","A124", 8.9),
           Student("vella","A125", 9.1),
           Student("aishu","A126", 9.9),]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name {}, Roll Number: {}, CGPA:  {}".format(student.name,student.roll_number,student.cgpa))