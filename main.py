# parent class
class Person( object ):

      # _init_ is known as the constructor
      def _init_(self, name, idnumber):
            self.name = name 
            self.idnumber = idnumber
      def display(self):
            print(self.name)
            print(self.idnumber)      


# child class 
class Employee(Person):
      def _init_(self, name, 
                 idnumber, salary,post):
            self.salary = salary
            self.post = post 

            # invoking the _init_of the parent class
            Person._init_(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Michael', 20250070, 15000, "Intern")
b= Employee('Olamide', 20250080, 75000, "Manger")     
c = Employee('Rachael', 20250090, 45000, "CEO")       

# calling afunction of the class Person using its instance
a.display()
b.display()
c.display()

               