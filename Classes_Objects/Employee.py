class Employee:


   def __init__(self,name,designation):
     self.name=name;
     self.designation=designation;


   def display(self):
     print("Name",self.name)
     print("Designation",self.designation)


emp2=Employee("Sachin","Developer");

emp2.display();
