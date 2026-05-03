# Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# Regular Employee program
class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        Employee.__init__(self, name, salary)   # direct calling the base class salary
        self.bonus = bonus

    def calculate_salary(self):  # Polymorphism method is used again
        return self.salary + self.bonus


# Contract Employee program
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        Employee.__init__(self, name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Manager program
class Manager(Employee):
    def __init__(self, name, salary, allowance):
        Employee.__init__(self, name, salary)
        self.manager_allowance = allowance

    def calculate_salary(self):
        return self.salary + self.manager_allowance


# Example usage (no loop)
emp1 = RegularEmployee("Kishore", 30000, 5000)
emp2 = ContractEmployee("Ashok kumar", 200, 120)
emp3 = Manager("Suresh krishna", 50000, 15000)

print(emp1.name, emp1.calculate_salary())
print(emp2.name, emp2.calculate_salary())
print(emp3.name, emp3.calculate_salary())