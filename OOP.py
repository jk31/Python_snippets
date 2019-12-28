class Employee:
    pass

emp_1 = Employee()
emp_1.first = "Vorname"
emp_1.last = "Nachname"
emp_1.pay = 6000

# This causes too much trouble. Now create **instance variables** directly in the class.

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

emp_1 = Employee("Peter", "Whatever", 6000)
print(emp_1.__dict__)
print(help(Employee))

#  Now add a **method**.

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Peter", "Whatever", 6000)

print(emp_1.fullname())
print(Employee.fullname(emp_1)) # this is what actually happens when run first print

# **Class variables** are equal in all instances

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # need Employee(or self) for class variable

emp_1 = Employee("Peter", "Whatever", 6000)

# changing class variables
# global
Employee.raise_amt = 1.5
# individual
emp_1.raise_amt = 1.3

# This is important because the function apply_raise depends either on Employee. or self.

**Class methods** and **static methods**

#  Regular methods take "self" as first argument. But what if we wnat class as first argument.

import datetime

class Employee:
    
    num_of_emps = 0 
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # need Employee(or self) for class variable
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    # alternative constructur
    @classmethod
    def from_string(cls, emp_str):
        first, last, name = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Peter", "Whatever", 6000)
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

#  **Inheritance** for e.g. subclasses

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # need Employee(or self) for class variable
        
class Developer(Employee):
    raise_amt = 1.10 # for own developer raise_amt
    
    # add more variables
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_empts(self):
        for emp in self.employees:
            print("-->", emp.fullname())
        
        
dev_1 = Developer("Peter", "Whatever", 6000, "C++")
mgr_1 = Manager("Sue", "Smith", 9000, [dev_1])

print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Manager))

 # **Magic** and **Dunder**  
 # Change build-in behavior, e.g. for `print(...)`

class Employee:   

    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
                
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) # need Employee(or self) for class variable
        
    def __repr__(self):
        return f"{self.first, self.last, self.pay} used if no str for printing"
    
    def __str__(self):
        return f"{self.first, self.last, self.pay} by using the str method"
    
    def __add__(self, other):
        return self.pay + other.pay
        
    
emp_1 = Employee("Peter", "B", 6000)
emp_2 = Employee("Lukas", "Ar", 7000)

emp_1 + emp_2

# **Property** decorators - Getters, Setters, Deleters  
# After you initialize an employee and change later the name, the email adress will not be altered corretly. One way would be to change it aswell manually but there is an other way.

# `@property` makes an method to attribute, so you don't have to use `...()` at the end of the method

# With a `@X.setter` you can change the attributes aswell

# With a `@x.deleter` you can `del` attributes

class Employee():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
         
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
    
emp_1 = Employee("John", "Smith")
emp_1.email
