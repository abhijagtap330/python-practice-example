class Employee:
    
    num_of_employee = 0
    raise_amount = 2
    
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_employee += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay =  emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 
        
emp1 = Employee("Abhijeet","Jagtap",30000)
emp2 = Employee("sam","user",40000)

print(Employee.num_of_employee)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str = 'John-Doe-10000'

new_emp1 = Employee.from_string(emp_str)
# first, last, pay =  emp_str.split('-')
# new_emp1 = Employee(first, last, pay)

print(new_emp1.email)
print(new_emp1.pay)

import datetime

my_date = datetime.date(2024, 8, 10)
print(Employee.is_workday(my_date))



class InputOutString(object):
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Enter Your Name : ")
        
    def printString(self):
        print(self.s.upper())

a = InputOutString()
a.getString()
a.printString()